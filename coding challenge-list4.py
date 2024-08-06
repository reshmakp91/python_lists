
n1 = int(input("Enter the number of elements of list1: "))
list1 = []
for i in range(n1):
    a = int(input("Enter element: "))
    list1.append(a)
n2 = int(input("Enter the number of elements of list2: "))
list2 = []
for i in range(n2):
    a = int(input("Enter element: "))
    list2.append(a)
print("List 1 is : ", list1)
print("List 2 is : ", list2)
result = [i for i in list1 if i in list2]
print("The common elements are : ", result )