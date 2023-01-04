import sys 

f = open ("contador.txt","a+")
f.seek(0)
str = f.read()
if str =="":
    str="0"
try: 
    contador =int(str)
    if len(sys.argv)[1]=="inc":
        contador + = 1
    
    elif sys.argv[1] == "dec":
        contador - = 1
    
