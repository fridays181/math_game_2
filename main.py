#inital/base info needed for the game to run
def base():
    #making all the vars global
    global animations
    global total
    global randomTotal
    global bA
    #setting up assets
    animations = ["-", "--", "---", "----"]
    #setting the total to edit to zero everytime the game starts
    total = 0
    #making a random number
    import random
    randomTotal = (random.randint(10,40))
    #making things look fancy var
    bA = "============"

#starting sequence
def starting():
    #calling to first function
    base()
    #intro to the game and rules
    print(bA)
    print("The goal of the game is to make the random number using only 1-4 in 10 rounds, dont get above or below the number assigned")
    print("The number you got this round is :")
    print(randomTotal)
    print("Now type 1,2,3, or 4 to add to youre total")
    print(bA)

#the main controls the user can do
def moving():
    global total
    global movement
    movement = input(": ")
    #if the user types a number add it to the toatal
    if movement == "1":
        print(animations[0])
        total = total + 1
    elif movement == "2":
        print(animations[1])
        total = total + 2
    elif movement == "3":
        print(animations[2])
        total = total + 3
    elif movement == "4":
        print(animations[3])
        total = total + 4
    #if they dont type a acceptable number restart
    else:
        moving()

#what the user will see while playing(more front end stuff)
def mainGame():
    global rounds
    #setting round to 9 since after the first round they wouldve gone through 1 cycle already
    rounds = 9
    #loop
    for i in range(10):
        moving()
        print(bA)
        #general visual stuff for user
        print("Total so far: ")
        print(total)
        print("Rounds left till: ")
        print(rounds)
        print("Number youre trying to make: ")
        print(randomTotal)
        print(bA)
        #suptracking 1 from rounds every loop
        rounds = rounds - 1
    endGame()

#deciding wheather the user won or not
#gegardless it starts the game over
def endGame():
    if total == randomTotal:
        for i in range(5):
            print("You win!")
        spark()
    else:
        print("You lost:(")
        spark()

#the games spark that sets everything in motion
def spark():
    starting()
    mainGame()

#the menu/starting screen
def menu():
    print(".     (===Ethans number game!===)      .")
    print("--==type anything to start the game!==--")
    starterInput = input("Type here: ")
    #an easter egg
    if starterInput == "egg":
        print("Goodjob!")
        spark()
    else:
        spark()

#the thing to start the game
menu()
