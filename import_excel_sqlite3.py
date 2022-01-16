import csv
import sqlite3

# import csv and extract data
with open('expenses-2022.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    expenses_info = [(i['Date'], i['Expense name/item'], i['Category'], i['Expense'], i['Total']) for i in dr]
    print(expenses_info)

# connect to sqlite
sqlite_connection = sqlite3.connect('expense.db')
cursor = sqlite_connection.cursor()

# create expense table
cursor.execute('create table expenses(Date varchar(10), Expense_name varchar(50), Category varchar(20), Expense int, Total int)')

# # insert data into table
cursor.executemany("insert into expenses(Date, Expense_name, Category, Expense, Total) VALUES (?, ?, ?, ?, ?);", expenses_info)

# show expenses table
cursor.execute('select * from expenses;')

# view results
result = cursor.fetchall()
print(result)