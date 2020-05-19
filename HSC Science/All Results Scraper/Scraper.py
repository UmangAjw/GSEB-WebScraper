import csv
import re
import requests
import lxml
from bs4 import BeautifulSoup

# Opening a file for the first time only
with open('result.csv', 'w') as resultfile:
    mywriter = csv.writer(resultfile, delimiter=',')
    mywriter.writerow(['Roll', 'Name', 'Result'])

count = 0
roll = 100001  # Change the initial value as per the initial roll number analyzed by you
rollstr = str(roll)

while count < 119666:  # Stopping condition depending upon how much range you want to scrape

    baseurl = base_url = 'http://gseb.org/522lacigam/sci/B' + \
        rollstr[0:2]+'/'+rollstr[2:4]+'/'+'B'+rollstr+'.html'
    # print(baseurl)
    page = requests.get(baseurl)
    # print(type(page))

    if requests.codes.ok == page.status_code:
        bs = BeautifulSoup(page.text, 'lxml')
        base_string = bs.find('table', class_='maintbl').find('td').prettify()
        # print(base_string)
        try:
            name_index = base_string.index('Name')
            exact_name_string = base_string[name_index:]
            name = re.compile('</b>(.*)</span>',
                              re.DOTALL).search(exact_name_string)

            name = name.group(1).strip()
            # print(name)
            with open('result.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow([roll, name, base_url])

            print(rollstr, name, base_url)

        except ValueError:
            with open('result.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow([roll, 'Error', 'Error'])
            print(roll, ': Error')

        count += 1
        roll += 1
        rollstr = str(roll)

    else:
        with open('result.csv', 'a', newline='') as resultfile:
            mywriter = csv.writer(resultfile, delimiter=',')
            mywriter.writerow([roll, '404', 'Error'])
        print(roll, ': 404')

        count += 1
        roll += 1
        rollstr = str(roll)
