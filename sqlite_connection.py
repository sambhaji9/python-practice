import sqlite3

connection = sqlite3.connect("D:\\softwares\\sqlite-tools-win32-x86-3370200\\student.db")

print(connection)
print(connection.total_changes)