# In operator:-
#example:-
'''r=[3,4,5,6,]
print (7 in r)
print (4 in r)

#example2:-
b='surya'
surya=b
print (surya in b)

#example:-
num='ntr'
print('t' in num )

r=[3,4,5,6,]
print(4 in r)
print (7 in r)

s=[7,8,9,4,6]
print(6 in s)
print(1 in s)

# is operator:-
#example:-
h=[4,5,6,7,9,]
y=h
print (y is h)
print (h is y)

h=[4,5,6,7,9,]
h=y
print(10 is y )

k='abhi'
abhi=k
print(abhi is k)
s="flower"
flower=y
print(flower is r)

l='teddy'
teddy=y
print(teddy is k)

print ("==================================================")
#conditional statement:-
# example:-
salary=5000
if salary >=10000 and salary <=20000:
    print (" your salary is high")

elif salary >=5000 and salary <=10000:
    print ("your salary is average")

else:
    print ("your salary is low")
    
    # example2
salary=1000

if salary >=15000 and salary <=18000:
     
     print("your salary is high")

elif salary >=5000 and salary <=8000:
     
     print ("your salary is average" )

else:
     print ("your salary is low")        

     
     #looping statements:-
     # examplE:-
     #point all values from array

     Y=[7,8,9,2,4,5]
     for num in y:
          print (num) 
    # example2:-
     surya=[1,2,3,4,5,6,7,8,]
     for num in surya:
       print ("surya")

       #exmple:-
     lalitha=[5,7,9,4,2,6,1,5,7,8,9]
     for num in lalitha:
       print("lalitha")

        #example4:-
       divya=[2,5,8,0,6,4]
       for num in divya:
           print("divya")

       #example:4
       harika=[2,5,8,0,6,4]
       for _ in 'harika':
        print ("harika")

    
        #print value from range values :-
        # examples:-
        for num in range (6):
            print (num)

        for ram in range (10):
            print ("ram")

        for nani in range (6):
            print ("nani")
        
        for _ in range (8):
            print("num")


        #print even numbers using range object -range (start, stop,step):- {even numbers}
        
        # examples:-
            for even in range (10,100,10):
             print (even)
        
        for even in range (4,20,4):
            print (even)

        for even in range (6,80,6):
            print (even) 

               
        print("==========================================================")
        #print odd numbers using range object -range (start,stop,step) :-{odd numbers}
        # example:-1
            
        for odd in range (1,17,3):    
         print (odd)

         for odd in range (5,90,5):
          print (odd)
     
        for odd in range (6,50,2):
          print(odd)

          for fives in range (6,60,3):
             print (fives)

        print ("===================================================")
        # whileloop:-
        # examples:-
        count =30
        while count >20:
           print(count)
           count -= 1          

        print("=================================================")
        # jump statement:-
        # examples:-
        for i in range (20):
           print (i)
           if i ==10:
              break
           
           # example:-2

           for i in range (5):
              if i ==3:
                 break 
              for j in range (4):
                 if j ==2:
                    break
                 print (f" {i} J={j}")

       #break
                 for i in range (10):
                    if i ==5:
                       break
                    print(i)


for i in range (8):
   if i==5:
      break
   for j in range (6):
      if j ==4:
         break
      print(f"i={i} j={j}") 

#continue
      
      if i in range (11):
         if i==5:
          continue
         print (i)





age=int(input("enter your age:"))
if age <=5:
   print ("kid")
elif age >6 and age <=10:
   print ("too young")
elif age >10 and age <=20:
   print ("young")
elif age >20 and age <=30:
   print ("teen")
elif age >30 and age<=50:
   print ("middle age")
elif age >50 and age <=70:
   print ("old")
else:
   print ("death")'''
 





print("====================================")


age=int(input("enter your age"))
if age>25:
    print("wait ")
elif age ==30:
    print("you can marrie")
else:
    print("not eligible")


       

        



            