
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':

            todo = input("enter a todo:") + "\n"

            with open("todolist.txt", "r") as file:
                todos = file.readlines()
                todos.append(todo)

            with open("todolist.txt", "w") as file:
                file.writelines(todos)
                file.close()

        case 'show':
            with open('todolist.txt', "r") as file:
                todos = file.readlines()
                file.close()

            """new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)"""

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                # for index, item in enumerate(todos):
                # item = item.strip("\n")
                row = f"{index + 1}.{item}"  # f string
                print(row)

        case 'edit':
            with open("todolist.txt", 'r') as file:
                todos = file.readlines()

            number = int(input("Number of todo to edit:"))
            number = number - 1
            existing_todo = todos[number]
            replace_todo = input("Enter todo to replace of :") + '\n'
            todos[number] = replace_todo

            with open("todolist.txt", 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            todo_comp = int(input("Number of todo complete:"))
            with open("todolist.txt", 'r') as file:
                todos = file.readlines()
            index = todo_comp - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            updated_todos = todos

            with open("todolist.txt", 'w') as file:
                file.writelines(updated_todos)
                file.close()
                # for bold text we used print("\033[1m" + "text" + "\033[0m") .
            message = "todos \033[1m"+f"{todo_to_remove}"+"\033[0m was removed from the list"
            print(message)

        case 'exit':
            break

print("Bye!")
