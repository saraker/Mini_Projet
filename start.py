import json
import os

OUR_HOMEWORK_FILE = 'To_Do_List.json'


def load_tasks():
    if os.path.exists(OUR_HOMEWORK_FILE):
        with open(OUR_HOMEWORK_FILE, 'r', encoding='utf-8') as file:
            try:
                all_tasks = json.load(file)
            except json.JSONDecodeError:
                all_tasks = []
    else:
        all_tasks = []
    return all_tasks


def save_tasks(all_tasks):
    with open(OUR_HOMEWORK_FILE, 'w', encoding='utf-8') as file:
        json.dump(all_tasks, file, indent=4, ensure_ascii=False)


def add(all_tasks, task):
    all_tasks.append(task)
    save_tasks(all_tasks)
    print("\n" + "*" * 50)
    print("    The task is added perfectly...")
    print("*" * 50)


def aff_tasks(all_tasks):
    if not all_tasks:
        print("\n[!] Your list of tasks is empty.")
        print("\n" + "!" * 50)
        print("   Your list of tasks is empty. Add something!  ")
        print("!" * 50)
    else:
        print("\n--- YOUR HOMEWORK LIST ---")
        header = "╔════╤══════════════════════════════════════════╤════════════╗"
        titles = "║ ID │            TASK DESCRIPTION              │   STATUS   ║"
        sep = "╠════╪══════════════════════════════════════════╪════════════╣"
        print(header)
        print(titles)
        print(sep)
        for i, task in enumerate(all_tasks, start=1):
            status = "Finished" if task['done'] else "Pending"
            title_fixed = task['title'].ljust(40)
            status_fixed = status.ljust(10)
            print(f"║ {i:<2} │ {title_fixed} │ {status_fixed} ║")
        print("╚════╧══════════════════════════════════════════╧════════════╝")


def make_done(all_tasks):
    aff_tasks(all_tasks)
    if not all_tasks:
        return
    try:
        index = int(input("\nWhich task is done (enter the index): ")) - 1
        if 0 <= index < len(all_tasks):
            if not all_tasks[index]['done']:
                all_tasks[index]['done'] = True
                save_tasks(all_tasks)
                print("\n" + "*" * 50)
                print("    Task marked as done!!  ")
                print("*" * 50)
            else:
                print("\n" + "*" * 50)
                print("    Task already done!!  ")
                print("*" * 50)
                aff_tasks(all_tasks)
        else:
            print("\n" + "*" * 50)
            print("    Invalid task number.  ")
            print("*" * 50)
    except ValueError:
        print("\n" + "*" * 50)
        print("    Please enter a valid number.  ")
        print("*" * 50)


def list_choices():
    all_tasks = load_tasks()
    while True:
        width = 55
        top_border = "╔" + "═" * (width - 2) + "╗"
        bottom_border = "╚" + "═" * (width - 2) + "╝"
        middle_line = "║" + " " * (width - 2) + "║"
        print(top_border)
        print(f"║{'   What would you like to do?'.center(width - 2)}║")
        print("╠" + "═" * (width - 2) + "╣")
        print(middle_line)
        print("║    1.   Add new task.                               ║")
        print("║    2.   View all tasks.                             ║")
        print("║    3.   Mark task as done.                          ║")
        print("║    4.   Exit.                                       ║")
        print(middle_line)
        print(bottom_border)
        choice = input("\nOperation number: ")
        if choice == '1':
            title = input("\nGive the name of the new task: ")
            task = {"title": title, "done": False}
            add(all_tasks, task)
        elif choice == '2':
            print("\nThis is your to do list: ")
            aff_tasks(all_tasks)
        elif choice == '3':
            make_done(all_tasks)
        elif choice == '4':
            print("\n" + "*" * 50)
            print("    Goodbye! Keeping up the hard work.")
            print("*" * 50)
            break
        else:
            print("\n" + "*" * 50)
            print("    Invalid choice, try again.")
            print("*" * 50)


if __name__ == "__main__":
    list_choices()