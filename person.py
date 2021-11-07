person1 = {'name': 'Sambhaji', 'age': 40}
person2 = {'name': 'Sadhana', 'age': 31}
person3 = {'name': 'Satyam', 'age': 12}
person4 = {'name': 'Aaradhya', 'age': 5}


mini_database = [
    person1,
    person2,
    person3,
    person4
]


for person in list(mini_database):
    if 'Satyam' in person.values():
        print('Satyam is here')
