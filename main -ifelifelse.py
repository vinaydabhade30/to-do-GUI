from function_mod import file_open_w, file_open_r

import time

print("today date is " + time.strftime("%Y/%m/%d"))

while True:
    user_action = input("ype add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = file_open_r()

        # with open("todolist-ifelifelse.txt", "r") as file:
        # todos = file.readlines()

        todos.append(todo)

        # with open("todolist-ifelifelse.txt", "w") as file:
        #  file.writelines(todos)
        file_open_w(todos)

    elif user_action.startswith("show"):

        todos = file_open_r()
        # with open('todolist-ifelifelse.txt', "r") as file:
        # todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}.{item}"  # f string
            print(row)

    elif user_action.startswith("edit"):
        try:
            # with open("todolist-ifelifelse.txt", 'r') as file:
            # todos = file.readlines()

            todos = file_open_r()

            # number = int(input("Number of todo to edit:"))
            number = int(user_action[5:])
            number = number - 1
            existing_todo = todos[number]
            replace_todo = input("enter the todo need to change:") + "\n"
            todos[number] = replace_todo

            # with open("todolist-ifelifelse.txt", 'w') as file:
            # todos = file.writelines(todos)

            file_open_w(todos)

        except ValueError or IndexError:
            print("Your command is not valid, after edit enter number")
        continue

    elif user_action.startswith('complete'):
        try:
            todo_comp = int(user_action[9:])
            todos = file_open_r()
            # with open("todolist-ifelifelse.txt", 'r') as file:
            # todos = file.readlines()"""

            index = todo_comp - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            updated_todos = todos

            # with open("todolist-ifelifelse.txt", 'w') as file:
            # file.writelines(updated_todos)

            file_open_w(updated_todos)

                # for bold text we used print("\033[1m" + "text" + "\033[0m") .
            message = "todos \033[1m" + f"{todo_to_remove}" + "\033[0m was removed from the list"
            print(message)
        except IndexError:
            print("enter number out of range")
        continue

    elif user_action.startswith('exit'):
        break
    else:
        print("bad command")

print("Bye!")
