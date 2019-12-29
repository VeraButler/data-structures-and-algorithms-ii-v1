import csv

# import distance data
distance_table = './WGU Dist Table.csv'

# START clean distance data
dist_tbl_hash = []
# distance graph for algorithm
distances = []
# address hash
address_hash = []
with open(distance_table) as dt:
    # remove new line \n
    filtered = (line.replace('\n', '') for line in dt)
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
            street_address = s[1:(i)]
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
for row in distances:
    # fix last element from ' ' to ''
    row[-1] = ''
    for i, col in enumerate(row):
        if col is '':
            # get hash id for row
            u = row[0]
            # set col to distance from distance A -> B
            # print(distances[count - 1][u])
            a_to_b = distances[i-1][u]
            row[i] = a_to_b
    # fix index
    del row[0]
    # print(row)
# END clean distance data



# START print functions
def print_street_address_only():
    for a in address_hash:
        print(a)


# Graph class
def build_bidirectional_distance_graph():
    # test variables
    first_line = True
    empty = ''

    # create new distance graph
    new_dist_graph = []
    for u, d in enumerate(dist_tbl_hash):
        if first_line:  # skip key:address line
            first_line = False
            continue
        for v, e in enumerate(dist_tbl_hash[u]):
            # if v is 1:
            # print(dist_tbl_hash[u][v])
            # del dist_tbl_hash[u][v]
            # skip first three elements
            if v > 2:
                if e is '':
                    #  find corresponding value in row to build bidirectional graph
                    d[v] = dist_tbl_hash[v - 2][u + 2]  # subtract 2 from v and add 2 to u to correct for skipped lines
                    # print(dist_tbl_hash[v][u + 2])
        new_dist_graph.append(d)

    #  for each row in new_dist_graph
    #       delete address in each row
    #       key:value pairs for address_id:mileage
    for row in new_dist_graph:
        row[0] = row[0] - 1
        del row[1]
    for i, row in enumerate(new_dist_graph):
        for j, el in enumerate(row):
            if j > 1:
                row[j] = (j - 2, float(el))
        prepare_row_for_sort = row[2::]
        save_row = [row[0], row[1]]
        prepare_row_for_sort.sort(key=lambda x: x[1])
        save_row.append(prepare_row_for_sort)
        # print(save_row)
        new_dist_graph[i] = save_row
    return new_dist_graph


class Graph:
    """  Graph formats the distance data in dist_tbl_graph into a bidirectional graph

        class member bidirectional:
            presorted key:value pairs of address_id:mileage in ascending order by mileage
    """
    def __init__(self):
        # data
        self.adjacency_list = distances
        self.sorted_bidirectional = build_bidirectional_distance_graph()
        self.distances_from_hub = []


    # def dij(self, start_vertex):
    #     g = self.adjacency_list
    #     # Put all vertices in an unvisited queue.
    #     unvisited_queue = []
    #     for current_vertex in g:
    #         unvisited_queue.append(current_vertex)
    #
    #     # start_vertex has a distance of 0 from itself
    #     distance_to_self = g[start_vertex][0]
    #
    #     # One vertex is removed with each iteration; repeat until the list is
    #     # empty.
    #     while len(unvisited_queue) > 0:
    #
    #         # Visit vertex with minimum distance from start_vertex
    #         smallest_index = self.sorted_bidirectional[start_vertex][0]
    #         for i in range(1, len(unvisited_queue)):
    #             if unvisited_queue[start_vertex][i] < unvisited_queue[smallest_index][i]:
    #                 smallest_index = i
    #         current_vertex = unvisited_queue.pop(smallest_index)
    #
    #         # Check potential path lengths from the current vertex to all neighbors.
    #         for adj_vertex in self.adjacency_list[current_vertex]:
    #             edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
    #             alternative_path_distance = current_vertex.distance + edge_weight
    #
    #             # If shorter path from start_vertex to adj_vertex is found,
    #             # update adj_vertex's distance and predecessor
    #             if alternative_path_distance < adj_vertex.distance:
    #                 adj_vertex.distance = alternative_path_distance
    #                 adj_vertex.pred_vertex = current_vertex




g = Graph()
# print(g.adjacency_list)
# print(g.sorted_bidirectional)




        # if g.sorted_bidirectional[smallest_index][2][1]:
        #     print(g.sorted_bidirectional[smallest_index][2][1])
        # for adj_vertex in g.sorted_bidirectional[smallest_index][2]:
        #     # print(adj_vertex)
        #     if adj_vertex[0] not in unvisited_queue and adj_vertex[0] != smallest_index:
        #         edge_weight = adj_vertex[]
        #         alternative_path_distance =
            # edge_weight = g.adjacency_list[start_vertex][adj_vertex[0]]
            # print(edge_weight)
        #             alternative_path_distance = current_vertex.distance + edge_weight
        # if alternative_path_distance < adj_vertex.distance:
        #     adj_vertex.distance = alternative_path_distance
        #     adj_vertex.pred_vertex = start_vertex




# for g in g.sorted_bidirectional:
#     print(g)
# route(0)


###############  ###############
########### TEST AREA ##########
###############  ###############

