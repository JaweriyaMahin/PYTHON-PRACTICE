import os

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks=[]
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as f:
            for line in f:
                line=line.strip()
                if line and "|" in line:
                    t,s=line.split("|",1)
                    tasks.append({"title":t,"status":s})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME,"w") as f:
        for task in tasks:
            f.write(f"{task['title']}|{task['status']}\n")

def view(tasks):
    if not tasks:
        print("\nNo tasks.")
        return
    print("\n----- TASKS -----")
    for i,t in enumerate(tasks,1):
        print(f"{i}. {t['title']} [{t['status']}]")

def add(tasks):
    title=input("Task: ").strip()
    if title:
        tasks.append({"title":title,"status":"Pending"})
        save_tasks(tasks)

def delete(tasks):
    view(tasks)
    try:
        n=int(input("Delete task no: "))
        tasks.pop(n-1)
        save_tasks(tasks)
    except:
        print("Invalid input")

def edit(tasks):
    view(tasks)
    try:
        n=int(input("Edit task no: "))
        tasks[n-1]["title"]=input("New title: ").strip()
        save_tasks(tasks)
    except:
        print("Invalid input")

def complete(tasks):
    view(tasks)
    try:
        n=int(input("Complete task no: "))
        tasks[n-1]["status"]="Completed"
        save_tasks(tasks)
    except:
        print("Invalid input")

def search(tasks):
    key=input("Search: ").lower()
    for i,t in enumerate(tasks,1):
        if key in t["title"].lower():
            print(f"{i}. {t['title']} [{t['status']}]")

def main():
    tasks=load_tasks()
    while True:
        print("""
====== TODO APP ======
1.View
2.Add
3.Delete
4.Edit
5.Complete
6.Search
7.Count
8.Exit
======================
""")
        ch=input("Choice: ")
        if ch=="1": view(tasks)
        elif ch=="2": add(tasks)
        elif ch=="3": delete(tasks)
        elif ch=="4": edit(tasks)
        elif ch=="5": complete(tasks)
        elif ch=="6": search(tasks)
        elif ch=="7": print("Total Tasks:",len(tasks))
        elif ch=="8": break
        else: print("Invalid choice")

if __name__=="__main__":
    main()
    