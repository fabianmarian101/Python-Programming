# f=open("data.txt","r")

# print("The position of the cursor is",f.tell())

# f.seek(10)

# print(f.read())
# f.close()

# f=open("data.txt","r")


# print(f.readlines())
# f.seek(0)
# for x in f.readlines():
#     print(x)

run =True
#_____________________________________________________________________________________________________
def exit_bank():
    global run
    run=False
#_____________________________________________________________________________________________________
def create_account():
   #getting information from user
    username = input("Enter a username  ")
    password = input("Enter a password  ")
    #storing this information in a file

    
    f = open("data.txt","a")
    f.write(username+","+password+","+ username+".txt \n")
    f.close()
    amount = open(username+".txt","w")
    amount.write("0")
    amount.close()
    print("\n Great !!! your account has been created \n") 


#_____________________________________________________________________________________________________
def check_balance():
       #getting information from user
     username = input("Enter a username ")
     password = input("Enter a password ")

     f = open("data.txt","r")
    
     for line in f.readlines():

        list_data = line.split(",")
        
        if username==list_data[0] and password==list_data[1] :

            print("Welcome user",username+"\n\n")

            amount = open(list_data[-1].replace(" \n",""),"r")

            print("Your balance is ",float(amount.read()))

            amount.close()

            print("\n\n Please do visit us again\n\n")

        # else:
        #     print("Sorry we donot have your information please retry!!!\n\n")
#_____________________________________________________________________________________________________
def credit() : #Funtion to credit amount to your bank account

    username = input("Enter your Username ") # Accepts username
    password = input("Enter your paasword ") #Accepts password

    f = open('data.txt',"r")

    for line in f.readlines():

        list_users = line.split(",")

        if username==list_users[0] and password==list_users[1] :

            f.close()

            amount_from_user = float(input("Enter the amount to credit ")) 

            amount = open(list_users[-1].replace(" \n",""),"r+")

            old_amount = float(amount.read()) # reading the old amount

            new_amount = old_amount + amount_from_user

            amount.write(str(new_amount))
            
            amount.close()

            print("Your Account has been credited with",str(amount_from_user)+"$","your balance is",str(new_amount))


def debit():

    username = input("Enter your Username ") # Accepts username
    password = input("Enter your paasword ") #Accepts password

    f = open('data.txt',"r")

    for line in f.readlines():

        list_users = line.split(",")

        if username==list_users[0] and password==list_users[1] :

            f.close()

            amount_from_user = float(input("Enter the amount to debit ")) 

            amount = open(list_users[-1].replace(" \n",""),"r+")

            old_amount = float(amount.read()) # reading the old amount

            new_amount = old_amount - amount_from_user

            amount.write(str(new_amount))
            
            amount.close()

            print("Your Account has been debited with",str(amount_from_user)+"$","your balance is",str(new_amount))






while run:

    print("Welcome to Wells Fargo")
    print("Please choose any one option")
    print("1: Credit Amount")
    print("2: Debit Amount")
    print("3: Check Balance")
    print("4: Create a new account")
    print("5: Exit")

    option=int(input("Enter your option "))

    print("the option is ",option ,"\n")

    if option==5:
        exit_bank()

    elif option==4:
        create_account()

    elif option==3:
        check_balance()

    elif option == 1 : #option to credit amount
        credit()




