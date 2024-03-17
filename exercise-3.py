def remove_all_after(numbers, n):
    # check the element if n in the list 
    if n in numbers:
    # if n in the list, return element from the first to the element that user input 
        return numbers[:numbers.index(n) + 1]
    # if n is not in the list, return the original list 
    return numbers


