print("Welcome to my League Of Legends Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the hardest ADC? ")
if answer.lower() == "aphelios":
    print("Correct!")
    score += 1
else:
    print("Incorrect......")

answer = input("Who is the most cringe Top Laner? ")
if answer.lower() == "teemo":
    print("Correct!")
    score += 1 
else:
    print("Incorrect......")

answer = input("Who is the coolest Mid Laner? ")
if answer.lower() == "sylas":
    print("Correct!")
    score += 1
else:
    print("Incorrect......")

answer = input("Who is the scariest Jungler? ")
if answer.lower() == "eveylnn":
    print("Correct!")
    score += 1
else:
    print("Incorrect......")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score/4) * 100) + "%.")