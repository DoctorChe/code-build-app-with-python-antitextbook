import sys
import sqlite3

args = sys.argv

#tasks = []

#Подключение к базе
conn = sqlite3.connect("tasks.db")
#Создание курсора
c = conn.cursor()
#Создание таблицы
c.execute('''CREATE TABLE IF NOT EXISTS tasks 
          (id INTEGER PRIMARY KEY NOT NULL, 
          title varchar, 
          content varchar)''')

try:
	command = args[1]
except IndexError:
	print("Invalid arguments!")
	sys.exit(1)

if command not in ("add","remove","list"):
    print("Invalid command\n Use add/remove/list")
    sys.exit(1)


if command == "add":
#    title = args[2]
#    content = args[3]
#    task = title + "|" + content
#    file = open("tasks.txt", "a")
#    file.write(task+"\n")
#    file.close()
#    print("Задача добавлена\n")
    
    #Функция занесения задачи в базу
    def add_task(title, content):
        c.execute("INSERT INTO tasks (title, content) VALUES ('%s','%s')"%(title, content))
        conn.commit()
    
    #Вводим данные
    title = input("Введите название задачи\n")
    content = input("Введите содержание задачи\n")
    add_task(title, content)
    print('Задача добавлена\n\n')

elif command == "remove":
#    try:
#        file = open("tasks.txt", "r")
#    except IOError as e:
#        print(str(e))
#        sys.exit(1)
#    tasks = file.readlines()
#    tasks = [task.strip() for task in tasks]
#    task_id = args[2]
#    del tasks[int(task_id)]
#    
#    file = open("tasks.txt", "w")
#    tasks = [task + "\n" for task in tasks]
#    file.writelines(tasks)
#    print("Задача удалена")
    
    #Функция удаления задачи из базы
    def remove_task(index):
#        c.execute("DELETE FROM tasks WHERE id = ('%s')"%(str(index)))
        print("I just deleted", c.execute("DELETE FROM tasks WHERE id = ('%s')"%(str(index))).rowcount, "rows")
        conn.commit()

    #Вводим данные
    index = input("Введите номер задачи\n")
    if c.execute("SELECT * FROM tasks WHERE id = ('%s')"%(str(index))).rowcount > 0:
        remove_task(index)
        print('Задача удалена\n\n')
    else:
        print("Задача с таким номером не найдена\n\n")
#    remove_task(index)

elif command == "list": 
#    try:
#        file = open("tasks.txt", "r")
#    except IOError as e:
#        print(str(e))
#        sys.exit(1)
#    tasks = file.readlines()
#    if len(tasks) == 0:
#        print("there are no tasks!")
#    else:
#        print("|-{0}----{1}----{2}----|".format("index", "title", "content"))
#        tasks = [task.strip() for task in tasks]
#        for i in range(len(tasks)):
#            title, content = tasks[i].split('|')
#            print("|-{0}--{1}----{2}-|".format(i, title, content))
#    file.close()
    
    #Делаем запрос в базу
    print("Список задач:\n")
#    c.execute('SELECT * FROM tasks')
#    row = c.fetchone()
    
    print("|-{0}--{1}------{2}-----|".format("№","Задача", "Содержание"))
#    #выводим список пользователей в цикле
#    while row is not None:
##        print("Номер:"+str(row[0])+" Задача: "+row[1]+" | Содержание: "+row[2])
#        print("|-{0}--{1}----{2}-|".format(str(row[0]), row[1], row[2]))
#        row = c.fetchone()
    # Print the table contents
    for row in c.execute("SELECT * FROM tasks"):
        print("|-{0}--{1}----{2}-|".format(str(row[0]), row[1], row[2]))

else:
    print("invalid command!")

# закрываем соединение с базой
c.close()
conn.close()
