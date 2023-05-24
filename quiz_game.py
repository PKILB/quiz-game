print("Welcome to my League Of Legends Quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Who is the hardest ADC? ")
if answer == "Aphelios":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the most cringe Top Laner? ")
if answer == "Teemo":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the coolest Mid Laner? ")
if answer == "Sylas":
    print("Correct!")
else:
    print("Incorrect......")

answer = input("Who is the scariest Jungler? ")
if answer == "Eveylnn":
    print("Correct!")
else:
    print("Incorrect......")