# reverse the elements in a list
n = int(input("Enter the number of elements: "))
list1 = []

for i in range(n):
    a = int(input("Enter element: "))
    list1.append(a)

print("The list before reversing is", list1)

def revrs(a):
    rev_list1 = []
    for i in range(len(a) - 1, -1, -1):
        rev_list1.append(a[i])
    return rev_list1

print("The list after reversal:", revrs(list1))
