import csv
import re
import requests
import lxml
from bs4 import BeautifulSoup

# Note:
# HSC General roll numbers are 6 digit ones. Also, they have 5 initials A, B, C, D, G, H, P, T, S
# While in the case of HSC science there is just 1 initials i.e. B (followed by 6 digits)

# Opening a file for the first time only
with open('12resultG2.csv', 'w') as resultfile:
    mywriter = csv.writer(resultfile, delimiter=',')
    mywriter.writerow(['Roll', 'Name', 'Result'])


count = 0
initials = 'G'  # Change this initials as per your convinience
roll = 200001  # Change the initial value as per the initial roll number analyzed by you
rollstr = str(roll)

# print(rollstr)
while count < 450000:  # Stopping condition depending upon how much range you want to scrape

    baseurl = base_url = 'http://gseb.org/3015ecruosnepo/gen/' + \
        initials + rollstr[0:2]+'/'+rollstr[2:4]+'/'+initials+rollstr+'.html'
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
            with open('12resultG2.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow([initials+rollstr, name, base_url])

            print(initials+rollstr, name, base_url)

        except ValueError:
            with open('12resultG2.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow(['A'+rollstr, 'Error', 'Error'])
            print(initials+rollstr, ': Error')

        count += 1
        roll += 1
        rollstr = str(roll)

    else:
        with open('12resultG2.csv', 'a', newline='') as resultfile:
            mywriter = csv.writer(resultfile, delimiter=',')
            mywriter.writerow(['A'+rollstr, '404', 'Error'])
        print(initials+rollstr, ': 404')

        count += 1
        roll += 1
        rollstr = str(roll)
