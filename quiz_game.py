print("Welcome to my League Of Legends Quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Who is the hardest ADC? ")
if answer == "Aphelios":
    print("Correct!")