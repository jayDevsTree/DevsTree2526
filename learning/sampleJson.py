import json

data = [{"name":"jay","age":22,"skills":["python","Java"]},{"name":"veer","age":22,"skills":["wordPress","Java"]}]

# with open('sample.json','w') as f:
#     json.dump(data,f,indent=4)
dict_data = {}
    
with open('sample.json','r') as f:
    read_data = json.load(f)
    #convert in dictonary
    for data in read_data:
        dict(data)
        dict_data[data['name']] = data
        
        
    print(read_data[0]['name'] == 'jay')
    # for key,value in read_data.items():
    #     print(key)
    
print(dict_data) 
    
