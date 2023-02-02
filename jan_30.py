                   #QUESTION-1
percentage=input("Enter the percentage plz:")
grade=""
if int(percentage)>90:
    grade="A"
elif int(percentage)>80 and int(percentage)<=90:
    grade="B"
elif int(percentage)>=60 and int(percentage)<=80:
    grade="C"
else:
    grade="D"
print("Your grade is",grade)
                  


             #QUESTION-2

cost_price=int(input("Enter the cost price in rupees:"))
tax=0
if cost_price>100000:
    tax=(15/100)*cost_price
if cost_price > 50000 and cost_price<=100000:
    tax=(10/100)*cost_price
if cost_price<=50000:
    tax=(5/100)*cost_price
print("Tax to paid by you is Rs",tax)




                 #QUESTION-3
city_name=input('Plz enter the city name:')
if city_name.lower() =="delhi":
    monument="Red Fort"
if city_name.lower()=="agra":
    monument="Taj Mahal"
if city_name.lower() == "jaipur":
    monument="Jal Mahal"
print("The monument is",monument)


                #QUESTION-4
number=int(input("Enter a number:"))
count=0
bool=False
while(number>=10):
    if number%3==0:
        count=count+1
        bool=True
    number=number/3
if bool==True:
    print("The count is",count)
else:
    print('Number is not divisible by 3 at all.')

               #QUESTION-5
'''
        While loop is used for iterating unkwown number of times(set by the programmer) until a given condition is met/satisfied.
        Once satisfied the condition the iteration stops.We use while loop for iterating when boundary condition is given to us for
        iterating

'''


              #QUESTION-6
n=int(input("Enter the number of stars in the 1st row:"))
i=0
while(i<n):
    j=0
    while(j<(n-i)):
        print("*",end=" ")
        j+=1
    print("")
    i+=1
print("\n")

k=0
while(k<n):
    l=0
    while(l<(k+1)):
        print("*",end=" ")
        l+=1
    print("")
    k+=1



print("\n")
m=0
while(m<n):
    p=0
    while(p<m+1):
        print(m+1-p,end=" ")
        p+=1
    print(" ")
    m+=1
print("\n")

                               #QUESTION-7,8
i=10
while(i>0):
    print(i)
    i-=1






