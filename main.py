import random
while True:
    choice=input("Press Enter To Roll the dice")
    number=random.randint(1,6)
    print("Congratulations You Got "+str(number))
    print("Do You Want To Roll Again(y/n)")
    if input().lower()=='n':
        break