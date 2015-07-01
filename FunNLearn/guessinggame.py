#Guessing game
print "Please think of a number between 0 and 100!"
low = 0
high = 100
secretNumber =(low+high)/2
while True:
    print("Is your secret number " + str(secretNumber) + "?")
    userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(userInput == 'l'):
        low = secretNumber
        high = high
        secretNumber =(low+high)/2
    elif(userInput == 'h'):
        low = low
        high = secretNumber
        secretNumber =(low+high)/2
    elif(userInput == 'c'):
        print "Game over. Your secret number was: "+str(secretNumber)
        break
    else:
        print "Sorry, I did not understand your input."
        
  
    