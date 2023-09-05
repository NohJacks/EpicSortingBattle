import random, copy

def bubbleSort (items):
    n = len(items)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0,n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if items[j] > items[j+1]:
                swapped = True
                # code below swaps the current number with the next one
                # python has a wierd thing where [=] can swap.
                items[j], items[j+1] = items[j+1], items[j]
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            if not swapped:
                break
    return items

def selectionSort(array):
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



if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = selectionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('blandet: ', lb)
    print('sorteret:', ls)
