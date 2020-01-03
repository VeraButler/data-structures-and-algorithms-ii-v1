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
import math

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

        # delivery times
        self.mileage = 0
        self.leave_time_hour = 8
        self.leave_time_minutes = 0
        self.hours = 0
        self.hours_str = ''
        self.minutes = 0
        self.minutes_str = ''
        self.delivery_time = 0

    # time to get to location (18mi/hr)
    #  todo fix me
    def add_to_delivery_time(self, miles):

        # calculate time
        frac, whole = math.modf(miles / 18)
        self.hours = round(whole) + self.leave_time_hour
        self.minutes = round(frac * 60) + self.leave_time_minutes

        # add zero for single digit minutes
        if len(str(self.minutes)) < 2:
            self.minutes = '0' + str(self.minutes)

        # set meridies
        if self.hours > 11:
            meridies = ' PM'
        else:
            meridies = ' AM'

        self.delivery_time = str(self.hours) + ':' + str(self.minutes) + meridies
        return self.delivery_time

    def add_package(self, package_id):
        # find complete package information
        # check for full truck, if not full then add package_info to truck
        if self.number_of_packages < 16 and package_id not in self.all_package_info:
            self.number_of_packages += 1
            # pop package from master package list
            if package_id in package_info.master_package_id_list:
                package_index = package_id - 1
                package_memory_address = package_info.master_package_list[package_index]
                # append package to package info
                self.all_package_info.append(package_memory_address)
                loaded_packages.append(package_id)
                package_info.master_package_id_list.remove(package_id)
        else:
            self.full_truck = True
        # else the truck is full, set boolean full_truck to True
        if self.full_truck is True:
            #  Truck is full. Fill next truck.
            print("Truck is full.")

    # function to load the trucks
    def load_truck(self, package_list):
        if package_list:
            list_name = package_list[0]
            # check if truck is at the hub and has room
            if self.at_hub and self.full_truck is False:
                print('Truck,', self.name, 'is good to load package list:', list_name)
                print('Loading truck....')

                for package in package_list[1:]:
                    if self.full_truck is True:
                        return
                    if isinstance(package, list) and self.full_truck is False:
                        package_id = package[0]
                        if package_id in package_info.master_package_id_list:
                            self.add_package(package_id)
                            package_list.remove(package)
                    else:
                        package_id = package
                        if package_id in package_info.master_package_id_list:
                            self.add_package(package_id)

    def route(self, start_vertex, package_list):
        if not package_list:
            return
        # set all packages in the list delivery status to 'en route'
        for p in package_list:
            p.delivery_status = 'en route'
        # Put all vertices in an unvisited queue.
        unvisited_queue = []
        # vertex_id = g.sorted_bidirectional[start_vertex][0]
        # set package list to address list
        package_list = find_address_list(package_list)
        # build a list of address ids to track unvisited package locations
        for vertex in g.sorted_bidirectional:
            for p in package_list:
                if p[0] == vertex[0] and p[0] not in unvisited_queue:
                    unvisited_queue.append(p[0])

        route = []
        while len(unvisited_queue) > 0:
            """ 
            sorted_bidirectional's second element is a list of tuples with distances by location in ascending order
              elements 1 & 2 [vertex_id, 'address_string', ->
              element_2 SUBLIST (Adjacency list)   
                                [(vertex_id, miles from self), (closest_location_1, miles_from_vertex_id),
                                ...(closest_location_N, miles_from_vertex_id), (furthest_location, miles from vertex_id)]"""
            # Visit vertex with closest distance from current location
            # smallest index is also the next_vertex
            hub = g.sorted_bidirectional[0][2]
            if start_vertex is 0:
                # # look for packages with high priority
                # for p in package_list:
                #     for q in p[2:]:
                #         if q.delivery_deadline == '9:00 AM':
                #             route.append(q.address_id)
                route.append(0)
                flag = False
                for vertex in hub:
                    for p in package_list:
                        if p[0] == vertex[0]:
                            address_id = p[0]
                            miles = vertex[1]
                            smallest_index = address_id
                            self.mileage += miles
                            # add time of delivery for truck and package
                            # deliver package
                            delivered_packages.append(p[2].package_id_number)
                            p[2].delivery_status = 'delivered'
                            flag = True
                            if p[2].delivery_status is 'delivered':
                                p[2].delivery_time = self.add_to_delivery_time(self.mileage)
                            break
                    if flag:
                        break
                unvisited_queue.remove(address_id)
                route.append(address_id)
                next_vertex = g.sorted_bidirectional[address_id][2]
                start_vertex = 1


            # next_vertex is the closest distance in the adjacency list
            #   it is the first occurence of a location that is still in the unvisited list
            #   the entire algorithm for location 0 -> 26 should return:
            #       0, 20, 21, 24, 26, 22, 17, 4, 16, 7, 13, 15, 18, 11, 5, 9, 2, 25, 19, 8, 12, 6, 1, 13, 14, 3, 23, 10

            # Check potential path lengths from the current vertex to all neighbors.
            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            # print('next miles', g.sorted_bidirectional[next_vertex][2])
            for vertex in next_vertex:
                if vertex[0] in unvisited_queue and vertex[0] != 0 and vertex[1] != 0.0:
                    # print('adj vertex', vertex)
                    adj_vertex = vertex[0]
                    miles = vertex[1]
                    # print(next_vertex)
                    # print(adj_vertex, edge_weight)
                    self.mileage += float(miles)
                    # deliver package
                    for p in package_list:
                        if p[0] == adj_vertex:
                            for package in p[2:]:
                                delivered_packages.append(package.package_id_number)
                                package.delivery_status = 'delivered'
                                if p[2].delivery_status is 'delivered':
                                    p[2].delivery_time = self.add_to_delivery_time(self.mileage)
                            package_list.remove(p)
                    break
            route.append(unvisited_queue.pop(unvisited_queue.index(adj_vertex)))
            next_vertex = g.sorted_bidirectional[adj_vertex][2]

        # go back to hub - use adjacency list which is just a list of the miles in order of location id
        for vertex in hub:
            location_id = vertex[0]
            miles_for_current_vertex = float(vertex[1])
            last_index_in_route = route[-1]
            if location_id == last_index_in_route:
                self.mileage += float(miles_for_current_vertex)
                route.append(0)
        self.delivery_time = self.add_to_delivery_time(self.mileage)
        return route


