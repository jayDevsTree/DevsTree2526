info = {
    'name': "jay",
    'age': 19,
    'gender': 'male',
    'height': 7,
    'CGPA': 9.7 
}

print("Using Square Brackets:",info['age'])
print("Using Get method:",info.get('age'))

print("Keys:",info.keys())
print('Values:',info.values())
print('Items(key,value):',info.items())

info['DOB'] = 2003 #add field

info["DOB"] = 2005# normal updating values on existing keys
info.update({"DOB": 2006})# update using Update method
print(info)

info.pop('DOB')
# print(info)

# del info['age']#remove field
# info.clear()

info.popitem()#remove last item
print(info)

# info.clear()#remove all items


personalInfo = info.copy()
# personalInfo = dict(info)
print("Copy of Dictionary:",personalInfo)

for key,value in info.items():
    print(f'{key} : {value} ')
    
