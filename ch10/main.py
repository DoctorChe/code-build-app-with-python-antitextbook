# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:19:02 2017

@author: a.likhobabin
"""
import sys
import sqlite3
import tasks4_homework as t

ADD,REMOVE,LIST = "add","remove","list"

def main():
    args = sys.argv
    
#    try:    
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
    
    if command not in (ADD,REMOVE,LIST):
        print("Invalid command\n Use {0}/{1}/{2}".format(ADD,REMOVE,LIST))
        sys.exit(1)
    
    if command == "add":
        title = args[2]
        content = args[3]
#        #Вводим данные
#        title = input("Введите название задачи\n")
#        content = input("Введите содержание задачи\n")
        t.add_task(title, content, c, conn)
    elif command == "remove":
        task_id = args[2]
        #Вводим данные
#        task_id = input("Введите номер задачи\n")
        t.remove_task(task_id, c, conn)
    elif command == "list": 
        t.list_task(c, conn)
    else:
        print("invalid command!")
#    except sqlite3.Error:
#        if conn:
#            print("Error! Rolling back)
#            conn.rollback()
#    finally:
#        if conn:
            # закрываем соединение с базой
    c.close()
    conn.close()

main()
