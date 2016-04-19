#!/usr/bin/python3



while True:
    user_first_option = int(input("Please pick from this first tier of options: 1. Option One 2. Option Two 3. Option Three 4. Option Four "))
    
    try:
        if user_first_option == 1:
            print("This is option 1")
        elif user_first_option == 2:
            print("This is option 2")
        elif user_first_option == 3: 
            print("This is option 3")
        elif user_first_option == 4:
            print("This is option 4")
    except:
        ("Invalid Input. Please press 1, 2, 3, or 4.")
        break
    
    