# GSEB-WebScraper

## Introduction & features
This scraper basically does work from your side to go through each roll number in given range and you can find all the results and also can find result by just name or surname or full name.

3 major results are declared in <http://gseb.org/> website are SSC, HSC science, HSC general. There are three different versions for each of them.  

You will able to store all the results in csv format.

## Instructions to use

Obviously you need to have python in your systems. Additionally, you need to have lxml, requests & BeautifulSoup. Else re & csv mostly will be included in default python installation.

### Installing lxml   
```pip install lxml```

### Intalling requests   
```pip install requests```

### Installing BeautifulSoup   
```pip install beautifulsoup4```

## Protips

You might need to know the roll numbers range starting and ending that you can get by general idea of students appearing in the examinations.
Generally, GSEB HSC science roll numbers have B in their initials and also it is of 6 digits. Something like this 
```B XXXXXX``` 
Also to start with roll numbers it starts from 100001 in most cases. Just try to search result of 100001, 100002 in <http://gseb.org/indexsci.html> if you get in line exam results you are good to go.

For SSC result there are more initials as compared to HSC science. 'A', 'B' , 'C' , 'S', 'P' initials are there because of huge number of students. Also, roll number is of 7 digits. So, you need to do little more work roll number looks like: ```A XXXXXXX``` 
You can try finding range over here <http://gseb.org/>. Trust me it just takes few mins to find range & then you are all set to scrape.

Same goes to this you need to find out sort of range. And then try searching end roll number of the results, General idea of it is to search the total number of students appeared in the exam.

#### For Search by name:
After installing you have to run ResultByName.py file. Reset the initial Value of roll to the intial roll number you analysed. Just change the string which you want to search (Commented in the code). I have assigned it to as per the latest result 2020 HSC Science GSEB result so need to worry about. You can shorten the range if you want to.

General practice to search by name is to search just by ```SURNAME NAME``` donot include fathers name because in some cases some might there might be fathers name with postfix 'Bhai' or 'Kumar' or 'Chandra' something like that. 

Wait for it let the code breath till it finds your result corresponding to the name with URL.

By the way you can also search by just name or just surname but that might result into great results. 

#### For scraping all the results
After installing just run Scraper.py Initialze the roll number (Commented in the code) analyzed by you before. I have assigned it to as per the latest result 2020 HSC Science GSEB result so need to worry about. You can shorten the range if you want to.

Let the code breath. Check the csv after the completion.

### Note 
Make sure you check the stopping condition as well according how much you want to scrape or search.

### Rate of scraping 
Generally you would scrape 20-30 results in a second. Again this is subject to website traffic and your internet speed. You would scrape atleast 20 results.
Finding results by name would be quicker

BOOM! you are good to go.
