# Corporation Promotion

Salary = {
    'Nick':{
        'Department':'Tech',
        'Salary':3000,
        'Level':1
    },

    'Henry':{
        'Department':'Marketing',
        'Salary':5000,
        'Level':2
    },

    'Lucy':{
        'Department':'Marketing',
        'Salary':7000,
        'Level':2

    },

    'Amelie':{
        'Department':'Tech',
        'Salary':4000,
        'Level':1

    },

    'Jesica':{
        'Department':'Marketing',
        'Salary':6000,
        'Level':2

    }
}

for x in Salary:
    value = Salary[x]
    if value['Level'] == 1:
        value['Level'] += 1
        value['Salary'] += 2000
        Salary[x] = value

print('------------------------Updated Salary------------------------\n')

keys = Salary.keys()
for x in keys:
    print(f'{x}: {Salary[x]}\n')

