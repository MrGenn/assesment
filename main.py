#importing time to space out messages
import time
#this is the answers to the questions.
Questions = ("1: ", "2: ", "3: ")
Answers = ("1", "2", "3")
trys = (3)
points = (0)

def wronganswer():
  global trys
  print("fail!")
  #every fail the player does, it takes 1 from the trys counter
  trys -= 1
  time.sleep(0.3)
  if trys in range(1, 4):
    print("try again!")
  else:
    print("you lose! try again!")

def wincondition():
  if points == 3:
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

#this asks the first question
print("now lets begin our quiz!")
time.sleep(0.3)
for x in range (trys):
  print("you have", trys, "tries left!")
  question1 = input(Questions[0])
  if question1 != Answers[0]:
    wronganswer()
  else:
    #this awards the player a point
    points += 1
    #this resets the try counter
    trys = 3
    print("goodjob!")
    time.sleep(0.3)
    for x in range (trys):
      #this asks the second question
      print("you have", trys, "tries left!")
      question2 = input(Questions[1])
      if question2 != Answers[1]:
        wronganswer()
      else:
        #this awards the player a point
        points += 1
        #this resets the try counter again
        trys = 3
        print("goodjob!")
        time.sleep(0.3)
        for x in range (trys):
          #this asks the third question
          print("you have", trys, "tries left!")
          question3 = input(Questions[2])
          if question3 != Answers[2]:
            wronganswer()
            time.sleep(0.3)
          else:
            #this awards the player a point
            points += 1
            time.sleep(0.3)
            wincondition()
            break
      break
  break