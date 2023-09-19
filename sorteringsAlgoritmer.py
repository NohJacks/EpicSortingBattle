import random, copy

def selectionSort(arr):
    arr=arr.copy()


def bubbleSort(arr):
        arr=arr.copy()
        n = len(arr)

        swapped = False

        for i in range(n - 1):

            for j in range(0, n - i - 1):


                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


            if not swapped:
                break

        return arr

if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bubbleSort(lb)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
