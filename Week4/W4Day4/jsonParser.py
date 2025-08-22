import json

data = {
    "name":"jay",
    "age":22,
    "skills":["python","Java"]
}

def write_json():

    with open('sample1.json','w') as f:
        json.dump(data,f,indent=4)
    print("json created")

def read_json():
    
    with open('sample1.json','r') as file:
        data = json.load(file)
        
    print("Read Operation:")
    print(data)
    
write_json()
read_json()

def update_json():
    with open('sample1.json','r') as file:
        data = json.load(file)
    
    data["hobby"]="chess"
    data["skills"].append('C++')
    
    with open('sample1.json','w') as f:
        json.dump(data,f,indent=4)
        
def delete_field_json():
    with open('sample1.json','r') as file:
        json.load(file)
    
    if "age" in data:
        del data["age"]
        
    with open ('sample1.json','w') as file:
        json.dump(data,file,indent= 4)
        
    print("Age field Delted")
    
    
update_json()
read_json()
delete_field_json()
read_json()