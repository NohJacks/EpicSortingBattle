import random, copy


def bubbleSort(items):
    n = len(items)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if items[j] > items[j + 1]:
                swapped = True
                items[j], items[j + 1] = items[j + 1], items[j]
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            if not swapped:
                break
    return items

def selectionSort(array):
    # Return the number of items in a list: so if there are 100 diffrent numbers. size would be 100
    size = len(array)
    # for every item in size. set i as min_index.
    # #this means if the funktion has run 2 times. the first item is sorted and
    # the next non-sorted number is 2
    for i in range(size):
        min_index = i
    # gets compared with other items in the list in the form of j. j is i+1,
    # meaning its always the next number after i
        for j in range(i + 1, size):
            # goes though the entire list and selects the minimum element in every iteration,
            # meaning it manuel compares each item to se if is smaller than the current seleceted.
            if array[j] < array[min_index]:
                min_index = j
                # after runing whought entire list, the elements swap the to sort the array.
                #that is to say it puts it on the current i (number space)
                (array[i], array[min_index]) = (array[min_index], array[i])
    return array

def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return   # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

    return arr

"""def mergeSort(arr,l,m,r):
        n1 = m - 1 + 1
        n2 = r - m

    # create temperay arrays
        L = [0]*(n1)
        R = [0]*(n2)

        # Copy data to temp arrays L[] and R[]
        for i in range (0,n1):
            L[i]=arr[1+i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1

        # l is for left index and r is right index of the
        # sub-array of arr to be sorted

        def merge(arr, l, r):
            if l < r:
                #Same as (l+r)//2, but avoids overflow for
                #large l and h
                m = l + (r - l) // 2

                #Sort first and second halves
                merge(arr, l, m)
                merge(arr, m + 1, r)
                mergeSort(arr, l, m, r)

        # Driver code to test above
        arr = [12, 11, 13, 5, 6, 7]
        n = len(arr)
        print("Given array is")
        for i in range(n):
            print("%d" % arr[i], end=" ")

        mergeSort(arr, 0, n - 1)
        print("\n\nSorted array is")
        for i in range(n):
            print("%d" % arr[i], end=" ")
"""

if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        # Kald den funktion, du vil teste
        ls = selectionSort(l)


        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('blandet: ', lb)
    print('sorteret:', ls)
