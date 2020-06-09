import csv
import re
import requests
import lxml
from bs4 import BeautifulSoup

# Note:
# SSC roll numbers are 7 digit ones. Also, they have 5 initials A, B, C, S, P
# While in the case of HSC science there is just 1 initials i.e. B (followed by 6 digits)

# Opening a file for the first time only
with open('10resultA.csv', 'w') as resultfile:
    mywriter = csv.writer(resultfile, delimiter=',')
    mywriter.writerow(['Roll', 'Name', 'Result'])


count = 0
initials = 'A'  # You have to change these initials to 'B' when you scrape all the results with 'A' initials
roll = 7000001  # Change the initial value as per the initial roll number analyzed by you
rollstr = str(roll)

# print(rollstr)
while count < 319667:  # Stopping condition depending upon how much range you want to scrape

    baseurl = base_url = 'http://gseb.org/285soipmahc/ssc/' + \
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
            with open('10resultA.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow(['A'+rollstr, name, base_url])

            print('A'+rollstr, name, base_url)

        except ValueError:
            with open('10resultA.csv', 'a', newline='') as resultfile:
                mywriter = csv.writer(resultfile, delimiter=',')
                mywriter.writerow(['A'+rollstr, 'Error', 'Error'])
            print('A'+rollstr, ': Error')

        count += 1
        roll += 1
        rollstr = str(roll)

    else:
        with open('10resultA.csv', 'a', newline='') as resultfile:
            mywriter = csv.writer(resultfile, delimiter=',')
            mywriter.writerow(['A'+rollstr, '404', 'Error'])
        print('A'+rollstr, ': 404')

        count += 1
        roll += 1
        rollstr = str(roll)
