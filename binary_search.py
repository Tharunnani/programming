# function for sorting the array
def bubble_sort(arr3):

    for i in range(n):
        for j in range(0, n-i-1):

            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]


# function for binary search
def binary_search(arr2, first1, Last, search1):

    while Last >= first1:
        mid = int(first1 + (Last - 1) / 2)
        mid = int(mid)
        if arr2[mid] == search1:
            return mid

        elif arr2[mid] < search1:
            first1 = mid + 1

        else:
            Last = mid - 1

    return -1


n = int(input("enter the no.of elements: "))  # for input of user specific number of elements

arr = []  # from here taking of input in an array or list
for i in range(0, n):
    arr1 = int(input("enter the element:"))

    arr.append(arr1)

bubble_sort(arr)  # function call for bubble sorting function

print("the sorted array is: ")  # printing the sorted array
for i in range (len(arr)):
    print(arr[i])

first = 0             # defining the variables for first element and last
last = len(arr) - 1

search = int(input("enter the number to be searched: "))  # asking input from user to enter the search element

result = binary_search(arr, first, last, search)  # function call for binary search function

if result != -1:                                        # printing the position of element
    print("element is present at index :", result+1)

else:
    print("element is not found in the array!")


