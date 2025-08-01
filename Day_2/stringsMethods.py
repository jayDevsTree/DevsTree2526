# string operations
str1 ='hello'
st2 = 'world'
st3 = 'Hello my name is Jay Patil'.split(" ")
print('Hello, "I am learning String Operations".')# writing double quotes one way
print("Hi, \"I'm Learning string operations\".")# writing double quotes one way
print(str1+" "+st2)
print(st3[:])

print(True if st3[0] == st3[-6] else False)

for i in st3:
    print(i)
    
# String methods

st = " Hello my name is Jay Patil"
print ("Upper:",st.upper())
print ("Lower:",st.lower())
print ("Capitalize:",st.capitalize())
print ("Title:",st.title())
print ("Count:",st.count("a"))
print ("Find:",st.find("a"))
print ("Replace:",st.replace("a","A"))
print ("Split:",st.split(" "))
print ("Strip:",st.strip())
print("isAlpha:",st.isalpha())
print("isendswith:",st.endswith("l"))

