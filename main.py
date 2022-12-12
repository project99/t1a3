from os import system
from supporting_fx import master_list, print_master_list, print_pt_meds, add_pt, remove_pt, add_med, remove_med

og_list = master_list

def print_options():
    print("1. Show list of patients and their meds")
    print("2. Show meds of specific patients")
    print("3. Add patient")
    print("4. Remove patient")
    print("5. Add med to a specific patient")
    print("6. Remove med from a specific patient")
    print("0. Exit")
    opt = input("Select your option: ")
    return opt

def print_pt_meds_fx():
    lu_pt = input ("Whose meds would you like to look up? ")
    print_pt_meds(og_list, lu_pt)


def add_pt_fx():
    add_name = input("What's the name of the patient you would like to add? ")
    add_meds = list(input ("Meds would you like to add: ").split())

    add_pt(og_list, add_name, add_meds)
    print(f"{add_name} has been added to the patient list")


def remove_pt_fx():
    print_master_list(og_list)
    name = input("Which patient would you like to remove: ")
    remove_pt(og_list, name)
  

def add_med_fx():
    print_master_list(og_list)
    name = input("Which patient would like to add meds to: ")
    add_med(og_list, name)


def remove_med_fx():
    print_master_list(og_list)
    pt = input ("Whose meds you want to remove? ")
    remove_med(og_list, pt)

option = ""

while option != "0":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        print("Here is a list of patients and their meds")
        print_pt_meds_fx(og_list)
    elif option == "2":
        print("Here is the meds of a specific patient")
        print_pt_meds_fx()
    elif option == "3":
        print("Adds a patient and their meds")
        add_pt_fx()
    elif option == "4":
        print("Removes a patient and their meds")
        remove_pt_fx()
    elif option == "5":
        print("Adds meds to a specific patient")
        add_med_fx()
    elif option == "6":
        print("Removes meds to a specific patient")
        remove_med_fx()
    elif option == "0":
        continue
    else:
        print("Invalid option")  
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 
