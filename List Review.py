def half_list(lst1):
    lst2=[]
    for idx in range (0,len(lst1)//2):
        lst2= lst2+ [lst1[idx]]
    return lst2

half_list=half_list([2,4,6,8,10,12,14])

print(half_list)


def count_func(lst):
    value_count=0
    for inx in range(0, len(lst)):
        if len(lst)>2:
            value_count+=1
    return value_count
count=count_func([1,2,3,4,5])
print(count)
