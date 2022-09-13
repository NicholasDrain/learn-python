userval=input("Do you want to play a game?")
if userval == "yes":
    print("you want to play a game")
    userval=input("What number between 1-5 am I thinking of")
    
if userval == "1":
    print("wrong")
    userval=input("Do you want to play again?")
    
    
elif userval == "2":
    print("wrong")
elif userval == "3":
    print("wrong")
elif userval == "4":
    print("correct")
    print("you won!")
elif userval == "5":
    print("wrong")
    

else:
    quit()

    

