#importing time to space out messages
import time
#this is the answers to the questions.
Answers = ("6")

#this code introduced the quiz and who made it
print("welcome to my quiz!")
time.sleep (0.3)
print("this was made by sam burrows")
time.sleep (0.3)
name = input("what is your name? ")
time.sleep (0.5)
print("hello there ", name, "!")
time.sleep (0.3)

#this asks the first question
print("now lets begin our quiz!")
time.sleep (0.3)
question1 = input("lets begin, what is 3 + 3? ")
if question1 == Answers:
  print("goodjob!")
else:
  print("you fucking idiot!")
  time.sleep (0.8)
  print("try that again you fucking neanderthal!")