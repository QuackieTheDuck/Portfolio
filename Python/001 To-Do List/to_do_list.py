# I think about modyfing how and when the list is saved
# for example to give user ability to name file and load after
# user demand without automatically loading at start
# however for now I'm satisfied with this program so I've decides to
# now to the next project


# need to add checking if lista exist otherwise the program crashes

import os
import json

def print_to_do_list(lista):
    print(f"{"To-Do List":^67}")
    print("="*67)
    print("Status | Number |",f"{"Task":^50}")
    print("="*67)
    if len(lista):
        for i in range(0, len(lista)):
            tmp=lista[i]
            print(f"{tmp["status"]:^6}","|", f"{(i+1):^6}","|", f"{tmp["task"]:^50}")
    else: print(f"{"No tasks":^67}")
    print("="*67)

def menu():                                             # Displays menu and
                                                        # gets the number of action
    print("0. Show/Hide List\n1. Add a new task \n2. Mark task as done\n3. Remove task\n4. Mark task as undone\n5. Exit")
    return(int(input("What would you like to do? ")))

def action_on_list(action, lista):                          # Actions on list
    match action:
        case 0:                                                             # case 0 ready and tested
            global show_list
            if show_list:
                show_list=0
            else:
                show_list=1
            return
        case 1:                                                                 # Case 1 ready and tested
            description=input("Name your new task(50 characters max): ")
            confirmation=input(f"Adding: {description}. Is this correct? (y/n) ")
            if confirmation.lower()=='y':
                lista.append({'status':'X','task':description})
            else:
                return
        case 2:
            completed=int(input("Which task would you like to mark as done? "))       # Case 2 ready and tested
            confirmation=input("Are you sure? (y/n) ")                                
            if confirmation.lower() == "y":
                tmp=lista[completed-1]
                tmp['status']=chr(0x0001F5F8)
        case 3:                                                                 # Case 3 ready and tested
            removed=int(input("Which task would you like to remove? "))         # wszystko dziala poprawnie
            confirmation=input("Are you sure? (y/n) ")
            if confirmation.lower() == "y":
                lista.pop(removed-1)
            else:
                return
        case 4:
            uncompleted=int(input("Which task would you like to mark as undone? "))     # Case 2 ready and tested
            confirmation=input("Are you sure? (y/n) ")                                  
            if confirmation.lower() == "y":
                tmp=lista[uncompleted-1]
                tmp['status']="X"
            else:
                return
        case 5:                                             # Case 4 ready and tested
            confirmation=input("Are you sure? (y/n) ")     
            if confirmation.lower() == "y":
                saving_list(lista)
                exit()
            else:
                return
        case _:
            pass

def saving_list(lista):
    with open("list.json","w") as l:
        json_list={"tasks":lista}
        l.write(json.JSONEncoder().encode(json_list))

def loading_list():                                 # Loading list completed
    with open("list.json","r") as l:
        lista=json.load(l)
    return(lista['tasks'])

def file_checking(lista):
    if os.path.isfile("list.json"):
        lista=loading_list()
    else:
        with open("list.json","w") as l:
            json_list={"tasks":[]}
            l.write(json.JSONEncoder().encode(json_list))
        lista=loading_list()

lista=[]
file_checking(lista)
show_list=1
os.system('title To-Do List')
while True:
    os.system('cls')                # Resreshes the terminal
    if show_list:
        print_to_do_list(lista)     # Prints out the list
    action_on_list(menu(),lista)    # Perform actions on list