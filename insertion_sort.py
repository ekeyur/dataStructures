def insertion_sort(list):
    for i in range(1,len(list)):
        j = i
        while j>0 and list[j] < list[j-1]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp
            j = j-1
    return list



def insertion_sort_tuple(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
    return list

# 
# def insertion_sort_prev(list):
#     for i in range(0,len(list)):
#         for j in range(len(list)-1,0,-1):
#             if (list[i] > list[j]):
#                 list[j],list[j-1] = list[j-1],list[j]
#     return list

my_array = [54,26,93,17,77,31,44,55,20]
print(insertion_sort_tuple(my_array))
