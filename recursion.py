def fact(x):
        if x == 1:
                return 1
        else:
                return x * fact(x-1)

def sum(array):
        total = 0
        if len(array) == 0:
                return 0
        else:
                return array.pop() + sum(array)
        return total
