#Bubble Sort 

"""Implement the bubble sort algorithm."""
#ToDo: UnitTest
#ToDo: change the function arguemnts  

def bubble_sort(list_):
    """Implement the bubble sort algorithm on the given list and return a 
    sorted list."""
    #This does it in place.
    swapped = False
    n = len(list_)
    count = 0
    while not swapped:
        swapped = True
        for i in xrange(n-1):
            if list_[i] > list_[i+1]:
                list_[i], list_[i+1] = list_[i+1], list_[i]
                swapped = False
        #This is to break out of loop, during debugging.
        if count > 10000:
            print "Failsafe break out of loop", count
            break
        count += 1
        n = n - 1
    return list_

print bubble_sort([1,2,3,4,5,6])
print bubble_sort([3,4,-1,3,5])
print bubble_sort([1,2,2,3,3,2,2,2,2])
print bubble_sort([5,4,3,2,1])            