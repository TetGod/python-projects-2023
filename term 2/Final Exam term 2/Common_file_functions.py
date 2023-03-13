

def write_Question(list, open_file):
    for i in list:
        open_file.write(i+"\n")

open_file = open("exams/ExampleTest.txt", "w")
open_file.write("Landon Bowcutt\n")

question1 = ["Python","Why is Python a good language for beginning programmers to learn?","Python is free and easy to use ","Python comes with professional source control features ","Computer games written in Python are easier to sell","All of these are true","1","most people find python to be the easiest to use"]
question2 = ["Python","Why did Guido van Rossum create the Python language?","All of these are true ","Windows","Mac OS","Linux","answer","exp"]
question3 = ["Python","How many major releases have there been of the Python language?","As a hobby project over a Christmas break ","As part of his job in AT&T's Bell Labs","To meet the demand for an advanced language","In order to impress his friends","answer","exp"]
question4 = ["Python","Which of the following best describes the Python Software Foundation?","3","1","10","One per year since 1989","answer","exp"]
question5 = ["Python","The Python language was named after what thing?","A for-profit organization created to sell Python licenses","A job-posting website for Python programmers","The company that Guido van Rossum worked for when he created Python","Monty Python's Flying Circus TV show","answer","exp"]
question6 = ["Python","What kinds of things can you find at the www.python.org website?","option 1","option 2","option 3","option 4","answer","exp"]
question7 = ["Python","What file extension is normally given to Python source code?","option 1","option 2","option 3","option 4","answer","exp"]
question8 = ["Python","Which of the following terms best describes the Python component that translates Python source code into program output?","option 1","option 2","option 3","option 4","answer","exp"]
question9 = ["Python","Which of the following approaches can you use to run Python programs?","option 1","option 2","option 3","option 4","answer","exp"]
question10 = ["Python","Which of the following is an advantage to using our online Python engine?","option 1","option 2","option 3","option 4","answer","exp"]
question11 = ["Python","Which of the following steps must be taken to create and run Python programs on your own computer?","option 1","option 2","option 3","option 4","answer","exp"]
question12 = ["Python","How do you safely break a long Python statement across multiple lines?","option 1","option 2","option 3","option 4","answer","exp"]
question13 = ["Python","What happens if you write code that does not follow Python syntax rules?","option 1","option 2","option 3","option 4","answer","exp"]
question14 = ["Python","Which of the following statements will display the phrase Python is great!","option 1","option 2","option 3","option 4","answer","exp"]
question15 = ["Python","Which of the following best describes how Python statements are executed?","option 1","option 2","option 3","option 4","answer","exp"]
question16 = ["Python","How does Python use indentation (spacing of statements to the right)?","option 1","option 2","option 3","option 4","answer","exp"]
question17 = ["Python","Which of the following lines contains a valid Python comment?","option 1","option 2","option 3","option 4","answer","exp"]
question18 = ["Python","What is the purpose of leaving comments in your source code?","option 1","option 2","option 3","option 4","answer","exp"]
question19 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question20 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question21 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question22 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question23 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question24 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]
question25 = ["Python","Question","option 1","option 2","option 3","option 4","answer","exp"]

questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14,question15,question16,question17,question18,question19,question20,question21,question22,question23,question24,question25]

for question in questions:
    write_Question(question,open_file)


open_file = open("exams/ExampleTest.txt", "r")
list = open_file.readlines()
print(list)

for i in range(len(list)):
    list[i] = list[i].strip("\n")

print(list)
open_file.close()

open_file = open("exams/ExampleTest.txt", "W")
open_file.write("Landon Bowcutt python term 2 final exam\n")
open_file.write("Question Category\n")
open_file.write("what is the Question to ask?\n")
open_file.write("Option 1\n")
open_file.write("Option 2\n")
open_file.write("Option 3\n")
open_file.write("Option 4\n")
open_file.write("answer\n")
open_file.write("exp\n")
for i in range(24):
    open_file.write("""category
    question
    option 1
    option 2
    option 3
    option 4
    answer
    exp
    """)


open_file.close()