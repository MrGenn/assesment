#importing time to space out messages
import time
#this is the answers to the questions.
Answers = ("6", "56", "544798")
trys = (3)

#this code introduced the quiz and who made it
print("welcome to my quiz!")
time.sleep (0.3)
print("this was made by sam burrows")
time.sleep (0.3)
name = input("what is your name? ")
time.sleep (0.3)
print("hello there",name,"!")
time.sleep (0.3)

#this asks the first question
print("now lets begin our quiz!")
time.sleep (0.3)
for x in range(trys):
  print("you have", trys,"left!")
  question1 = input("first question, what is 3 + 3?: ")
  if question1 == Answers[0]:
    #this resets the try counter
    trys = 3
    print("goodjob!")
    #this asks the second question
    print("you have", trys,"left!")
    question2 = input("question 2, what is 56? ")
    if question2 == Answers[1]:
      #this also resets the try counter
      trys = 3
      print("im gonna kill your family!")
      #this asks the third question
      print("you have", trys,"left!")
      question3 = input("question 3! what is 223354 + 321444? ")
      if question3 == Answers[2]:
        print("kys")
#these punish the player for messing up, silly player!
      else:
        print("fail!")
        trys -= 1
        time.sleep (0.8)
        if trys in range (1,4):
          print("try again!")
        else:
          print("you lose! try again?")
      break
    else:
      print("fail!")
      trys -= 1
      time.sleep (0.8)
      if trys in range (1,4):
        print("try again!")
      else:
        print("you lose! try again?")
  else:
    print("fail!")
    trys -= 1
    time.sleep (0.8)
    if trys in range (1,4):
      print("try again!")
    else:
      print("you lose! try again?")