# def set_vertex(self, vertex):
#     self.vertex = vertex
#
# def get_distances_from_hub(self):
#     """
#
#     creates a list of distances in
#         key:value pairs of address_id:miles_from_hub
#     these key:value pairs will be used to insert into a circular route
#     the packages with address ids closest to the hub will be inserted into to the
#      beginning and end of the best_route array
#
#     """
#     for d in self.sorted_bidirectional:
#         # print('d', d)
#         for distances in d[2:]:
#             # print('dist', distances)
#             address_id = distances[0][0]
#             for pairs in distances:
#                 # print(pairs)
#                 if pairs[0] == 0:
#                     hub = pairs
#         self.distances_from_hub.append((address_id, hub[1]))
#     # remove hub
#     self.distances_from_hub.pop(0)
#     self.distances_from_hub.sort(key=lambda x: x[1])
#
# def dijkstra_shortest_path(self, start_vertex):
#     # Put all vertices in an unvisited queue.
#     unvisited_queue = []
#     self.set_vertex(start_vertex)
#
#     for current_vertex in g.adjacency_list:
#         unvisited_queue.append(current_vertex)
#
#     # start_vertex has a distance of 0 from itself
#     start_vertex.distance = 0
#
#     # One vertex is removed with each iteration; repeat until the list is
#     # empty.
#     while len(unvisited_queue) > 0:
#
#         # Visit vertex with minimum distance from start_vertex
#         smallest_index = 0
#         for i in range(1, len(unvisited_queue)):
#             if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
#                 smallest_index = i
#         current_vertex = unvisited_queue.pop(smallest_index)
#
#         # Check potential path lengths from the current vertex to all neighbors.
#         for adj_vertex in self.adjacency_list[current_vertex]:
#             edge_weight = self.edge_weights[(current_vertex, adj_vertex)]
#             alternative_path_distance = current_vertex.distance + edge_weight
#
#             # If shorter path from start_vertex to adj_vertex is found,
#             # update adj_vertex's distance and predecessor
#             if alternative_path_distance < adj_vertex.distance:
#                 adj_vertex.distance = alternative_path_distance
#                 adj_vertex.pred_vertex = current_vertex


# def dijkstras_sp(self, start_vertex):
#     # make a copy of the master graph
#     # todo replace with package list later
#     data = self.bidirectional[start_vertex]
#     print(data)
#     # put all vertices in an unvisited queue
#     unvisited_queue = []
#     for current_vertex in data:
#         current_vertex = float(current_vertex)
#         unvisited_queue.append(current_vertex)
#
#     # start_vertex has a distance of 0 from itself
#     start_vertex_distance = data[start_vertex][start_vertex]
#
#     # one vertex is removed with each iteration; repeat until the list is empty
#     while len(unvisited_queue) > 0:
#
#         # Visit vertex with  minimum distance from start_vertex
#         smallest_index = 0
#         for i in range(1, len(unvisited_queue)):
#             if unvisited_queue[i] < unvisited_queue[smallest_index]:
#                 smallest_index = i
#         current_vertex = unvisited_queue.pop(smallest_index)
#
#         # Check potential path lengths from the current vertex to all neighbors
#         for adj_vertex in data[current_vertex]:
#             edge_weight = self.edge_weights[(current_vertex, adj_vertex)]
#             alternative_path_distance = adj_vertex + edge_weight
#
#             # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
#             if alternative_path_distance < adj_vertex:
#                 adj_vertex = alternative_path_distance
#                 prev_adj_vertex = current_vertex

###https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

# print solution
# def print_solution(self, dist):
#     print("Vertex tDistance from Source")
#     for node in range(self.V):
#         print(node, "to", node + 1, ":", dist[node])
#
#
# def min_distance(self, dist, spt_set):
#     """
#     A utility function to find the vertex with minimum distance value,
#     from the set of vertices not yet included in shortest path tree
#     """
#     # initialize minimum distance for next node
#     minimum = float('inf')
#
#     # search not nearest vertex not in the shortest path tree
#     for v in range(self.V):
#         if dist[v] < minimum and spt_set[v] is False:
#             minimum = dist[v]
#             minimum_index = v
#     return minimum_index
#
#
# def dijkstras(self, src):
#     """
#     This function implements Dijkstra's single source shortest path algorihtm for a graph represented using
#     adjacency matrix representation
#     """
#     # initilize variables
#     dist = [float('inf')] * self.V
#     dist[src] = 0
#     spt_set = [False] * self.V
#
#     for cout in range(self.V):
#         """
#         Pick the minimum distance vertex from the set of vertices not yet processed.
#         u is always equal to src in the first iteration
#         """
#         u = self.min_distance(dist, spt_set)
#
#         """Put the minimum distance vertex in the shortest path tree"""
#         spt_set[u] = True
#
#         """Update dist value of the adjacent vertices of the picked vertex only if the current
#         distance is greater than new distance and teh vertex is not in the shorrtest path tree
#         """
#         for v in range(self.V):
#             if float(self.bidirectional[u][v]) > 0 and spt_set[v] == False and dist[v] > dist[u] + float(
#                     self.bidirectional[u][v]):
#                 dist[v] = dist[u] + float(self.bidirectional[u][v])
#     self.print_solution(dist)