
n = int(input("Enter the number of elements: "))
list1=[]
sum = 0
avg = 0
for i in range(0,n):
    a =int(input("Enter element: "))
    list1.append(a)
print("The list is ", list1)
for a in list1:
    sum += a
print("The sum is : ", sum)
avg = sum/n
print("The average is : ", avg)

