print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")

score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does PSU stands for? ").lower()
if answer == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%.")