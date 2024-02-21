'''a=5
b=8
print(type(a),type(b))


a=5.77
b=6.9999
c=32
print(type(a),type(b),type(c))'''



def multiplicationtable(a):
 for i in range(1,11):
  print(f" {a} x {i} = {a*i}")
    
def additiontable(b):
 for i in range(1,11):
  print(f"{b} + {i} ={b+i}")

def subractiontable(c):
 for i in range(1,11):
  print(f"{c} - {i} ={c-i}")

num=int(input("enter your value"))

print("================================")

multiplicationtable(num)

print("========================")

additiontable(num)

print("==============================")

subractiontable(num)







