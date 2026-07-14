def show_menu():
    print("=== TO-DO LIST ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Import task to a file")
    print("0. Exit")
    print("")

def add_task():
    print("Adding task...")

def list_tasks():
    print("Listing tasks...")

def remove_task():
    print("Removing task...")

def import_to_file():
    print("Importing task to a file...")

def exit_program():
    print("Exiting program...")

def main():
    show_menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        add_task()
    elif opcao == 2:
        list_tasks()
    elif opcao == 3:
        remove_task()
    elif opcao == 4:
        import_to_file()
    elif opcao == 0:
        exit_program()

main()