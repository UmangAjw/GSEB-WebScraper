import requests
from bs4 import BeautifulSoup
import lxml

findex = -1
count = 0
roll = 100001  # Initial roll number analyzed by you
rollstr = str(roll)

while(findex == -1):
    base_url = 'http://gseb.org/522lacigam/sci/B' + \
        rollstr[0:2]+'/'+rollstr[2:4]+'/'+'B'+rollstr+'.html'
    # print(base_url)
    page = requests.get(base_url)
    # print(type(page))

    if page.status_code == requests.codes.ok:
        bs = BeautifulSoup(page.text, 'lxml')
        base_string = bs.find('table', class_='maintbl').find('td').prettify()
        # print(base_string)
        findex = base_string.find('AJW')  # Change the name you want to search

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
        count += 1
        roll += 1
        rollstr = str(roll)

    if count > 119666:  # Stopping condition depending upon how much range you want to search
        break
