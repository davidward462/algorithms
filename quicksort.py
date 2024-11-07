def quicksort(array):
        if (len(array) < 2):
                # base case
                return array
        else:
                # recursive case
                pivot = array[0]

                # list comprehension
                #less = [i for i in array[1:] if i <= pivot]

                less = []
                for i in array[1:]:
                        if i <= pivot:
                                less.append(i)

                # list comprehension
                #greater = [i for i in array[1:] if i > pivot]

                greater = []
                for i in array[1:]:
                        if i > pivot:
                                greater.append(i)

                return quicksort(less) + [pivot] + quicksort(greater)

