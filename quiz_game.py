print("Welcome to my League Of Legends Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Who is the hardest ADC? ")
if answer.lower() == "Aphelios":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the most cringe Top Laner? ")
if answer.lower() == "Teemo":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the coolest Mid Laner? ")
if answer.lower() == "Sylas":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the scariest Jungler? ")
if answer.lower() == "Eveylnn":
    print("Correct!")
else:
    print("Incorrect......")