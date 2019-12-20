# Other Assumptions:
####################
# Trucks have a “infinite amount of gas” with no need to stop.
# The package ID is unique; there are no collisions.
# No further assumptions exist or are allowed.

# Delivery time is instantaneous, i.e., no time passes while at a delivery
# (that time is factored into the average speed of the trucks).

# The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m.
# The correct address is 410 S State St., Salt Lake City, UT 84111.
#####################
# THOUGHTS:
# The truck is responsible for delivering up to 16 packages at 18 miles per hour.

# imports
import package_info
from graph import g
import time


class Truck:
    # init class
    def __init__(self):
        # Each truck can carry a maximum of 16 packages.
        self.number_of_packages = 0
        # Trucks travel at an average speed of 18 miles per hour.
        self.average_speed = 18
        # Each driver stays with the same truck as long as that truck is in service.
        self.driver = 1
        # Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
        # The day ends when all 40 packages have been delivered.
        self.time = 8
        # There is up to one special note for each package.
        self.package_notes = 'No notes.'
        # track the distance driven
        self.distance = 0
        # package information
        self.all_package_info = []
        # set at hub to True
        self.at_hub = True
        self.full_truck = False

    # add a package
    def add_package(self, package_info):
        #  boolean value for allowance of package add
        can_add_package = True
        if self.number_of_packages < 16:
            self.number_of_packages += 1
            # append package to package info
            self.all_package_info.append(package_info)
        else:
            #  Truck is full. Fill next truck.
            can_add_package = False
            return can_add_package
        # maybe add an error here later (https://stackoverflow.com/questions/33962267/python-return-error-from-function)

# TODO make this algorithm work for the the packages on each truck
#   delivery status
#   delivered timestamp
# graph for tsp, https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
# graph = []
# for d in distance_table.dist_tbl_hash:
#     temp_graph = []
#     for el in d[2:]:
#         temp_graph.append(el[1])
#     graph.append(temp_graph)


# print('delivery_system', dijkstras_delivery_system(graph, 0))
# print('delivery_system', delivery_system(graph, 1))
# Driver Code
# if __name__ == "__main__":
#     # matrix representation of graph
#     graph = [[0, 10, 15, 20], [10, 0, 35, 25],
#              [15, 35, 0, 30], [20, 25, 30, 0]]
#     s = 0
#     print(travellingSalesmanProblem(graph, s))

# ################################################## #

# create trucks
T1 = Truck()
T2 = Truck()
T3 = Truck()

# initiate and set visited variable to an empty list
visited_locations = []
# initiate and set delivered packages list
delivered_packages = []


# function to load the trucks
def load_truck(truck, package_list):
    list_name = package_list[0]
    # check if truck is at the hub and has room
    if truck.at_hub and truck.full_truck is False:
        print('Truck is good to load.')
        print('Loading truck....')
        for package in package_list[1:]:
            if truck.full_truck is True:
                break
            truck.add_package(list_name, package)
            package_list.pop()


# method find_best_route
#   match package address ids to distance table
#     sort distances with nearest neighbor algorithm
#   returns a list of the best route for packages from and to the HUB
# def find_best_route(self, package_list, distances):
#     print('method: find_best_route')
#     #   match package address ids to distance table
#     for d in distances:
#         print(d)

#  this function returns the address id and street address associated with the package id into a list
def build_graph(packages_on_truck_list, master_packages_list, master_distance_list):
    # get package id, address id, street address
    address_list = find_address_list(packages_on_truck_list, master_packages_list)
    master_graph = []
    best_route = []
    # all distances
    for d in master_distance_list:
        # temporary graph to hold each row to be appended to graph
        temp_graph = []
        # for each element in all distances append only the mileage
        for el in d[2:]:
            # get only the distances you need from package list
            for a in address_list:
                # if distance table number is address id then append mileage to temp_graph
                if el[0] == a[1]:
                    temp_graph.append(el[1])
        # append temp_graph as a row in graph
        master_graph.append(temp_graph)
    return master_graph

