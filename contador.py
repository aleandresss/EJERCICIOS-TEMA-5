import sys 

f = open ("contador.txt","a+")
f.seek(0)
str = f.read()
if str =="":
    str="0"
try: 
    c=n