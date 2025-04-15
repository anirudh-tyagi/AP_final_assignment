def process_list(lst):
    # a. Print the fourth item in the list
    if len(lst) >= 4:
        print(f"Fourth item: {lst[3]}")
    else:
        print("The list has fewer than 4 items.")
    
    # b. Print all items in the list except the first two
    print(f"Items except the first two: {lst[2:]}")
    
    # c. Print the list in reverse order
    print(f"List in reverse order: {lst[::-1]}")
    
    # d. Print the sum of elements in the list
    print(f"Sum of elements: {sum(lst)}")
    
    # e. Print the maximum and minimum elements in the list
    print(f"Maximum element: {max(lst)}")
    print(f"Minimum element: {min(lst)}")
    
    # f. If the list contains a zero, print out the index of the first zero, else print -1
    if 0 in lst:
        print(f"Index of first zero: {lst.index(0)}")
    else:
        print("-1")
    
    # g. Print the list sorted in ascending and descending order
    print(f"Sorted list in ascending order: {sorted(lst)}")
    print(f"Sorted list in descending order: {sorted(lst, reverse=True)}")

process_list([10, 20, 30, 40, 50, 60, 70, 80])
