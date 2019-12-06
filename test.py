import packages
import distances

# p1 = packages.package1
# p2 = packages.package2
# p3 = packages.package3
# p4 = packages.package4
# p5 = packages.package5
# p6 = packages.package6
# p7 = packages.package7
# p8 = packages.package8
# p9 = packages.package9
# p10 = packages.package10
# p11 = packages.package11
# p12 = packages.package12
# p13 = packages.package13
# p14 = packages.package14
# p15 = packages.package15
# p16 = packages.package16
# p17 = packages.package17
# p18 = packages.package18
# p19 = packages.package19
# p20 = packages.package20
# p21 = packages.package21
# p22 = packages.package22
# p23 = packages.package23
# p24 = packages.package24
# p25 = packages.package25
# p26 = packages.package26
# p27 = packages.package27
# p28 = packages.package28
# p29 = packages.package29
# p30 = packages.package30
# p31 = packages.package31
# p32 = packages.package32
# p33 = packages.package33
# p34 = packages.package34
# p35 = packages.package35
# p36 = packages.package36
# p37 = packages.package37
# p38 = packages.package38
# p39 = packages.package39
# p40 = packages.package40

# set address_id for all packages
# use: corresponds to distances graph
address_id = -1


def set_address_id(graph, package):
    # print(graph)
    # print(package)
    for i in graph:
        if i[1] == package.delivery_address:
            package.address_id = i[0]


set_address_id(distances.address_hash, p1)
set_address_id(distances.address_hash, p2)
set_address_id(distances.address_hash, p3)
set_address_id(distances.address_hash, p4)
set_address_id(distances.address_hash, p5)
set_address_id(distances.address_hash, p6)
set_address_id(distances.address_hash, p7)
set_address_id(distances.address_hash, p8)
set_address_id(distances.address_hash, p9)
set_address_id(distances.address_hash, p10)
set_address_id(distances.address_hash, p11)
set_address_id(distances.address_hash, p12)
set_address_id(distances.address_hash, p13)
set_address_id(distances.address_hash, p14)
set_address_id(distances.address_hash, p15)
set_address_id(distances.address_hash, p16)
set_address_id(distances.address_hash, p17)
set_address_id(distances.address_hash, p18)
set_address_id(distances.address_hash, p19)
set_address_id(distances.address_hash, p20)
set_address_id(distances.address_hash, p21)
set_address_id(distances.address_hash, p22)
set_address_id(distances.address_hash, p23)
set_address_id(distances.address_hash, p24)
p25.address_id = 7
p26.address_id = 25
set_address_id(distances.address_hash, p27)
set_address_id(distances.address_hash, p28)
set_address_id(distances.address_hash, p29)
set_address_id(distances.address_hash, p30)
set_address_id(distances.address_hash, p31)
set_address_id(distances.address_hash, p32)
set_address_id(distances.address_hash, p33)
set_address_id(distances.address_hash, p34)
set_address_id(distances.address_hash, p35)
set_address_id(distances.address_hash, p36)
set_address_id(distances.address_hash, p37)
set_address_id(distances.address_hash, p38)
set_address_id(distances.address_hash, p39)
set_address_id(distances.address_hash, p40)

# initialize and set address_ids list
address_ids_list = [
    (p1.package_id_number, p1.address_id),
    (p2.package_id_number, p2.address_id),
    (p3.package_id_number, p3.address_id),
    (p4.package_id_number, p4.address_id),
    (p5.package_id_number, p5.address_id),
    (p6.package_id_number, p6.address_id),
    (p7.package_id_number, p7.address_id),
    (p8.package_id_number, p8.address_id),
    (p9.package_id_number, p9.address_id),
    (p10.package_id_number, p10.address_id),
    (p11.package_id_number, p11.address_id),
    (p12.package_id_number, p12.address_id),
    (p13.package_id_number, p13.address_id),
    (p14.package_id_number, p14.address_id),
    (p15.package_id_number, p15.address_id),
    (p16.package_id_number, p16.address_id),
    (p17.package_id_number, p17.address_id),
    (p18.package_id_number, p18.address_id),
    (p19.package_id_number, p19.address_id),
    (p20.package_id_number, p20.address_id),
    (p21.package_id_number, p21.address_id),
    (p22.package_id_number, p22.address_id),
    (p23.package_id_number, p23.address_id),
    (p24.package_id_number, p24.address_id),
    (p25.package_id_number, p25.address_id),
    (p26.package_id_number, p26.address_id),
    (p27.package_id_number, p27.address_id),
    (p28.package_id_number, p28.address_id),
    (p29.package_id_number, p29.address_id),
    (p30.package_id_number, p30.address_id),
    (p31.package_id_number, p31.address_id),
    (p32.package_id_number, p32.address_id),
    (p33.package_id_number, p33.address_id),
    (p34.package_id_number, p34.address_id),
    (p35.package_id_number, p35.address_id),
    (p36.package_id_number, p36.address_id),
    (p37.package_id_number, p37.address_id),
    (p38.package_id_number, p38.address_id),
    (p39.package_id_number, p39.address_id),
    (p40.package_id_number, p40.address_id)
]



