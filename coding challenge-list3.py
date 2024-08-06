# removing duplicates in a list
n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    a = int(input("Enter element: "))
    list1.append(a)
print("The list before removing duplicates", list1)
def Remove(a):
    list2 = []
    for i in a:
        if i not in list2:
            list2.append(i)
    return list2     
print(Remove(list1))
