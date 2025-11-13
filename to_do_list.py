to_do_list = []

print("WELCOME TO THE TO-DO LIST APP")
print("*****************************")
print("Options:")
print("1. Add a task")
print("2. View tasks")
print("3. delete tasks")
print("4. EXIT APP")

while True:
    task = int(input("Enter number:"))

    if task == 1:
        add_task = input("Enter the task you want to add:")
        to_do_list.append(add_task)
        print(f'Task "{add_task}" added to the list.')

    elif task == 2:
        if not to_do_list:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(to_do_list, start=1):
                print(f"{idx}. {task}")
        
    elif task == 3:
        if not to_do_list:
            print("Your to-do list is empty. No tasks to delete.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(to_do_list, start=1):
                print(f"{idx}. {task}")
            delete_task = int(input("Enter the number of the task you want to delete:"))
            if 1 <= delete_task <= len(to_do_list):
                removed_task = to_do_list.pop(delete_task - 1)
                print(f'Task "{removed_task}" has been deleted from the list.')
            else:
                print("Invalid task number.")
    elif task == 4:
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
