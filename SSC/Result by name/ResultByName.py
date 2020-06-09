import requests
from bs4 import BeautifulSoup
import lxml

# Note:
# SSC roll numbers are 7 digit ones. Also, they have 5 initials A, B, C, S, P
# While in the case of HSC science there is just 1 initials i.e. B (followed by 6 digits)

findex = -1
count = 0
initials = 'A'  # You have to change these initials to 'B' if you wanna find the results by name in initials in 'B'
roll = 7000001  # Initial roll number analyzed by you 7 digit for SSC board
rollstr = str(roll)


while(findex == -1):
    baseurl = base_url = 'http://gseb.org/285soipmahc/ssc/' + \
        initials + rollstr[0:2]+'/'+rollstr[2:4]+'/'+initials+rollstr+'.html'
    # print(base_url)
    page = requests.get(base_url)
    # print(type(page))

    if page.status_code == requests.codes.ok:
        bs = BeautifulSoup(page.text, 'lxml')
        base_string = bs.find('table', class_='maintbl').find('td').prettify()
        # print(base_string)

        # Change the name you want to search (Order Should be SURNAME NAME MIDDLENAME)
        # Protip: If you don't know full name you can try with just surname or just name or surname + name
        findex = base_string.find('PATEL')

        if(findex == -1):
            print(rollstr + ': Nope')
            count += 1
            roll += 1
            rollstr = str(roll)
        else:
            print(base_url)
            break
    else:
        print('404')

    if count > 319667:  # Stopping condition depending upon how much range you want to search
        break
