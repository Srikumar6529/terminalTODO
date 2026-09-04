import os
import json
HOME_DIR = os.path.expanduser("~")
filepath = os.path.join(HOME_DIR, "todos.json")
def get_todos():
    with open(filepath, "r", encoding = "utf-8") as file:
        todo_list = json.load(file)
    return todo_list
def save_todos(todos):
    def sort_on(item):
        return item["id"]
    todos = sorted(todos, key=sort_on)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(todos,file)
