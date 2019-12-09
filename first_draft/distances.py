import csv
from typing import List, Any
# from packages import *

distance_table = '../WGU Dist Table.csv'

dist_tbl_hash = []
# distance graph for algorithm
distances = []
# address hash
address_hash = []
with open(distance_table) as dt:
    # remove new line \n
    filtered = (line.replace('\n', ' ') for line in dt)
    reader = csv.reader(filtered)
    # row_id is hash for dist_tbl_hash
    row_id = 0
    # skip first row
    dt.readline()
    # append each row to dist_tbl_hash
    for row in reader:
        # print(row)
        # hash each row with row_id and row
        if row_id is 0:
            address_id = 0
            for col in row:
                if col is not 0:
                    temp = col
                    # print(col)
                    # print(temp)
                    col = [address_id + 1, temp]
                    row[address_id] = col
                    address_id += 1

        temp_list = [row_id]
        # use built in extend method to iterate over row and add each element of the row
        temp_list.extend(row)
        dist_tbl_hash.append(temp_list)
        row_id += 1
        # for col in row:
        #     # v = col

    # set variables for insert function
    # delivery_address, delivery_deadline, delivery_city, delivery_state, delivery_zip_code, package_weight,
    #                delivery_status

u = 0
v = 0


for row in dist_tbl_hash:
    if row[0] is 0:
        del row[0]
        street_address = "4001 South 700 East"
        row[0][1] = street_address
        address_hash.append([1, street_address])
    s = str(row[2])
    # https://stackoverflow.com/questions/10059554/inserting-characters-at-the-start-and-end-of-a-string
    street_address = ""
    for i, c in enumerate(s):
        if c is "(":
            # https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/
            # clean the street address of it's zipcode
            street_address = s[1:(i-1)]
            row[2] = street_address
            address_hash.append([row[0], street_address])
            # print(address_hash)
            break
    # build distances_graph
    if isinstance(row[0], list) is False:
        temp_list = [row[0]]
        temp_list.extend(row[3::])
        distances.append(temp_list)
    u += 1
    v += 1

# initialize counter for column numbers
    # use for creating symmetrical graph
    # if col is empty then replace with row[0] -> count
count = 0
for row in distances:
    # fix last element from ' ' to ''
    row[-1] = ''
    for col in row:
        if col is '':
            # get hash id for row
            u = row[0]
            # set col to distance from distance b -> a
            # print(distances[count - 1][u])
            a_to_b = distances[count - 1][u]
            row[count] = a_to_b
        count += 1
    count = 0
# for row in distances:
#     print(row)

# Find shortest distances with Dijkstras Algorithm
# For adjacency matrix representation of the graph
# packages[1] == address == addresses[u-1]
# print(addresses)
# print(dist_tbl_hash)


# class Distance:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
#
#     def print_solution(self, dist):
#         print("Vertices tDistance from Source")
#         for node in range(self.V):
#             print(node, "t", dist[node])
#
#     # A utility function to find teh vertex ith minimum distance value, form the set of vertices
#     # not yet included in shortest path tree
#     def min_distance(self, dist, spt_set):
#
#         # Initialize minimum distance for next node with max system size allowed
#         minimum = 2**63 - 1
#
#         # Search not nearest vertex no in the shortest path tree
#         for v in range(self.V):
#             if dist[v] < minimum and spt_set[v] == False:
#                 minimum = dist[v]
#                 min_index = v
#         return min_index
#
#     # Function that implements Dijkstra's single source
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):
#         dist = [2**63 - 1] * self.V
#         dist[src] = 0
#         spt_set = [False] * self.V
#
#         for cout in range(self.V):
#
#             # Pick the minimum distance vertex from the set of vertices not yet processed
#             # u is always equal to src in first iteration
#             u = self.min_distance(dist, spt_set)
#
#             # Put the minimum distance vertex in the shortest path tree
#             spt_set[u] = True
#
#             # Update dist value of the adjacent vertices of the picked vertex only if the current
#             # distance is greater than new distance and the vertex in not in the shortest path tree
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]
#
#         self.print_solution(dist)
#
# # Driver Program
# g = Distance(27)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#           ]
# g.dijkstra(0)
# print(dist_tbl_hash)
# TODO create a distance graph for dijkstra




# print("dgraph: ", distances)
# print("ahash:", address_hash)


