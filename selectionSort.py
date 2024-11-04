def findSmallest(array):
        smallest = array[0]
        index = 0
        for i in range(len(array)):
                if array[i] < smallest:
                        smallest = array[i]
                        index = i
        return index


def selectionSort(array):
        result = []
        for i in range(len(array)):
                smallestIndex = findSmallest(array)
                result.append(array.pop(smallestIndex))
        return result

