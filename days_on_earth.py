from datetime import date

now = date.today()
birthday = date(1981, 3, 6);
age = now - birthday
print(age.days)