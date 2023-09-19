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

def selectionSxort(array):
    size = len(array)
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
                # swapping the elements to sort the array
                (array[i], array[min_index]) = (array[min_index], array[i])
    return array

def insertionSxort(arr):
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

def merge(arr,l,m,r):
    n1 = m - 1 + 1
    n2 = r - m

# create temperay arrays
#L = [0]*(n1)
#R = [0]*(n2)



if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        # Kald den funktion, du vil teste
        ls = bubbleSort(l)


        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('blandet: ', lb)
    print('sorteret:', ls)


