import requests
from bs4 import BeautifulSoup
import lxml

# Note:
# HSC General roll numbers are 6 digit ones. Also, they have 5 initials A, B, C, D, G, H, P, T, S
# While in the case of HSC science there is just 1 initials i.e. B (followed by 6 digits)

findex = -1
count = 0
initials = 'G'  # Change this initials as per your convinience
roll = 200001  # Change the initial value as per the initial roll number analyzed by you
rollstr = str(roll)


while(findex == -1):
    baseurl = base_url = 'http://gseb.org/3015ecruosnepo/gen/' + \
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
        findex = base_string.find('AJW')

        if(findex == -1):
            print(rollstr + ': Nope')
            count += 1
            roll += 1
            rollstr = str(roll)
        else:
            print(rollstr+': '+base_url)
            break
    else:
        print(rollstr+': 404')
        count += 1
        roll += 1
        rollstr = str(roll)

    if count > 25000:  # Stopping condition depending upon how much range you want to search
        break
