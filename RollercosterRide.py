print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster! ")
    age = int(input("How old are you ? "))
    if age < 12:
        bill = 5
        print("Child Tickets Are £5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets Are £7.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok!, Have a free ride on us.")
    
    else:
        bill = 12
        print("Adult Tickets Are £12. ")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is £{bill}")
else:
    print("Sorry, Your have to grow a little taller to ride this rollercoster.")