#!/usr/bin/env python3
import sys
from src.utils import *
from src.todo import *
import subprocess

 
#print("------------------------------TERMINAL TODO------------------------------")
def chk_id(id):
    try:
        id = int(id)
        return id
    except ValueError:
        print(f"{id} is not a valid id. Please try again Properly")
        sys.exit(1)
        
def main():
    if len(sys.argv)<2:
        print("Usage todo command[add|ls|delete|update|toggle] args")
        sys.exit(1)
    command = sys.argv[1]
    if command == "ls":
        list_todos(get_todos())
    elif command == "add":
        if len(sys.argv)!=3:
            print(f"see todo help for proper usage of command {command}")
            sys.exit(1)
        content = sys.argv[2]
        todos = get_todos()
        todos = add_todo(todos,content)
        save_todos(todos)
        print("Added new Todo")
        subprocess.run(["todo","ls"])

    elif command == "delete":
        if len(sys.argv)!=3:
            print(f"see todo help for proper usage of command {command}")
            sys.exit(1)
        id = sys.argv[2]
        id = chk_id(id)
        todos = get_todos()
        todos = delete_todo(todos,id)
        save_todos(todos)
        subprocess.run(["todo","ls"])
 
    elif command == "update":
        if len(sys.argv)!=4:
            print(f"see todo help for proper usage of command {command}")
            sys.exit(1) 
        id = sys.argv[2]
        id = chk_id(id)
        content = sys.argv[3]
        todos = get_todos()
        todos = update_todo(todos,id,content)
        save_todos(todos)
        #print("Updated TODO")
        subprocess.run(["todo","ls"])
 
    elif command == "toggle":
        if len(sys.argv)!=3:
            print(f"see todo help for proper usage of command {command}")
            sys.exit(1)
        id = sys.argv[2]
        id = chk_id(id)
        todos = get_todos()
        todos = toggle_checkbox(todos,id)
        save_todos(todos)
        subprocess.run(["todo","ls"])
 
    elif command == "help":
        print("list of all possible commands and thier usage:")
        print("ls       Usage: <todo ls>                        | Lists all the todo's") 
        print("add      Usage: <todo add \"new todo\">            | adds a new todo")
        print("delete   Usage: <todo delete id>                 | deletes the todo at id")
        print("update   Usage: <todo update id \"new content\">   | updates the todo at id with new content")
        print("toggle   Usage: <todo toggle id>                 | toggles the checkmark for specified todo")
    else:
        print(f"Invalid Command: {command}")
        print("Use <todo help> for list of all possible commands")

if __name__=="__main__":
    main()
