from insert import *
from update import *
from delete import *
from select import *


def print_menu():
    print('1. Show Customers')
    print('2. Add a Customer')
    print('3. Remove a Customer')
    print('4. Update a Customer')
    print('5. Quit')
    print('press any key to show menu')
    print()


def insertcustomer():
    print("Add Customer : ")
    customername = input("FirstName: ")
    customerfamily = input("LastName: ")
    nationalcode = input("NationalCode: ")
    insert(customername, customerfamily, nationalcode)


def selectcustomer():
    print("Customers are : ")
    select()


def updatecustomer():
    print("Update Customer : ")
    nationalcode = input("NationalCode: ")
    customername = input("Enter New Name : ")
    update(nationalcode, customername)


def deletecustomer():
    print("Delete Customer : ")
    nationalcode = input("Enter Customer NationalCode: ")
    delete(nationalcode)


menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = input("Type in a number (1-5): ")

    if menu_choice == "1":
        selectcustomer()

    elif menu_choice == "2":
        insertcustomer()

    elif menu_choice == "3":
        deletecustomer()

    elif menu_choice == "4":
        updatecustomer()

    elif menu_choice == "5":
        break

    else:
        print_menu()
