import pymysql
import sys

def menu():
    while True:
        print("Please pick an option")
        menu = ('''     
        1 - Login to Chatpal
        2- Exit system
                \n''')
        choice = input(menu)
        if choice == "1":
            login()
        elif choice == "2":
            print("Thank you for using Chatpal")
            sys.exit()
        else:
            print("Unrecognized choice")

def login():
    while True:
            db = pymysql.connect("localhost", "root", "mymapua20", "loginacc")
            print("Please login to use Chatpal")
            email = input("Enter Mapua email: ")
            password = input("Enter password: ")
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM `accounts` WHERE `email` = '"+email+"' AND `password` = '"+password+"'")
            verify = mycursor.fetchall()
            if verify:
                for i in verify:
                    print("Success, Welcome to Chatpal")
                return ("Opening Chatpal")
                break
            else:
                print("Sorry, user not found")
                reply = input("Do you want to try again? y/n: ")
                if reply.lower() == "n":
                    print("Thank you for using our service")
                sys.exit()

menu()