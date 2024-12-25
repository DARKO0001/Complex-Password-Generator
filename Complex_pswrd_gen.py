#imports

import random

#characters - 

upper_cha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower_cha = 'mnbvcxzlkjhgfdsapoiuytrewq'
numbs = '3719052846'
special = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

#welc -

def welc():
    print("=====Welcome to Complex Password Generator🔒=====")
#take the input and check

def length():
    while True:
        user_input = input("Please enter the length of the password (minimum 8): ")
        try:
            # check
            user_input = int(user_input)
            # Check > 11
            if user_input < 8:
                print("Password length must be at least 8. Please try again.")
                continue
            return user_input
        except:
            # error
            print("Please enter a number! Try again.")

# gen function 

def generate_password(length):
    password_final = ''
    password = [random.choice(upper_cha),random.choice(lower_cha),random.choice(special),random.choice(special),random.choice(numbs)]
    all_characters = upper_cha + lower_cha + numbs + special
    for chr in range(length-5):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return password_final.join(password)

#main 

def main_gen():
    #welcome massage - 
    welc()
    #for print the all passwords with order num and store in 
    counter = 0
    generated_passwords = []  
    #looping the main functions 
    while True:
        password_length = length()
        random_password = generate_password(password_length)
        generated_passwords.append(random_password) 
        print("-----------------------------------------")
        print(f"Generated Password 🔑: {random_password}")
        print("-----------------------------------------")
        
        
        # ask the user want more or not if no print all genreated passwords and exit

        again = input("Do you want to generate another password? (y/n): ").strip().lower()
        if again == 'n':
            print("All passwords 🔒: ")
            for pwd in generated_passwords:
                counter+=1
                print(f'{counter} - Password: {pwd}')
            break

#main start

if __name__ == "__main__":
    main_gen()