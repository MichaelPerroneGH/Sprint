# Michael Perrone Integration Project
# Quiz Game
# Sources/Help: Python Tutorial -Multiple Choice Quiz by Geek Tutorials on Youtube
# Sources/Help: Lesson 4 For loop with range Snakify
# Sources/Help: Concepts from Python Activities 1-15 

import random 
score = 0

# Question #1
answer1 = input(" When was Florida Gulf Coast Founded? \na. 1992 \nb. 1991 \nc. 1993 \nAnswer: ")
if answer1 == "b" or answer1 == "1991":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is 1991.")
    print("Score:", score)
    print("\n")

# Question #2
answer2 = input("What is the capital of Florida? \na. Tallahassee \nb. Orlando \nc. Jacksonville \nAnswer: ")
if answer2 == "a" or answer2 == "Tallahassee":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is Tallahassee.")
    print("Score:", score)
    print("\n")

# Question #3
answer3= input(" When was Florida granted Statehood? \na. 1817 \nb. 1825 \nc. 1845\nAnswer: ")
if answer3 == "c" or answer3 == "1845":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is 1845.")
    print("Score:", score)
    print("\n")

# Question #4
answer4 = input("Where is Disney World located? \na. Orlando \nb. Anaheim \nc. Tampa \nAnswer: ")
if answer4 == "a" or answer4 == "Orlando":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is Orlando.")
    print("Score:", score)
    print("\n")

# Question #5
answer5 = input("What building is COP 1500 loacated in?  \na. Edwards Hall  \nb. Howard Hall \nc. Holmes Hall  \nAnswer: ")
if answer5 == "c" or answer5 == "Holmes Hall":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is Holmes Hall.")
    print("Score:", score)
    print("\n")

# Question #6
answer6 = input("What is the largest city in Florida in terms of Area? \na. Orlando \nb. Jacksonville \nc. Miami   \nAnswer: ")
if answer6 == "b" or answer5 == "Jacksonville":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is Jacksonville.")
    print("Score:", score)
    print("\n")

# Question #7
answer7 = input("What is the largest river in Florida? \na. The St. Johns River \nb. The Mississippi River \nc. The Red River   \nAnswer: ")
if answer7 == "a" or answer5 == "The St. Johns River":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is The St. Johns River.")
    print("Score:", score)
    print("\n")

# Question #8
answer8 = input("How many counties does Florida have? \na. 66 \nb. 67 \nc. 65   \nAnswer: ")
if answer8 == "b" or answer5 == "67":
    score += 1
    print("You are Correct!")
    print("Score:", score)
    print("\n")
else:
    print("You are Incorrect. The answer is 67.")
    print("Score:", score)
    print("\n")


# Quiz Review
for score in range(1,9):
  print(score)
if score <= 6:
    print("You got these many questions correct:", score,)
elif score == 7:
    print("You got these many questions correct:", score, "Good job!")
else:
    print("You got these many questions correct:", score, "You got a perfect score!")

    
   

    
    
