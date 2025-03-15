#declaring the correct answer as a variable 
answer = "Paris"
Answer = str(input("what is the capital fo france?")) #userinput with a question also using correct data type incase of user error 

if Answer.upper() == answer.upper(): #.upper() to ignore capitalization 
    print("answer is correct!")
else:
    print("answer is wrong")


#advanced requirement: quiz that asks for the capitals of 10 European countries.
#assigning values to the varibale named answer 
answer1 = "Berlin"
answer2 = "Rome"
answer3 = "Madrid"
answer4 = "Lisbon"
answer5 = "Amsterdam"
answer6 = "Athens"
answer7 = "Brussels"
answer8 = "Stockholm"
answer9 = "Vienna"
answer10 = "Paris"


#calling for userinput with a question
q1 = str(input("Whats is the capital of Germany"))

if q1.lower() == answer1.lower(): #.lower() to ignore capitalization 
    print("Correct")
else:
    print("Incorrect The correct answer is: ", answer1) #feedbakc on the right answer if its wrong 

q2 = str(input("Whats is the capital of Italy"))
if q2.lower() == answer2.lower():
  print("Correct")
else:
 print("Incorrect The correct answer is: ", answer2)

q3 = str(input("Whats is the capital of Spain"))
if q3.lower() == answer3.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer3)

q4 = str(input("Whats is the capital of Portugal"))
if q4.lower() == answer4.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer4)

q5 = str(input("Whats is the capital of Netherlands"))
if q5.lower() == answer5.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer5)

q6 = str(input("Whats is the capital of Greece"))
if q6.lower() == answer6.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer6)

q7 = str(input("Whats is the capital of Belgium"))
if q7.lower() == answer7.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer7)

q8 = str(input("Whats is the capital of Sweden"))
if q8.lower() == answer8.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer8)

q9 = str(input("Whats is the capital of Austria"))
if q9.lower() == answer9.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer9)

q10 = str(input("Whats is the capital of France"))
if q10.lower() == answer10.lower():
    print("Correct")
else:
 print("Incorrect The correct answer is: ", answer10)
 