# create trucks
T1 = Truck('T1')
T2 = Truck('T2')
T3 = Truck('T3')


def find_address_list(packages_list):
    address_bucket_list = []
    # find address id for package
    if packages_list:
        for p in packages_list:
            package_id = p.package_id_number
            address_id = p.address_id
            street_address = p.delivery_address
            # a[0] is address id from master address list
            # a[1] is the address string 'XXX street street_address' correlated with the address id
            address_bucket_list.append(p)
            address_for_package_found.append(package_id)

    # group packages into bucket list by locations
    # find packages with the same delivery address
    same_delivery_address = []
    found_package_list = []
    for p in address_bucket_list:
        street_address = p.delivery_address
        address_id = p.address_id
        package_id = p.package_id_number
        if [address_id, street_address] not in same_delivery_address:
            same_delivery_address.append([address_id, street_address])
        for s in same_delivery_address:
            if s[1] == street_address:
                index = same_delivery_address.index(s)
                if package_id not in found_package_list:
                    found_package_list.append(package_id)
                    same_delivery_address[index].append(p)
    # for s in same_delivery_address:
    #     print('same', s)
    return same_delivery_address


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
print(T1.add_to_delivery_time(T1.mileage))

# Truck 2
"""
This truck is used to deliver delayed packages and #9 with the wrong address

Set truck to leave at 9:05
"""
T2.leave_time_hour = 9
T2.leave_time_minutes = 5
T2.load_truck((package_info.truck_two_only)) # 4 packages - 2, 18, 36, 38
T2.load_truck(package_info.delayed_flight) # 4 packages - 6, 25, 28, 32
T2.load_truck(package_info.wrong_address) # 1 package - 9
# T2.load_truck(package_info.master_package_id_list)
print('find route 2', T2.route(0, T2.all_package_info))
print(T2.mileage)
print(T2.add_to_delivery_time(T2.mileage))


# Truck 3
T3.load_truck(package_info.naked_packages)
T3.load_truck(package_info.packages_without_delivery_deadlines)
T3.load_truck(package_info.packages_with_delivery_deadlines)
print('find route 3', T3.route(0, T3.all_package_info))
print(T3.add_to_delivery_time(T3.mileage))

# total miles for all 3 trucks
total_miles = T1.mileage + T2.mileage + T3.mileage
print('total', total_miles)

# delivered packages
delivered_packages.sort()
print(delivered_packages)







