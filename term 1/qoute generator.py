# Landon Bowcutt
# 9/8/2022
# inspirational qoute generator

# imports
import random
import requests
from bs4 import BeautifulSoup
# global variables
welcomes =["Top of the morning to you","Good Morning","ohayo","доброе утро dobroye utro","Buenos dias","Bonjour",
              "buổi sáng","sugeng enjang","Buongiorno","dobré ráno","dobro jutro","excellent morning","god morgen","Καλημέρα kalimera",
              "Guten Morgen","صبح بخیر","super morning","Goedemorgen","günaydın","bonum mane","добро утро"]

url = "http://www.quotationspage.com/random.php"




quote_1 = "\"When you have a dream, you've got to grab it and never let go.\""
quote_1_name = "Carol Burnett"
quote_2 = "\"Nothing is impossible. The word itself says 'I'm possible.\""
quote_2_name = "Audrey Hepburn"
quote_3 = "\"There is nothing impossible to they who will try.\""
quote_3_name = "Audrey Hepburn"
quote_4 = "\"The bad news is time flies. The good news is you're the pilot.\""
quote_4_name = "Michael Altshule"
quote_5 = "\"Life has got all those twists and turns. You've got to hold on tight and off you go.\""
quote_5_name = "Nicole Kidman"
quote_6 = "\"Keep your face always toward the sunshine, and shadows will fall behind you.\""
quote_6_name = "Walt Whitman"
quote_7 = "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\""
quote_7_name = "Winston Churchill"
quote_8 = "\"You define your own life. Don't let other people write your script. — Oprah Winfrey\""
quote_8_name = "Oprah Winfrey"
quote_9 = "\"You are never too old to set another goal or to dream a new dream.\""
quote_9_name = "Malala Yousafzai"
quote_10 = "\"It’s worth remembering that it is often the small steps, not the giant leaps, that bring about the most lasting change.\""
quote_10_name = "Queen Elizabeth"

quotes =[quote_1,quote_2,quote_3,quote_4,quote_5,quote_6,quote_7,quote_8,quote_9,quote_10]

names = [quote_1_name,quote_2_name,quote_3_name,quote_4_name,quote_5_name,quote_6_name,quote_7_name,quote_8_name,quote_9_name,quote_10_name]

# function
def quote_card(quote,name):
    size = len(quote)+5# get the size of the quote and add 5 to ir
    welcome = random.choice(welcomes)
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t"+"="*(size)+" ")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+welcome+" "*(size-len(welcome)-2)+"|")
    print("\t\t\t\t|"+quote+" "*(size-len(quote)-2)+"|")
    print("\t\t\t\t| \t---"+name+" "*(size-len(name)-12)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t|"+" "*(size - 2)+"|")
    print("\t\t\t\t"+"="*(size)+" ")

def scraper(url):
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
    return quote,name
    
# main
def main():
    # build program
    quote, name = scraper(url)
    quote_card(quote,name)
    

# start the program      
main()

# hold program open till user hits enter
input()
 
