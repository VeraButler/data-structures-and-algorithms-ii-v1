from distance_table import dist_tbl_hash

# ### Use this space to try out ideas and free code ###
data = dist_tbl_hash
print(data)

T1 = []
T2 = []
T3 = []
list_one = []
list_two = []
list_three = []
visited = []

def get_shortest_distances(list):
    #  temporary list to hold shortest distances
    temp_miles_list = []
    for a in list:
        #  skip first element which is address id
        if isinstance(a, tuple):
            print('sl', a)
            temp_miles_list.append(a[1])
    temp_miles_list.sort()
    print(temp_miles_list)




get_shortest_distances(data[0])
# def sort(data):
#     for i, n in enumerate(data):
#         if i % 3 is 0:
#             max_val = max(data)
#             list_one.append(max_val)
#             visited.insert(0, max_val)
#             data.pop(max_val - 1)
#         elif i % 3 is 1:
#             max_val = max(data)
#             list_two.append(max_val)
#             visited.insert(0, max_val)
#             data.pop(max_val - 1)
#         elif i % 3 is 2:
#             max_val = max(data)
#             list_three.append(max_val)
#             visited.insert(0, max_val)
#             data.pop(max_val - 1)
#     final_lists = [list_one, list_two, list_three]
#     return final_lists
#
#
# # Alternatively, you could sort the list, then get element -1, -2, and -3
# def sort2(data):
#     # print(data)
#     temp_list = [max(data)]
#     data.pop(0)
#     for i, item in enumerate(data):
#         if i % 2 is 0:
#             temp_list.append(item)
#         if i % 2 is 1:
#             temp_list.insert(0, item)
#     return temp_list
#
#
# three_lists = sort(data)
# T1 = sort2(three_lists[0])
# T2 = sort2(three_lists[1])
# T3 = sort2(three_lists[2])

print('visited', visited)
# print('L1', sort2(list_one))
# # print('L1 - sorted', sort2(list_one))
# print('L2', sort2(list_two))
# print('L3', sort2(list_three))
print('T1', T1)
print('T2', T2)
print('T3', T3)
