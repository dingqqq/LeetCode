import random

class Sort:
    def bubbleSort(self, x):

        return

    def quickSort(self, x):

        if len(x) <= 1:
            return x

        pivot = x[0]

        middle = [pivot]
        left = []
        right = []

        for y in x[1:]:
            if y < pivot:
                left.append(y)
            elif y > pivot:
                right.append(y)
            else:
                middle.append(y)

        return self.quickSort(left) + middle + self.quickSort(right)

# Test code
sortClass = Sort()

for i in range(10):
    x = random.sample(range(10), 10)
    print x
    print sortClass.bubbleSort(x)
    print sortClass.quickSort(x)
