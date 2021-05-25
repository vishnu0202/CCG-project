print("welcome player")
start=1
pl_score=0
cmp_score=0
while start==1:
    a=0
    while a==0:
        print("enter a valid number with colour listed below \norange=1\nblue=2\nred=3\ngreen=4\nyellow=5\nviolet=6")
        choice=int(input("\n............player enter your choice........"))
        if choice==1:
            print("your colour is yellow and value is 1")
            a=1 
        elif choice==2:
            print("your colour is orange and value is 2")
            a=1
        elif choice==3:
            print("your colour is blue and value is 3")
            a=1
        elif choice==4:
            print("your colour is red and value is 4") 
            a=1
        elif choice==5:
            print("your colour is green and value is 5")
            a=1
        elif choice==6:
            print("your colour is violet and value is 6")
            a=1
        else:
            print(".........enter a valid number between the given limit...........")
            a=0

    import random
    cmp=random.randint(1,6)
    if cmp==1:
        print("computer choice is orange point is 1")
    elif cmp==2:
        print("computer choice is blue point is 2")
    elif cmp==3:
        print("computer choice is red point is 3")
    elif cmp==4:
        print("computer choice is green point is 4")
    elif cmp==5:
        print("computer choice is yellow point is 5")
    elif cmp==6:
        print("computer choice is violet point is 6")
    else:
        pass
    if cmp==choice:
        pl_score=pl_score+1
        print("player score:",pl_score)
        print("computer score:",cmp_score)
    else:    
        cmp_score=cmp_score+1
        print("player score:",pl_score)
        print("computer score:",cmp_score)
    
    c=0
    while c==0:
        decide=input("do you want to continue game Y/N..")
        one=decide.upper()
        if one=="Y":
            start=1
            c=1
        elif one=="N":
            start=0
            c=1
        else:
            print(".............enter a valid option..............")
            c=0
if pl_score>cmp_score:
    print("=====>player  win<========")
    print("====>computer defeated<====")
elif pl_score==cmp_score:
    print("game tied")
else:
    print("=====>computer  win<========")
    print("======>player defeated<======")
print("Thank you for playing")
