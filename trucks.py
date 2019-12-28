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

# todo
#   pop packages from ALL associated lists
#   get total mileage from all trucks

# initiate and set visited variable to an empty list
visited_locations = []
# initiate and set delivered packages list
delivered_packages = []
address_for_package_found = []
loaded_packages = []


class Truck:
    # init class
    def __init__(self, truck):
        # truck name
        self.name = truck
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
        self.mileage = 0

    def add_package(self, list_name, package_id):
        # find complete package information
        # check for full truck, if not full then add package_info to truck
        if self.number_of_packages < 16 and package_id not in self.all_package_info:
            self.number_of_packages += 1
            # append package to package info
            self.all_package_info.append(package_id)
            loaded_packages.append(package_id)
        # else the truck is full, set boolean full_truck to True
        elif self.full_truck is True:
            #  Truck is full. Fill next truck.
            print("Truck is full.")

    # function to load the trucks
    def load_truck(self, package_list):
        list_name = package_list[0]
        # check if truck is at the hub and has room
        if self.at_hub and self.full_truck is False:
            print('Truck,', self.name, 'is good to load package list:', list_name)
            print('Loading truck....')
            for package in package_list[1:]:
                if self.full_truck is True:
                    print("Truck is full. These packages remain: ", package_list)
                    break
                if isinstance(package, list) and self.full_truck is False:
                    self.add_package(list_name, package[0])
                else:
                    self.add_package(list_name, package)

    def route(self, start_vertex, package_list):
        # Put all vertices in an unvisited queue.
        unvisited_queue = []
        # vertex_id = g.sorted_bidirectional[start_vertex][0]
        # set package list to address list
        package_list = find_address_list(package_list, package_info.pkg_tbl_hash)
        print(package_list)
        # build a list of address ids to track unvisited package locations
        for vertex in g.sorted_bidirectional:
            for p in package_list:
                if p[1] == vertex[0]:
                    unvisited_queue.append(p[1])

        route = []
        miles = 0
        while len(unvisited_queue) > 1:
            """ 
            sorted_bidirectional's second element is a list of tuples with distances by location in ascending order
              elements 1 & 2 [vertex_id, 'address_string', ->
              element_2 SUBLIST (Adjacency list)   
                                [(vertex_id, miles from self), (closest_location_1, miles_from_vertex_id),
                                ...(closest_location_N, miles_from_vertex_id), (furthest_location, miles from vertex_id)]"""
            # Visit vertex with closest distance from current location
            # smallest index is also the next_vertex
            if start_vertex is 0:
                flag = False
                for vertex in g.sorted_bidirectional[start_vertex][2]:
                    for p in package_list:
                        if p[1] == vertex[0]:
                            package_id = p[0]
                            address_id = p[1]
                            # print('pkg list', package_list)
                            # print('if p adn v', g.sorted_bidirectional[start_vertex][2])
                            smallest_index = g.sorted_bidirectional[start_vertex][2][address_id][0]
                            self.mileage += g.sorted_bidirectional[start_vertex][2][address_id][1]
                            # print('round 1 miles', smallest_index, self.mileage)
                            # deliver package
                            delivered_packages.append(p[0])
                            flag = True
                            break
                    if flag:
                        break
                # print(smallest_index)
                route.append(unvisited_queue.pop(smallest_index))
                next_vertex = g.sorted_bidirectional[smallest_index][2]
                start_vertex = 1


            # next_vertex is the closest distance in the adjacency list
            #   it is the first occurence of a location that is still in the unvisited list
            #   the entire algorithm for location 0 -> 26 should return:
            #       0, 20, 21, 24, 26, 22, 17, 4, 16, 7, 13, 15, 18, 11, 5, 9, 2, 25, 19, 8, 12, 6, 1, 13, 14, 3, 23, 10

            # Check potential path lengths from the current vertex to all neighbors.
            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            # print('next miles', g.sorted_bidirectional[next_vertex][2])
            adj_vertex = smallest_index
            for vertex in next_vertex:
                if vertex[0] in unvisited_queue and vertex[0] != 0 and vertex[1] != 0.0:
                    adj_vertex = vertex[0]
                    edge_weight = vertex[1]
                    # print(next_vertex)
                    # print(adj_vertex, edge_weight)
                    self.mileage += edge_weight
                    # print(adj_vertex, edge_weight)
                    # alternative_path_distance = next_vertex + edge_weight
                    # print(vertex, alternative_path_distance)

                    # deliver package
                    for p in package_list:
                        if p[1] == adj_vertex:
                            package_list.remove(p)
                            delivered_packages.append(p[0])
                    break
            route.append(unvisited_queue.pop(unvisited_queue.index(adj_vertex)))
            next_vertex = g.sorted_bidirectional[adj_vertex][2]

        # go back to hub - use adjacency list which is just a list of the miles in order of location id
        # print(g.adjacency_list[0][adj_vertex])
        print('packages remaining', package_list)
        self.mileage += float(g.adjacency_list[0][adj_vertex])
        # print(route)
        # print(miles)
        return route



