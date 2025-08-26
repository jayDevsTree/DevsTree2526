import json

names = ['jay','veer','Dhawnit','het','nilanshu','devarsh','talha','dev','Dhruv','parth']
nums = [1,2,3,4,5,6,7,8,9,0]

# for ele,value in enumerate(names,1):
#     print(f'{ele}:{value}')
    
# data = dict(list(enumerate(names,1)))
# print(data)

data = dict(enumerate(names,start=1))
data2 = dict(list(enumerate(nums,1)))
with open ('Week5/W5Day1/listTojson.json','w') as f:
    json.dump(data2,f)

# with open('Week5/W5Day1/listTojson.json','w') as f:
#     json.dump(names,f)
    
# with open('Week5/W5Day1/listTojson.json','r') as f:
#     data = json.load(f)
#     print(data)


