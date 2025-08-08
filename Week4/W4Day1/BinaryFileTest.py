import pickle

# write binary using pickle.dump()
with open ('Week4/W4Day1/BinaryFileTestOutput.txt' ,'wb') as f:
    str = 'hello'
    l1 = [2,3.4,'binary',True]
    dict1 = {'a':1,'b':2,'c':3,'d':4}
    pickle.dump(str,f)
    pickle.dump(l1,f)
    pickle.dump(dict1,f)
# read binary using pickle.load()
with open ('Week4/W4Day1/BinaryFileTestOutput.txt' ,'rb') as f:
    str = pickle.load(f)
    l1 = pickle.load(f)
    dict1 = pickle.load(f)
    print(str)
    print(l1)
    print(dict1)
    
