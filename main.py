#importing time to space out messages
import time
#this is the answers to the questions.
Questions = ("How many houses are there?: ", "who is the head of rutherford?: ", "how many gyms are there?: ","what colour is hillary?: ","what colour is ngata?: ","what colour is lydiard?: ","what colour is mansfield?: ")
Answers = ("6", "mrs koster", "3","red","green","orange","yellow")
points = 0

def wronganswer():
  global trys
  print("fail!")
  #every fail the player does, it takes 1 from the trys counter
  time.sleep(0.3)

def wincondition():
  if points >= 6:
    print("you win!")
  else:
    print("you lose...")

#this code introduced the quiz and who made it
print("welcome to my quiz!")
time.sleep(0.3)
print("this was made by sam burrows")
time.sleep(0.3)
name = input("what is your name? ")
time.sleep(0.3)
print("hello there", name)
time.sleep(0.3)
print("please use numberical numbers only and do all words in full lower case, also make sure everything is spelt correctly")

#this asks the first question
print("now lets begin our quiz!")
time.sleep(0.3)
question1 = input(Questions[0])
if question1 != Answers[0]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter
  print("goodjob!")
  time.sleep(0.3)
#this asks the second question
question2 = input(Questions[1])
if question2 != Answers[1]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter again
  print("goodjob!")
  time.sleep(0.3)
#this asks the third question
time.sleep(0.3)
question3 = input(Questions[2])
if question3 != Answers[2]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter
  print("goodjob!")
  time.sleep(0.3)
#this asks the fourth question
question4 = input(Questions[3])
if question4 != Answers[3]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter again
  print("goodjob!")
  time.sleep(0.3)
#this asks the fifth question
time.sleep(0.3)
question5 = input(Questions[4])
if question5 != Answers[4]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter
  print("goodjob!")
  time.sleep(0.3)
#this asks the sixth question
question6 = input(Questions[5])
if question6 != Answers[5]:
  wronganswer()
else:
  #this awards the player a point
  points += 1
  #this resets the try counter again
  print("goodjob!")
  time.sleep(0.3)
#this asks the final question
question7 = input(Questions[6])
if question7 != Answers[6]:
  wronganswer()
  time.sleep(0.3)
else:
  #this awards the player a point
  points += 1
  time.sleep(0.3)
wincondition()