# create trucks
T1 = Truck('T1')
T2 = Truck('T2')
T3 = Truck('T3')


def find_address_list(packages_list, address_list):
    temp_list = []
    # find address id for package
    #  if package id == package address id
    # todo why are the packages at certain locations not delivered
    #  the delivered packages do not match up with the remaining packages list
    for a in address_list:
        # print('a', a)
        # find address id and save it to a variable
        for d in g.sorted_bidirectional:
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
                    if p[0] not in address_for_package_found:
                        address_for_package_found.append(int(p[0]))
            if type(p) == int:
                # print('int')
                # print('ptype', type(p))
                # print('a', a)
                if a[0] is p:
                    temp_list.append([a[0], address_id, a[1]])
                    if p not in address_for_package_found:
                        address_for_package_found.append(int(p))



    # todo group packages into bucket list by location:
    # grouped_by_address = []
    #
    # for i, p in enumerate(temp_list):
    #     # print('address for package found', address_for_package_found)
    #     # print('p', p)
    #     for a in p:
    #         if a in address_for_package_found:
    #             grouped_by_address.append(a)
    #             address_for_package_found.remove(int(a))
    #             break
    #     grouped_by_address.append(1)
    #     # print('temp list', temp_list)
    #     # print('grouped', grouped_by_address)
    return temp_list


# load trucks
"""
List names from package_info:
# priority 1
packages_with_delivery_deadlines = ["Delivery Deadlines"]
delayed_flight = ["Delayed Flights"]
truck_one_only = ["Load on this Truck one only"]
truck_two_only = ["Load on this Truck two only"]
truck_three_only = ["Load on this Truck two only"]

# priority 2
wrong_address = ["Wrong Address"]

# priority 3
packages_without_delivery_deadlines = ["No Delivery Deadline"]
naked_packages = ["No Special Needs"]

# list of packages with special notes
packages_with_special_notes = ["Special Notes"]


# separate lists for packages with special notes
delayed_flight = ["Delayed Flights"]
truck_one_only = ["Load on this Truck one only"]
truck_two_only = ["Load on this Truck two only"]
truck_three_only = ["Load on this Truck two only"]
wrong_address = ["Wrong Address"]
"""
# Truck 1
T1.load_truck(package_info.truck_one_only) # 0 packages
T1.load_truck(package_info.packages_with_delivery_deadlines) # 14 packages
T1.load_truck(package_info.naked_packages) # until full
print('find route 1', T1.route(0, T1.all_package_info))


# Truck 2
T2.load_truck((package_info.truck_two_only)) # 4 packages - 2, 18, 36, 38
T2.load_truck(package_info.delayed_flight) # 4 packages - 6, 25, 28, 32
T2.load_truck(package_info.wrong_address) # 1 package - 9
T2.load_truck(package_info.naked_packages) # until full
print('find route 2', T2.route(0, T2.all_package_info))


# Truck 3
T3.load_truck(package_info.naked_packages)
T3.load_truck(package_info.packages_without_delivery_deadlines)
print('find route 3', T3.route(0, T3.all_package_info))

