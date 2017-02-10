#! /usr/bin/env python3

main_list = []

def main():
    print("This is the main function!")
    while True:
        user_num = input("Enter number to add to list: ")
        if user_num:
            main_list.append(int(user_num))
            print(main_list)
        else:
            print("You entered nothing, the final list is...")
            print(main_list)
            break
    bubblesort(main_list)

def secondary():
    print("This is the secondary function!")

def bubblesort(in_list):
    print("Running bubble sort on " + str(in_list))
    for i in range(len(in_list),1,-1):
        swapped = False
        print("Pass number {0}".format(len(in_list)-i))
        for j in range(1,i):
            print("  Comparing list[{0}] and list[{1}]".format(j-1,j))
            if in_list[j-1] > in_list[j]:
                swap(in_list,j-1)
                print("    SWAP! " + str(in_list))
                swapped = True
            else:
                print("    " + str(in_list))
        if not swapped:
            break
    print("The sorted list is..." + str(in_list))

def swap(in_list,index):
    temp_element = in_list[index+1]
    in_list[index+1] = in_list[index]
    in_list[index] = temp_element

if __name__ == "__main__":
    main()
