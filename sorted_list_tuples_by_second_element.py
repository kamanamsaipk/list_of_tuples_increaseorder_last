original_lst = [(1,9),(2,5,7),(9,3,2),(3,0),(5,8)]
print(original_lst)
for i in range(len(original_lst) - 1):
        for j in range(len(original_lst) - i - 1):
            if original_lst[j][-1] > original_lst[j+1][-1]:                                                                         
                original_lst[j], original_lst[j+1] = original_lst[j+1], original_lst[j]  # Swap it if the current one is larger
            else:
                 pass
print("sorted list of tuples in increasing order by last element is : ", original_lst)


#output:  sorted list of tuples in increasing order by last element is :  [(3, 0), (9, 3, 2), (2, 5, 7), (5, 8), (1, 9)]