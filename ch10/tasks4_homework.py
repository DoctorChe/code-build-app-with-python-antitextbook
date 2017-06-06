import sqlite3

#def connect_db():
#    #Подключение к базе
#    conn = sqlite3.connect("tasks.db")
#    #Создание курсора
#    c = conn.cursor()
#    return conn, c    

#Функция занесения задачи в базу
def add_task(title, content, c, conn):
    try:    
#        conn, c = connect_db()
#        c.execute("INSERT INTO tasks (title, content) VALUES ('%s','%s')"%(title, content))
        c.execute("INSERT INTO tasks (title, content) VALUES (?, ?)", (title, content))
        print(type((title, content)))
    except sqlite3.Error:
        if conn:
            print("Error! Rolling back")
            conn.rollback()
    finally:
        if conn:
            conn.commit()
            print('Задача добавлена\n\n')
        
#Функция удаления задачи из базы
def remove_task(task_id, c, conn):
    try:
    #    conn, c = connect_db()
        
    #    if c.execute("SELECT * FROM tasks WHERE id = ('%s')"%(str(task_id))).rowcount > 0:
    #        c.execute("DELETE FROM tasks WHERE id = ('%s')"%(str(task_id)))
    #        print('Задача удалена\n\n')
    #    else:
    #        print("Задача с таким номером не найдена\n\n")
    
        c.execute("DELETE FROM tasks WHERE id = ?", (str(task_id), ))
    #    print("I just deleted", c.execute("DELETE FROM tasks WHERE id = ('%s')"%(str(index))).rowcount, "rows")
    except sqlite3.Error:
        if conn:
            print("Error! Rolling back")
            conn.rollback
    finally:
        if conn:
            conn.commit()
            print('Задача удалена\n\n')

#Функция удаления задачи из базы
def list_task(c, conn):
#    conn, c = connect_db()
    
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

#print(__name__)

if __name__ == "__main__":
    print("this is some print statement")