# total miles for all 3 trucks
total_miles = T1.mileage + T2.mileage + T3.mileage
print('total', total_miles)

# check for any missed packages
temp_list = []
for i in range(40):
    if i not in delivered_packages:
        temp_list.append(i + 1)
print('t', temp_list)

loaded_packages.sort()
print('loaded', loaded_packages)
address_for_package_found.sort()
print('address list from find_address()', address_for_package_found)
T3.load_truck(temp_list)

temp_list = []
for i in range(40):
    if i not in delivered_packages:
        temp_list.append(i + 1)
print('t', temp_list)

# check = [package_info.packages_with_delivery_deadlines, package_info.packages_without_delivery_deadlines, package_info.truck_two_only,
#          package_info.wrong_address, package_info.naked_packages, package_info.delayed_flight, package_info.delivery_deadline]


# load special needs first
#   see lists in package info
# print(package_info.truck_one_only)
# print(package_info.truck_two_only)
# load truck
# print(package_info.truck_two_only)
# print(package_info.naked_packages)
# load_truck(T2, package_info.truck_two_only)
# load_truck(T2, package_info.naked_packages)
# print(T2.all_package_info)
# graph = build_graph(T2.all_package_info, package_info.pkg_tbl_hash, g.bidirectional)
# dijkstras_delivery_system(graph, 0)
# print(find_address_list(T2.all_package_info, package_info.pkg_tbl_hash))
# print(find_best_route(T2.all_package_info))
# find best route for trucks
# T2_best_route = find_best_route(T2.all_package_info)
# for r in T2_best_route:
#     print(r)
# print(calculate_miles(T2_best_route))
# deliver packages









#####################
#    TEST AREA      #
#####################
# def find_route(self, current_location):
#     """
#     dist_from_hub[1:26]
#     n = len(truck_package_list)
#     truck_package_list[0:n]
#     package_address_list[0:n]
#
#     find fist package from truck_package_list that is in dist_from_hub
#         curr_location = truck_package_list[curr_index]
#         break
#
#     find next_location and append it to best_route
#
#     todo if packages have the same address drop them both off - HEURISTIC
#     """
#     best_route = []
#     c = g.distances_from_hub
#     p = self.all_package_info
#     length = len(p)
#     a = find_address_list(p, package_info.pkg_tbl_hash)
#     # print(h)
#     # print(p)
#     # print(a)
#     if p:
#         i = 0
#         while i < length:
#             if i == 0:
#                 found_closest_location = False
#                 for address_id in c:
#                     for paid in a:
#                         # print(paid)
#                         hub_address_id = address_id[0]
#                         # print('hub', hub_address_id)
#                         package_address_id = paid[1]
#                         # print('package add id', package_address_id)
#                         if hub_address_id == package_address_id:
#                             # print('match1')
#                             current_location = package_address_id
#                             # print(current_location)
#                             best_route.append(('0 to', current_location, address_id[1]))
#                             self.mileage += address_id[1]
#                             c = g.bidirectional[current_location]
#                             found_closest_location = True
#                             break
#                         if found_closest_location:
#                             break
#                     if found_closest_location:
#                         break
#                 i = i + 1
#             else:
#                 j = 0
#                 while j < len(a):
#                     for paid in a:
#                         for address_id in c[2]:
#                             next_location = address_id[0]
#                             # print('hub', current_location)
#                             # print('hub', next_location)
#                             package_address_id = paid[1]
#                             if next_location == package_address_id and address_id[1] != 0.0:
#                                 if paid[0] in p and paid[0] not in delivered_packages:
#                                     if address_id[1] > 7.0:
#                                         # print('greater than 1.0')
#                                         # using append() + pop() + index()
#                                         # moving element to end
#                                         a.append(a.pop(a.index(paid)))
#                                         if address_id[1] > 3.0:
#                                             # print('greater than 4.0')
#                                             a.append(a.pop(a.index(paid)))
#                                             if address_id[1] > 1.01:
#                                                 # print('greater than 7.0')
#                                                 a.append(a.pop(a.index(paid)))
#                                                 if address_id[1] > 1.0:
#                                                     print('g than 11', address_id)
#                                                     self.all_package_info.pop(self.all_package_info.index(paid[0]))
#                                                     break
#                                     best_route.append((paid[0], current_location, 'to', next_location, address_id[1]))
#                                     current_location = next_location
#                                     c = g.bidirectional[next_location]
#                                     delivered_packages.append(paid[0])
#                                     self.mileage += address_id[1]
#                                     print(self.mileage)
#                                     # remove package from p
#                                     if paid[0] in self.all_package_info:
#                                         self.all_package_info.remove(paid[0])
#                         p = self.all_package_info
#                         a = find_address_list(p, package_info.pkg_tbl_hash)
#                     j = j + 1
#                 j = 0
#                 i = i + 1
#                 # print('index', i)
#         delivered_packages.sort()
#         print('del pkg', delivered_packages)
#         return best_route
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
# def build_graph(packages_on_truck_list, master_packages_list, master_distance_list):
#     # print('pon', packages_on_truck_list)
#     # print('mpl', master_packages_list)
#     # print('mdl', master_distance_list)
#     # get package id, address id, street address
#     address_list = find_address_list(packages_on_truck_list, master_packages_list)
#     print(address_list)
#     master_graph = []
#     # best_route = []
#     # all distances
#     for d in master_distance_list:
#         # print('d', d)
#         # temporary graph to hold each row to be appended to graph
#         temp_graph = []
#         # for each element in all distances append only the mileage
#         for el in d[2:][0]:
#             # get only the distances you need from package list
#             for a in address_list:
#                 # if distance table number is address id then append mileage to temp_graph
#                 if el[0] == a[1]:
#                     temp_graph.append(el)
#                     package_id = int(a[0])
#                     address_id = a[1]
#         # append temp_graph as a row in graph
#         temp_graph.insert(0, [package_id, address_id])
#         master_graph.append(temp_graph)
#     return master_graph