def find_address_list(packages_list, address_list):
    temp_list = []
    # find address id for package
    #  if package id == package address id
    for a in address_list:
        # print('a', a)
        # find address id and save it to a variable
        for d in g.bidirectional:
            # print('d', d)
            if a[1] == d[1]:
                address_id = d[0]
                # print('address id', address_id)
                break
        for p in packages_list:
            if type(p) is list:
                # print('list')
                if a[0] is p[0]:
                    # a[0] is address id from master address list
                    # a[1] is the address string 'XXX street name' correlated with the address id
                    temp_list.append([a[0], address_id, a[1]])
            if type(p) == int:
                # print('int')
                # print('ptype', type(p))
                # print('a', a)
                if a[0] is p:
                    temp_list.append([a[0], address_id, a[1]])
    # temp_list = [package_id, address_id, address string]
    # print('package address list', temp_list)
    return temp_list

# Python3 program to implement traveling salesman
# problem using naive approach.
maxsize = float('inf')
V = 16

# implementation of traveling Salesman Problem
def dijkstras_delivery_system(graph, s):
    print('calculating....')
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)
        # HEURISTIC:
        # Get the current processor time in seconds using time.process_time() method
        # the larger the value the longer the process will take
        # and the more accurate (shorter miles) the algorithm will be
        # most people are willing to wait 3 seconds for an answer, so I chose 3 as my max wait time value
        max_wait_time = 3
        process_time = time.process_time()
        if not next_permutation(vertex) or process_time > max_wait_time:
            break
    return min_path


# next_permutation implementation
def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


# def find_next_location(distances_list, packages_list):
#     # next location should be closest from current location
#     # current location starts at hub
#     # print('distances_list', distances_list)
#     # print('package_list', packages_list)
#     # get address list using packages_list (package ids) and package_info.pkg_tbl_hash (master package list)
#     #   returns [package_id, address_id, address string]
#     address_list = find_address_list(packages_list, package_info.pkg_tbl_hash)
#     # FIRST find package with closest position to HUB
#     next_location = []
#
#     for d in distances_list[2:]:
#         # print('d', d)
#         for id in address_list:
#             if id[1] == d[0]:
#                 print('id in address list', id)
#                 # print(d)
#                 # print(id)
#                 # append package id, address id, distance from current location
#                 next_location.append((id[0], d[0], d[1]))
#                 # print('next location', next_location)
#                 break
#     # print('package distances from hub', package_distances_from_hub)
#     next_location.sort(key=lambda x: x[2])
#     # print('next location', next_location[0])
#     return next_location
#
#
# def find_best_route(packages_list):
#     best_route = []
#     current_location = 0
#     for p in packages_list:
#         # print('p', p)
#         print('package', p)
#         print('current location list', distance_table.dist_tbl_hash[current_location])
#         next_location = find_next_location(distance_table.dist_tbl_hash[current_location], packages_list)
#         # print('next location', next_location)
#         best_route.append(next_location)
#         current_location = next_location[1][1]
#         # print('current location', current_location)
#         packages_list.remove(p)
#         # print('packages list', packages_list)
#     return best_route


#     # append first location for the first and last el of best route
#     best_route.append(next)
#     # todo before removing packages add them to delivered list with timestamp
#     from_location = (package_distances_from_hub[0])
#     package_distances_from_hub.remove(package_distances_from_hub[0])
#     to_location = (package_distances_from_hub[0])
#     package_distances_from_hub.remove(package_distances_from_hub[0])
#
#     print('package distances from hub', package_distances_from_hub)
#     print(best_route)
#     # NEXT find closests packages to first two locations


#     temp_best_route.reverse()
#     # circular route for truck going from HUB to closest -> max -> back to closest to HUB
#     for i, n in enumerate(pack):
#         # todo add package ids - 'pXX' => address_bidirectional_graph[0] - might be better to add at an earlier time
#         if i % 2 is 0:
#             best_route.append(n)
#             del n
#         if i % 2 is 1:
#             best_route.insert(0, n)
#             del n
#     # best_route = (package id, (address id, miles from current address to next address)
#     # todo drop packages with same address together


