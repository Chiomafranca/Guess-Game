print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")
score = 0

answer = input("What dose Cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What dose GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
 
answer = input("What dose RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 3) * 100) + "%.")




