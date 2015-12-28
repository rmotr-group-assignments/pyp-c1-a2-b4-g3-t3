#ToDo: UnitTest

def insertion_sort(list_):
    """Implement the insertion sort algorithm on the given list and return a 
    sorted list."""
    for i, item in enumerate(list_):
        j = i
        while j > 0  and list_[j-1] > item:
            list_[j] = list_[j-1]
            j -= 1
        list_[j] = item
    return list_
    
print insertion_sort([1,2,3,4,5,6])
print insertion_sort([-1,2,-3,4,12,6,7])
print insertion_sort([1,1,1,12,2,2,2,3,3,3,5])
print insertion_sort([5,4,3,2,1])