# # sort for shortest distances in a row
# #   get sorted shortest distances for any address list in ascending order according to mileage
# #   this is to be used in main algorithm to find the nearest neighbor from the current location
# def find_best_route(package_list):
#     # find distance table hash row that matches address list of loaded packages
#     #   for each row of new address list through for loop below
#     #  temporary list to hold shortest distances
#     address_list = find_address_list(package_list, package_info.pkg_tbl_hash)
#     # temporary table to hold address bidirectional graph
#     address_bidirectional_graph = []
#     for d in distance_table.dist_tbl_hash:
#         # print('d', d)
#         for a in address_list:
#             # print('a', a)
#             pid = a[0]
#             if d[0] is a[1]:
#                 # address_bidirectional_graph = [package id, address id, address string, distances tuples in asc order
#                 address_bidirectional_graph.append([pid, d])
#                 # print('address_bidirectional_graph:', address_bidirectional_graph)
#     # initiate and set a temporary list to hold each row on the address bidirectional graph
#     temp_miles_list = []
#     for i, a in enumerate(address_bidirectional_graph):
#         # b only has to elements so this does not affect performance very much
#         for b in a[1:]:
#             for c in b:
#                 #  skip first element which is address id
#                 if isinstance(c, tuple):
#                     temp_miles_list.append(c)
#             # sort by second element of each sublist of temp_miles_list
#             # reverse = None (Sorts in Ascending order)
#             # key is set to sort using second element of
#             # sublist lambda has been used
#             temp_miles_list.sort(key=lambda x: x[1])
#         # set current row in address_bidirectional_graph to nearest neighbors list
#         # temp_miles_list.insert(0, address_list[3])
#         address_bidirectional_graph[i] = temp_miles_list
#         address_bidirectional_graph[i].insert(0, 'p' + str(a[0]))
#         # set temp_miles_list to an empty list
#         temp_miles_list = []
#     # for each row in address list find closest matching address id of other packages on the truck
#     # for a in address_bidirectional_graph:
#     # temp_miles_list[0] = (address_id, miles)
#     # temp_miles_list[1], temp_miles_list[2]...temp_miles_list[n] = (closest_neighbor, miles to nearest neighbor)
#     temp_best_route = []
#     best_route = []
#     for j, nn in enumerate(address_bidirectional_graph, start=2):
#         print(nn)
#         temp_best_route.append(nn[2])
#     temp_best_route.sort(key=lambda x: x[1])
#     temp_best_route.reverse()
#     # circular route for truck going from HUB to closest -> max -> back to closest to HUB
#     for i, n in enumerate(temp_best_route):
#         # todo add package ids - 'pXX' => address_bidirectional_graph[0] - might be better to add at an earlier time
#         if i % 2 is 0:
#             best_route.append(n)
#             del n
#         if i % 2 is 1:
#             best_route.insert(0, n)
#             del n
#     # best_route = (package id, (address id, miles from current address to next address)
#     # todo drop packages with same address together
#     return best_route

def calculate_miles(route):
    miles_sum = 0
    for r in route:
        miles_sum = miles_sum + r[1]
    return miles_sum


# load special needs first
#   see lists in package info
# print(package_info.truck_one_only)
# print(package_info.truck_two_only)
# load truck
# print(package_info.truck_two_only)
# print(package_info.naked_packages)
load_truck(T2, package_info.truck_two_only)
load_truck(T2, package_info.naked_packages)
print(T2.all_package_info)
graph = build_graph(T2.all_package_info, package_info.pkg_tbl_hash, distance_table.dist_tbl_hash)
dijkstras_delivery_system(graph, 0)
# print(find_address_list(T2.all_package_info, package_info.pkg_tbl_hash))
# print(find_best_route(T2.all_package_info))
# find best route for trucks
# T2_best_route = find_best_route(T2.all_package_info)
# for r in T2_best_route:
#     print(r)
# print(calculate_miles(T2_best_route))
# deliver packages




