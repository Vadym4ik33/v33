import sqlite3
import tkinter as tk
from tkinter import ttk

# Создаем подключение к базе данных
conn = sqlite3.connect('employees.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу 'employees' с указанными атрибутами
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone TEXT,
                    email TEXT,
                    salary REAL
                )''')

# Функция для добавления сотрудника в базу данных
def add_employee(name, phone, email, salary):
    cursor.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)", (name, phone, email, salary))
    conn.commit()

# Функция для отображения всех сотрудников в виджете Treeview
def display_employees():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Создание графического интерфейса
root = tk.Tk()
root.title("Список сотрудников компании")

# Создание виджетов
tree = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Salary"), show="headings")
tree.heading("Name", text="ФИО")
tree.heading("Phone", text="Телефон")
tree.heading("Email", text="Email")
tree.heading("Salary", text="Заработная плата")

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
salary_entry = tk.Entry(root)
add_button = tk.Button(root, text="Добавить сотрудника", command=add_employee)

display_employees()

# Размещение виджетов на форме
tree.pack()
name_entry.pack()
phone_entry.pack()
email_entry.pack()
salary_entry.pack()
add_button.pack()

# Закрытие подключения к базе данных
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Запуск приложения
root.mainloop()