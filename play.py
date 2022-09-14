score = 0
userval = input("Do you want to play a game?")
if userval == "no":
    quit()

userval=input("What number between 1-5 am I thinking of: ")
if userval == "1":
    print("wrong")   
elif userval == "2":
    print("wrong")
elif userval == "3":
    print("wrong")
elif userval == "4":
    print("correct")
    score+=1
elif userval == "5":
    print("wrong")
else:
    quit()

    
userval=input("What number between 1-5 am I thinking of: ")
if userval == "1":
    print("wrong")   
elif userval == "2":
    print("wrong")
elif userval == "3":
    print("correct")
    score+=1
elif userval == "4":
    print("wrong")
elif userval == "5":
    print("wrong")
else:
    quit()

userval=input("What number between 1-5 am I thinking of: ")
if userval == "1":
    print("correct")
    score+=1   
elif userval == "2":
    print("wrong")
elif userval == "3":
    print("wrong")
elif userval == "4":
    print("wrong")
elif userval == "5":
    print("wrong")
else:
    quit()

print("your score is: {}".format(score) )
quit()