# # Python3 program to implement traveling salesman
# # problem using naive approach.
# maxsize = float('inf')
# V = 16
#
# # implementation of traveling Salesman Problem
# def dijkstras_delivery_system(graph, s):
#     print('calculating....')
#     print('g', graph)
#     print('This graph is already sorted in asc order but you need to know the address ids LOL')
#     # store all vertex apart from source vertex
#     vertex = []
#     for i in range(V):
#         if i != s:
#             vertex.append(i)
#
#     # store minimum weight Hamiltonian Cycle
#     min_path = maxsize
#
#     while True:
#
#         # store current Path weight(cost)
#         current_pathweight = 0
#
#         # compute current path weight
#         k = s
#         for i in range(len(vertex)):
#             # print('graph k', graph)
#             current_pathweight += graph[k][vertex[i]]
#             k = vertex[i]
#         current_pathweight += graph[k][s]
#
#         # update minimum
#         min_path = min(min_path, current_pathweight)
#         # HEURISTIC:
#         # Get the current processor time in seconds using time.process_time() method
#         # the larger the value the longer the process will take
#         # and the more accurate (shorter miles) the algorithm will be
#         # most people are willing to wait 3 seconds for an answer, so I chose 3 as my max wait time value
#         max_wait_time = 3
#         process_time = time.process_time()
#         if not next_permutation(vertex) or process_time > max_wait_time:
#             break
#     print(min_path, vertex)
#     return min_path
#
#
# # next_permutation implementation
# def next_permutation(L):
#     n = len(L)
#
#     i = n - 2
#     while i >= 0 and L[i] >= L[i + 1]:
#         i -= 1
#
#     if i == -1:
#         return False
#
#     j = i + 1
#     while j < n and L[j] > L[i]:
#         j += 1
#     j -= 1
#
#     L[i], L[j] = L[j], L[i]
#
#     left = i + 1
#     right = n - 1
#
#     while left < right:
#         L[left], L[right] = L[right], L[left]
#         left += 1
#         right -= 1
#
#     return True


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





