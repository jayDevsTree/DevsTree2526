import json

file_path ='sample2.json'
def readJson():
    print("Read Operation:")
    with open(file_path,'r') as file:
        data = json.load(file)
        
    print(data)

readJson()

def writeJson(file_path,data):
    with open(file_path, 'w') as file:
       json.dump(data,file,indent=4)
    print("json write content Updated")
    
def updateJson(file_path,data):
    with open(file_path,'r') as f:
        json.load(f)
        
    data["hobby"]="chess"
    data["skills"].append('C++')
    
    with open(file_path,'w') as f:
        json.dump(data,f,indent=4)
    print("json updated")
    
   
        
    
    

       
       