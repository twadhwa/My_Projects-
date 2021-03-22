# Program to generate password

# The main part of the code is the random libraray 
import random



def password(a,b):
    
    # Function takes the range of characters and returns the password "
    digits=random.randint(a,b)
    password=""
    for i in range(digits):
        choose=random.randint(0,3)
        alpha_bigger=chr(random.randint(65,91))
        alpha_small=chr(random.randint(97,122))
        numeric=chr(random.randint(48,58))
        special_character=chr(random.choice([64,95]))
        if (choose==0):
            password=password + alpha_bigger

        elif(choose==1):
            password=password + alpha_small

        elif(choose==2):
            password= password + numeric

        else :
            password = password + special_character


    return ( password )

def main ():
    
    # Main function of the program "
    start_length=int(input("Enter the starting number of the range of the password "))
    end_length = int ( input ("Enter the ending number of the range of the password "))
    print("Your password is ")
    print(password(start_length,end_length))

main()
