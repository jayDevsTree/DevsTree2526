# args --> return Tuple arguments
# kwargs --> return Dict arguments

def defaultParameters():
    def myfun_name(name = 'Jay'):
        print("Default :", end='')
        print("Hello",name)
    myfun_name()
    myfun_name('Manthan')
    

def argumentfunctions():
    
    def myfun_name(*names):# *args
        print("Args1 :", end='')
        for i in names:
            print(i, end = ', ')
        print()
        
    myfun_name('jay','veer','Dhawnit','het','nilanshu','devarsh')

    def myfun_num(*nums):# *args
        print("Args2 :", end='')
        for i in nums:
            print(i , end = ' ')
        print()
        
    myfun_num(1,2,3,4,5)

    def myfun_list(*element):
        print("Args3 :", end='')
        for i in element:
            print(i , end = ', ')
        print()
        
    l1 = [1,'jay',9.88,bool, True,[1,2,3],None,(1,2,3),{'devarsh':1,'jay':2}]

    myfun_list(*l1)# list take as argument
    

def keywordArgumentfunctions():
    
    def myfun_name(**names):# **kwargs
        print("kwargs1 :", end='')
        for i in names:
            print(i, end = ', ')# print i ans a (key:value) in key value 
        print()
        
    myfun_name(name1 = 'jay',name2 = 'veer',name3 = 'Dhawnit',name4 = 'het',name5 = 'nilanshu',name6 = 'devarsh')
    
    def myfun_name_dict(**names):# **kwargs
        print("kwargs1 :", end='')
        for i,v in names.items():
            print(i,v ,end = ', ')# print i ans a (key:value) in key value 
        print()
        
    myfun_name_dict(name1 = 'jay',name2 = 'veer',name3 = 'Dhawnit',name4 = 'het',name5 = 'nilanshu',name6 = 'devarsh')# pass normal value of key value format
    myfun_name_dict(**{'name1': 'jay','name2': 'veer','name3': 'Dhawnit','name4': 'het','name5': 'nilanshu','name6': 'devarsh'}) # pass as a dictonary
    
    def myfun_kname(**names):
        print("kwargs2 :", end='')
        for i,v in names.items():
            print(i,":",v , end = ', ')
    myfun_kname(name1 = 'jay',name2 = 'veer',name3 = 'Dhawnit',name4 = 'het',name5 = 'nilanshu',name6 = 'devarsh') 
    print()
    
    def myfun_topics(**topics): 
        print("kwargs3 :", end='')
        print(f'name = {topics['name']}, topic = {topics['topic']} , field = {topics['field']}.')# pass as a dictonary key name
            
    myfun_topics(name='Jay', topic='Python', field = 'Data Science')
    myfun_topics(name='Dhruv', topic='Data Science', field = 'Data cleaning')
    
    
defaultParameters()
argumentfunctions()
keywordArgumentfunctions()