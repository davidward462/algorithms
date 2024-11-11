def binarySearch(inputList, item):
        return None

def quicksort(array):
        if (len(array) < 2):
                # base case
                return array
        else:
                # recursive case
                pivot_index = 0
                pivot = array[pivot_index]
                less = []
                for i in range(len(array)):
                        if (i != pivot_index):
                                if (array[i] < pivot):
                                        less.append(array[i])

                greater = []
                for i in range(len(array)):
                        if (i != pivot_index):
                                if (array[i] > pivot):
                                        greater.append(array[i])
                return quicksort(less) + [pivot] + quicksort(greater)
