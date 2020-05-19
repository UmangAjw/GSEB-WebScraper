# GSEB-WebScraper

## Introduction & fetures
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
Generally, GSEB HSC science roll numbers have B in their initials and also it is of 6 digits. Something like this ```B XXXXXX``` 

Also to start with roll numbers it starts from 100001 in most cases. Just try to search result of 100001, 100002 in <http://gseb.org/> if you get in line exam results you are good to go. 
And then try searching end roll number of the results, General idea of it is to search the total number of students appeared in the exam.

#### For Search by name:
After installing you have to run ResultByName.py file. Reset the initial Value of roll to the intial roll number you analysed. Just change the string which you want to search. (Commented in the code)
General practice to search by name is to search just by ```SURNAME NAME``` donot include fathers name because in some cases some might there might be fathers name with postfix 'Bhai' or 'Kumar' or 'Chandra' something like that.

By the way you can also search by just name or just surname but that might result into great results. 

#### For scraping all the results
After installing just run Scraper.py Initialze the roll number (Commented in the code) analyzed by you before. 

BOOM! you are good to go.
