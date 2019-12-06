from package import Package, get_pkg_list
import distances


# pXX stands for packageNUM
p1 = Package(1)
p2 = Package(2)
p3 = Package(3)
p4 = Package(4)
p5 = Package(5)
p6 = Package(6)
p7 = Package(7)
p8 = Package(8)
p9 = Package(9)
p10 = Package(10)
p11 = Package(11)
p12 = Package(12)
p13 = Package(13)
p14 = Package(14)
p15 = Package(15)
p16 = Package(16)
p17 = Package(17)
p18 = Package(18)
p19 = Package(19)
p20 = Package(20)
p21 = Package(21)
p22 = Package(22)
p23 = Package(23)
p24 = Package(24)
p25 = Package(25)
p26 = Package(26)
p27 = Package(27)
p28 = Package(28)
p29 = Package(29)
p30 = Package(30)
p31 = Package(31)
p32 = Package(32)
p33 = Package(33)
p34 = Package(34)
p35 = Package(35)
p36 = Package(36)
p37 = Package(37)
p38 = Package(38)
p39 = Package(39)
p40 = Package(40)

package_list = get_pkg_list()

# create a list of up to 16 packages, with the shortest distances, to load onto each truck
###################################
# set address_id for all packages
# use: corresponds to distances graph
address_id = -1


def set_address_id(graph, package):  # set address ids helper function
    # print(graph)
    # print(package)
    for i in graph:
        if i[1] == package.delivery_address:
            package.address_id = i[0]


# set all address ids for packages
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
p25.address_id = 7  # data format inconsistency - needed manual entry here
p26.address_id = 25  # data format inconsistency - needed manual entry here
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


# helper function to take second element for a sort
def take_second(elem):
    return elem[1]


# function to hash and sort a row for distances in ascending order
def sort_graph_for_shortest_distances(row):
    temp_address_id = 1
    # put each row of distance graph in ascending order
    # must keep track of original positions
    for col in row[1:]:
        sorted_dist = row
        # add hash to column to keep track of original location
        sorted_dist[temp_address_id] = (temp_address_id, col)
        # if dist_graph[0][temp_address_id][1] < dist_graph[0][temp_address_id + 1][1]
        temp_address_id += 1
    # remove first element from the sorted_dist row
    sorted_dist.pop(0)
    sorted_dist.sort(key=take_second)
    # temp_graph.sort(key=takeSecond)
    return sorted_dist


# build a sorted distance graph for easier access to the data and program readability
def build_shortest_dists_graph(dist_graph):
    # initialize shortest distances graph
    shortest_dists = []
    # sort rows of dist_graph for shortest distances then append to shortest_dists graph
    for row in dist_graph:
        sorted_row = sort_graph_for_shortest_distances(row)
        shortest_dists.append(sorted_row)
    return shortest_dists


# nearest neighbor algorithm

# initialize and set empty visited locations list
visited_locations = []
# initialize and set empty closest location
current_location = 1
count = 0
# find the package with the closest location relative to current location
def find_next_location(address_list, location, count):
    # build graph of shortest distance in ascending order
    shortest_dists = build_shortest_dists_graph(distances.distances)
    # go to first address from HUB
    # find any package(s) with address ID 21
    distance_driven = 0
    next_location = -1
    # define and set counter
    # todo test for accuracy
    for p in address_list:
        # p[0] is package id
        pkg_id = p[0]
        # p[1] is location id
        p_del_id = p[1]
        # find the nearest neighbor
        next_location = shortest_dists[0][1][0]
        # keep track of visited locations with an array
        visited_locations.append(shortest_dists[0][1][0])
        # the next location id that is not 1 in the list
        if location is 1:
            print('if1')
            print('  c', count)
            # find the shortest distance from the current location
            shortest_dist_miles = shortest_dists[location][count][1]
            distance_driven += float(shortest_dist_miles)
            print("  if1-sd1:", shortest_dist_miles)
        # all other locations besides the HUB (address_id 1)
        if location is not 1:
            print('if2')
            print('  c', count)
            shortest_dist_miles = shortest_dists[next_location][count][1][1]
            print("  if2-sd2:", shortest_dist_miles)
            if count is 2:
                print('  if-if')
                distance_driven = distance_driven + float(shortest_dist_miles)
            else:
                print('  if - else :', shortest_dist_miles)
                distance_driven = distance_driven + float(shortest_dist_miles[1])
                print("  dist driven: ", distance_driven)
        print("sd2outer:", shortest_dist_miles)
        curr_location = next_location
        get_distance_to_closest_location(address_list, curr_location, count)
        next_location = shortest_dists[curr_location][1][0]

    return next_location



# time to get to location (18mi/hr)
def get_time_to_location(miles):
    miles_per_hour = 18
    minutes_per_hour = 60
    seconds_per_minute = 60
    distance = miles
    time = miles/18
    return time


def get_distance_to_closest_location(dist_graph, location, count):
    count = count + 1
    # current_location = 1
    # print("distg:", dist_graph)
    # print("alist:", address_ids_list)
    # find next closest location
    closest_location = find_next_location(address_ids_list, location, count)
    # calculate time to get there
    print("c", closest_location)

# function to return the second element of the
# two elements passed as the paramater
print(get_distance_to_closest_location(distances.distances, current_location, count))
print(get_distance_to_closest_location(distances.distances, current_location, count))
print(visited_locations)
print("time:", get_time_to_location(60))

# print(package1.info())
# print(package2.info())
# print(package3.info())
# print(package4.info())
# print(package5.info())
# print(package6.info())
# print(package7.info())
# print(package8.info())
# print(package9.info())
# print(package10.info())
# print(package11.info())
# print(package12.info())
# print(package13.info())
# print(package14.info())
# print(package5.info())
# print(package6.info())
# print(package7.info())
# print(package8.info())
# print(package9.info())
# print(package10.info())
# print(package1.info())
# print(package2.info())
# print(package3.info())
# print(package4.info())
# print(package5.info())
# print(package6.info())
# print(package7.info())
# print(package8.info())
# print(package9.info())
# print(package10.info())
