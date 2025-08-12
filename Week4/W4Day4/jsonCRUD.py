import json

file ='sample2.json'
def readJson():
    print("Read Operation:")
    with open(file,'r') as file:
        data = json.load(file)
        
    print(data)

readJson()

def writeJson(file,data):
    with open(file, 'w') as file:
       json.dump(data,file,indent=4)
    print("json write content Updated")
    
def updateJson(file,data):
    with open(file,'r') as f:
        json.load(f)
    
   
        
    
    

       
       