# function to hash and sort a row for distances in ascending order
def sort_graph_for_shortest_distances(row):
    temp_address_id = 1
    # put each row of distance graph in ascending order
    # keep track of original positions
    for col in row[1:]:
        sorted_dist = row
        # add hash to column to keep track of original location
        sorted_dist[temp_address_id] = (temp_address_id, col)
        # if dist_graph[0][temp_address_id][1] < dist_graph[0][temp_address_id + 1][1]
        temp_address_id += 1
    sorted_dist.pop(0)
    sorted_dist.sort(key=takeSecond)
    # temp_graph.sort(key=takeSecond)

    return sorted_dist


def build_shortest_dists_graph(dist_graph):
    # initialize shortest distances graph
    shortest_dists = []
    # sort rows of dist_graph for shortest distances then append to shortest_dists graph
    for row in dist_graph:
        sorted_row = sort_graph_for_shortest_distances(row)
        shortest_dists.append(sorted_row)
    return shortest_dists


# nearest neighbor algorithm
visited_locations = []
def find_next_location(address_list, current_location):
    # build graph of shortest distance in ascending order
    shortest_dists = build_shortest_dists_graph(distances.distances)
    # go to first address from HUB
    # find any package(s) with address ID 21
    distance_driven = 0
    next_location = -1
    # todo test for accuracy
    for p in address_list:
        # p[0] is package id
        pkg_id = p[0]
        # p[1] is location id
        p_del_id = p[1]
        next_location = shortest_dists[0][1][0]
        print("next:", next_location)
        # you are looking for the next location id that is not 1 in the list
        if (current_location > 1) and (pkg_id == next_location) and (pkg_id not in visited_locations):
            visited_locations.append(shortest_dists[0][1][0])
            # print(shortest_dists[current_location])
            shortest_dist = shortest_dists[current_location][1][1]
            distance_driven += float(shortest_dist)
            print("success")
            current_location = next_location
            next_location = shortest_dists[current_location][1][0]
            return next_location
        elif (pkg_id == next_location) and (pkg_id not in visited_locations):
            visited_locations.append(shortest_dists[0][1][0])
            # print(shortest_dists[current_location])
            shortest_dist = shortest_dists[current_location][1][1]
            distance_driven += float(shortest_dist)
            print("success")
            current_location = next_location
            next_location = shortest_dists[current_location][1][0]
            return next_location

# time to get to location (18mi/hr)
def get_time_to_location(miles):
    miles_per_hour = 18
    minutes_per_hour = 60
    seconds_per_minute = 60
    distance = miles
    time = miles/18
    return time



def get_distance_to_closest_location(dist_graph, package_list):
    current_location = 2
    # print("distg:", dist_graph)
    # print("alist:", address_ids_list)
    # find next closest location
    closest_location = find_next_location(address_ids_list, current_location)
    # calculate time to get there
    print("c", closest_location)

# function to return the second element of the
# two elements passed as the paramater
print(get_distance_to_closest_location(distances.distances, packages.package_list))
print(visited_locations)
print("time:", get_time_to_location(60))


'''
Nearest Neighbor Algorithm
1. initialize all vertices as unvisited
2. select an arbitrary vertex, set it as the current vertex u. Mark U as visited
3. find out the shortest edge connectoin the current vertex u and an unvisted vertex v
4. set v as the current vertex u. mark v as visted
5. if all the vertices in the domain are visted then terminate. Else go to step 3

'''
'''
https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
k-nearest neighbor algorithm KNN

1. load data
2. Initialize K to chosen number of neighbors 
    a. K = num packages left to deliver
3. for each example in data
    a. calculate the distance between the query example and the current example from the data
    b. add the distance and the index of the example to an ordered collection
4. sort the ordered collection of distances and indices in ascending order by the distances
5. pick the first K entries from the sorted collection
6. get the labels of the selected K entries
7. If regression, return the mean of the K labels
8. If classification, return the mode of the K labels
'''

