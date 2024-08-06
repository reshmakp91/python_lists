
n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    a = int(input("Enter element: "))
    list1.append(a)
print("The list is", list1)
x = int(input("Enter the number to count in list: "))

def count(list1, x):
    count = 0
    for i in list1:
        if (i == x):
            count +=  1
    return count
print("The count of",x,"in",list1,": ",count(list1,x))


