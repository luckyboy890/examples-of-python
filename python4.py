'''def multipliction():
    print("multipliction function called32")
    return 5*6

print ("running")
c= multipliction()
print (c)

    

def addition ():
    print ("addition function called")
    return 8+9

print("start")
c=addition()
print (c)

print("=================================")
def multiplication(a,b):
    print("multiplication function called")
    return (a*b)


num1=int(input("enter your number1"))
num2=int(input("enter your number2"))

c=multiplication(num1,num2)
print(c)

print("=========================================")

def suma (name, className, sub, reg):
    print(sub)
    print(name)
    print(className)
    print(reg)
suma(reg=1, sub="english",className="class",name="julli")
suma("julli","english",className="class",reg=1)

print("==============================================")

score=[134,67,99,15,34,102,45]
for s in score:
    if s>100:
        print(f"{s} is invalid")
        print (s)
        break
        
print("==========================================")


malelist=["surya","karthik","abhi","venky"]
femalelist=["kajal","thamanna","rithika",]
pythonlist=malelist+femalelist

pythonlist.append("dinesh")

pythonlist.remove("dinesh")

print (pythonlist)


print("pythonlist={0}". format(pythonlist))

print("========================================")

print("malelist={0}".format(malelist))

print("============================================")

print("femalelist={0}".format(femalelist))


print(malelist[1])
print(femalelist[-1])

print(pythonlist[1:6])



print("=========================================")

movielist=["7thsence","hanuman","jalsa","kgf"]
directorlist=["rajamouli","prashanth nill","thivikram","koratalla shiva"]
fanslist=(movielist+directorlist)

fanslist.append("salar")

print(fanslist)


print("=================================")

print("fanslist={0}".format(fanslist))

print("===================================")

print("movielist={0}".format(movielist))

print("======================================")

print("directorlist={0}".format(directorlist))


# write a programm take three values and print highest value:


num1=30
num2=70
num3=80
if (num1>num2) and (num2<num1):
    print(num1)
elif (num2>num3)and (num3<num2):
    print(num2)
elif (num3>num1) and (num1<num3):
    print(num3)


list=[2,5,6,12,13]

print(f"{ list[4]}  longest number in list")'''


num=int(input("enter your value"))
count=len(str(num))
print(f" number of count {count}")


