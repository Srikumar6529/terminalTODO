# ANSI Color Constants
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
GRAY = "\033[90m"

def list_todos(todos):
    if not todos:
        # Stark, clean notification
        print(f"\n--- No tasks found. You're caught up! ---\n")
        return
    
    # Simple, non-emoji hacker style header
    print(f"\n{BOLD}{CYAN}--- TODO LIST ---{RESET}")
    
    for item in todos:
        if item["done"]:
            # Option 1 Matrix style: Dimmed out entirely to gray when completed
            status = "[X]"
            print(f" {item['id']:-2d}. {GRAY}{status} {item['content']}{RESET}")
        else:
            # Option 3 Stealth style: High-contrast, standard text weight for active items
            status = "[ ]"
            print(f" {item['id']:-2d}. {status} {BOLD}{item['content']}{RESET}")
            
    print(f"{CYAN}-----------------{RESET}\n")

def add_todo(todos, content):
    max_id = 0
    for item in todos:
        curr_id = item["id"]
        max_id = max(curr_id, max_id)
    new_item = {"id": max_id + 1, "content": content, "done": False}
    todos.append(new_item)
    return todos

def delete_todo(todos, id):
    new_todos = [item for item in todos if item["id"] != id]
    if len(new_todos) == len(todos):
        # Destructive/Failure errors pop out in stark red alert text
        print(f"{RED}Error: TODO with id {id} not found.{RESET}")
    else:
        print(f"{RED}Deleted TODO successfully.{RESET}")
        for i, item in enumerate(new_todos):
            item["id"] = i + 1
    return new_todos

def update_todo(todos, id, content):
    flag = False
    for item in todos:
        if item["id"] == id:
            flag = True
            item["content"] = content
            break
    if not flag:
        print(f"{RED}Error: TODO with id {id} not found.{RESET}")
    else:
        # Mild confirmation without flooding your screen with heavy color
        print("Updated TODO")
    return todos

def toggle_checkbox(todos, id):
    flag = False
    for item in todos:
        if item["id"] == id:
            flag = True
            item["done"] = not item["done"]
            break
    if not flag:
        print(f"{RED}Error: TODO with id {id} not found.{RESET}")
    else:
        print("Toggled status successfully")
    return todos
