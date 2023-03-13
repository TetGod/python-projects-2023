# Landon Bowcutt
# 9/16/22
# Web Scraper


# inputs
import requests
from bs4 import BeautifulSoup

url = "http://www.quotationspage.com/random.php"

response = requests.get(url)
if response.ok:
    print("connected to "+url)
    soup = BeautifulSoup(response.text,"lxml")

##    # <p class="quote"> this is the tag for the quote
    # geting the quote from the soup by searching for its tags and class name
    quote = str(soup.find("dt",{"class":"quote"}))
    # clean up the quote by replacing any un needed parts of the String with "" nothing
    quote = quote.replace("<dt class=\"quote\">","")
    quote = quote.replace("</a> </dt>","")

    # loop through whats left of the string and colect the parts we need 
    createString = False # creat a bool we can toggel when we need to start creating the string
    x="" # create a place holder variable to create a new string in using cancatination
    for i in quote: #cycle through each char in the String 
        if i == ">": #if the char is > we need to start colecting the next charecters
            createString = True # toggel the bool to start collecting
        if createString: # if our bool is true 
            x += i # Start adding each char to String
    quote = x # set the string we built to quote variable

    # finish removing the un needed data
    quote = quote.replace(">"," ")
    quote = quote.capitalize()

    
    

# <span class="author" this is tag for the author
    name = str(soup.find("dd",{"class":"author"}))
    name = name.replace("<div class=\"icons\">","")
    name = name.replace("<dd class=\"author\">","")

    start = False
    end = False
    x = ""
    for i in range(len(name)):
        if name[i*-1] =="(":
            start = True
        if start and end == False:
            x+=name[i*-1]
            if name[i*-1] == "\"":
                end = True
    name = x
    name = name [6:len(name)-2:1]
    name = name[::-1]
    if name == "":
        name = "Unknown"
    print(quote)    
##    print(name)
        
            
