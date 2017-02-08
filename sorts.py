#! /usr/bin/env python3

main_list = []

def main():
    print("This is the main function!")
    while True:
        user_num = input("Enter number to add to list: ")
        if user_num:
            main_list.append(int(user_num))
            printlist()
        else:
            print("You entered nothing, ending list...")
            break
        
def printlist():
    print(main_list)

def secondary():
    print("This is the secondary function!")

def bubblesort():
    pass

if __name__ == "__main__":
    main()
