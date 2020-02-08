# Vera Butler #000929765
"""
TRUCK CLASS ASSUMPTIONS

Trucks have a “infinite amount of gas” with no need to stop.
The package ID is unique; there are no collisions.
Delivery time is instantaneous, i.e., no time passes while at a delivery
    (that time is factored into the average speed of the trucks).
No further assumptions exist or are allowed.
The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m.
    The correct address is 410 S State St., Salt Lake City, UT 84111.
"""

# imports
import package_info
from graph import g
import math


"""
SET GLOBAL EMPTY LISTS delivered_packages, address_for_packages_found, loaded_packages
    *These lists need to be global so that all Trucks can access them throughout the software solution
"""
delivered_packages = []
address_for_package_found = []
loaded_packages = []


# SET number_of_drivers = 2
drivers = [1, 1]


def check_driver_count():
    if len(drivers) == 0:
        return False
    else:
        return True


class Truck:
    """
    :method: set_delivery_time
        :return: STRING X:XX AM/PM

    :method: set_load_time
        SET self.load_time
        :return: VOID

    :method: add_package
        APPEND package object memory location TO LIST self.all_package_info
        :return: VOID

    :method: load_truck
        SET package object delivery_status IN :param: package_list TO 'in route'
        SET package object on_truck IN :param: package_list TO self.name
        SORT packages IN LIST :param: package_list

    :method: deliver_package
        APPEND package_id TO LIST delivered_packages
        SET package.delivery_status = 'delivered'
        REMOVE package_id FROM LIST master_package_id_list
        SET package.delivery_time
        SET package_delivery_time
        CHECK IF package IS delivered on time

    :method: route
        CHECK for available drivers AND DISABLE 1 driver
        CHECK for empty package list: if TRUE RETURN

        O(N)
        SET EACH package IN :param: package_list TO 'in route'

        FIND addresses for packages IN :param: package_list
        APPEND EACH package_id TO LIST unvisited_queue

        FIND the best route
        ENABLE 1 driver
        :return: best route
    """
    # init class with data members
    # O(1)
    def __init__(self, truck):


        # update this list when new trucks are added to the route
        truck_ids_list = ['T1', 'T2', 'T3']

        # self.name should be limited to the list truck ids
        if truck in truck_ids_list:
            self.name = truck
        else:
            print("Invalid truck ID. Please enter T1, T2, or T3 or update the truck_ids_list in the Truck class.")

        # Track the number of packages on each truck
        self.number_of_packages = 0

        # Maximum number of packages allowed on each Truck is 16
        self.max_packages = 16

        # Trucks travel at an average speed of 18 miles per hour.
        self.average_speed = float(18)

        # Each driver stays with the same truck as long as that truck is in service.
        self.driver = 0

        # Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
        # The day ends when all 40 packages have been delivered.
        self.time = 8

        # There is up to one special note for each package.
        self.package_notes = 'No notes.'

        # track the distance driven
        self.distance = float(0)

        # Package list to hold package ids on the truck
        self.all_package_info = []

        # Boolean to track if truck is at the hub or en route
        self.at_hub = True

        # Boole to track the trucks max capacity of 16 packages
        self.full_truck = False

        # mileage and time need to be tracked in order to update package_info.load_time, package_info.delivery_time,
        # and package_info.delivery_status
        self.mileage = 0
        self.leave_time_hour = 8
        self.leave_time_minutes = 0
        self.hours = 0
        self.hours_str = ''
        self.minutes = 0
        self.minutes_str = ''
        self.delivery_time = 0

    # O(1)
    def set_delivery_time(self, miles):
        # calculate the time based on 18 miles per hour - O(1)
        frac, whole = math.modf(miles / self.average_speed)
        self.hours = round(whole) + self.leave_time_hour
        self.minutes = round(frac * 60) + self.leave_time_minutes

        # IF self.minutes > 60 THEN subtract 60
        if self.minutes > 60:
            self.minutes = self.minutes - 60

        # add zero for single digit minutes
        if len(str(self.minutes)) < 2:
            self.minutes = '0' + str(self.minutes)

        if self.hours > 11:
            meridies = ' PM'
        else:
            meridies = ' AM'

        self.delivery_time = str(self.hours) + ':' + str(self.minutes) + meridies

        return self.delivery_time

    # O(1)
    def set_load_time(self):
        leave_time_minutes = self.leave_time_minutes
        # add zero for single digit minutes
        if len(str(leave_time_minutes)) < 2:
            leave_time_minutes = '0' + str(self.leave_time_minutes)

        if self.hours > 11:
            meridies = ' PM'
        else:
            meridies = ' AM'

        return str(self.leave_time_hour) + ':' + str(leave_time_minutes) + meridies

    #
    def add_package(self, package_id):
        # find complete package information
        # check for full truck, if not full then add package_info to truck
        # O(N + N)
        if self.number_of_packages < self.max_packages and package_id not in self.all_package_info:
            self.number_of_packages += 1

            # pop package from master package list

            if package_id in package_info.master_package_id_list:
                package_index = package_id - 1
                package_memory_address = package_info.master_package_list[package_index]
                # set loaded_on_truck for package
                package_memory_address.loaded_on_truck = self.name
                # append package to package info
                self.all_package_info.append(package_memory_address)
                loaded_packages.append(package_id)
                # package_info.master_package_id_list.remove(package_id)
        else:
            self.full_truck = True
        # else the truck is full, set boolean full_truck to True
        if self.full_truck is True:
            #  Truck is full. Fill next truck.
            print("Truck is full.")

    # O(N)(N) => O(N^2)
    def load_truck(self, package_list):
        if package_list:
            # check if truck is at the hub and has room
            if self.at_hub and self.full_truck is False:
                print('Loading truck....', self.name)

                for package in package_list[1:]:
                    if self.full_truck is True:
                        return
                    else:
                        if isinstance(package, list):
                            package_id = package[0]
                            # O(N)
                            if package_id in package_info.master_package_id_list:
                                self.add_package(package_id)
                        else:
                            package_id = package
                            # O(N)
                            if package_id in package_info.master_package_id_list:
                                self.add_package(package_id)
    # O(N)
    def deliver_package(self, package):
        delivered_packages.append(package.package_id_number)
        package.delivery_status = 'delivered'
        # O(N)
        package_info.master_package_id_list.remove(package.package_id_number)
        package.delivery_time = self.set_delivery_time(self.mileage)
        if package.delivery_status == 'delivered':
            package.delivery_time = self.set_delivery_time(self.mileage)
            if package_info.is_package_on_time(package, package.delivery_time) is False:
                print("Package", package.package_id_number, "was delivered late.")
            else:
                print("Package", package.package_id_number, "was delivered on time.")

    # # O(N^6logN)
    def route(self, start_vertex, package_list):

        if check_driver_count() is True:
            self.driver = 1
            drivers.pop()
        else:
            print("No available drivers.")
            return

        # if the package_list parameter is empty return
        if not package_list:
            return

        # set all packages in the list delivery status to 'en route'
        # O(N)
        for p in package_list:
            p.delivery_status = 'en route'
            p.load_time = self.set_load_time()

        # track unvisited locations
        unvisited_queue = []
        # set package list to address list
        package_list = find_address_list(package_list)
        # build a list of address ids to track unvisited package locations
        # O(N^2)
        for p in package_list:
            package_location = p[0]
            if package_location not in unvisited_queue:
                unvisited_queue.append(package_location)

        route = []
        address_id = 0
        # O(N^5log^2N)
        while len(unvisited_queue) > 0:
            # Visit vertex with closest distance from current location
            # smallest index is also the next_vertex
            hub = g.sorted_bidirectional[0]
            if start_vertex is 0:
                route.append(0)
                flag = False
                # O(N)
                for vertex in hub:
                    # O(N)
                    for p in package_list:
                        if p[0] == vertex[0]:
                            packages = p[2:]
                            address_id = p[0]
                            miles = vertex[1]
                            self.mileage += miles
                            # add time of delivery for truck and package
                            # deliver package
                            # O(1) - because of break statement
                            # https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
                            for package in packages:
                                # O(N)
                                if package.package_id_number in package_info.master_package_id_list:
                                    self.deliver_package(package)
                            flag = True
                            break
                    if flag:
                        break
                # O(N)
                unvisited_queue.remove(address_id)
                route.append(address_id)
                next_vertex = g.sorted_bidirectional[address_id]
                start_vertex = 1

            # next_vertex is the closest distance in the sorted adjacency list
            #   it is the first occurrence of a location that is still in the unvisited list
            #   the entire route algorithm for location 0 -> 26 should return:
            #       0, 20, 21, 24, 26, 22, 17, 4, 16, 7, 13, 15, 18, 11, 5, 9, 2, 25, 19, 8, 12, 6, 1, 13, 14, 3, 23, 10

            # O(N^5log^2N)
            for vertex in next_vertex[1:]:
                vertex_id = vertex[0]
                # O(N) where N <= 16
                if vertex_id in unvisited_queue:
                    adj_vertex = vertex_id
                    miles = vertex[1]
                    self.mileage += miles
                    # deliver package
                    # O(logN) where N <= 16
                    for p in package_list:
                        if p[0] == adj_vertex:
                            packages_with_same_address = p[2:]
                            # O(N) where N <= 5
                            for package in packages_with_same_address:
                                # O(N) where N <= all_packages
                                if package.package_id_number in package_info.master_package_id_list:
                                    # O(N)
                                    self.deliver_package(package)
                            # O(N)
                            package_list.remove(p)
                    route.append(unvisited_queue.pop(unvisited_queue.index(adj_vertex)))
                    next_vertex = g.sorted_bidirectional[adj_vertex]
                    break



        # go back to hub - use adjacency list which is just a list of the miles in order of location id
        # O(1)
        hub = g.adjacency_list
        last_index_in_route = route[-1]
        miles_back_to_hub = hub[last_index_in_route][0]
        self.mileage += miles_back_to_hub
        route.append(0)
        self.delivery_time = self.set_delivery_time(self.mileage)

        self.driver = 0

        # return driver to hub
        drivers.append(1)

        return route

# O(N^5)
def find_address_list(packages_list):
    """
         // list of package address in memory
         SET EMPTY LIST address_bucket_list

         // check if package list exists
O(1)    IF BOOLEAN packages_list IS NOT EMPTY:

            ////////// START TOP LEVEL LOOP //////////
            // create a list to hold all memory addresses of packages associated with each package in the package list
            // argument and a list to hold all package ids associated with packages in the package list argument
O(3N+1)     FOR EACH ADDRESS package IN LIST packages_list:
                    SET INT package_id == INT package.package_id_number

                    APPEND ADDRESS package TO LIST address_bucket_list
                    APPEND INT package_id TO LIST address_for_package_found
                END FOR
            ////////// END TOP LEVEL LOOP //////////

             ////////// START TOP LEVEL LOOP //////////
             //list for boolean use to enforce unique data entries
             SET EMPTY LIST same_delivery_address
             // list for boolean use to flag that a package has been found and no packages are missed
             SET EMPTY LIST found_package_list

O(3N+2)     FOR EACH ADDRESS package IN LIST address_bucket_list

                // set and initialize variables street_address, address_id, package_id to associated package information
                SET STRING street_address = STRING package.delivery_address
                SET INT address_id = INT package.address_id
                SET INT package_id = INT package.package_id_number

                // check if the address_id and street_address variables are not in same_delivery_address list then then
                // build the same_delivery_address and found_packages lists
O(3N+2)(N)      IF LIST [address_id, street_address] IS NOT IN LIST same_delivery_address
                    APPEND LIST [address_id, street_address] TO LIST same_delivery_address

O(3N+2)(N)(N^3)     FOR LIST s IN same_delivery_address

O(1)                IF s[1] == street_address
O(N)                    SET INT index == INDEX OF same_delivery_address
O(2N)                   IF INT package_id IS NOT IN LIST found_package_list:
                            APPEND INT package_id TO LIST found_package_list
O(N)                        INSERT MEMORY ADDRESS package TO same_delivery_address AT INDEX index
                        END IF
                    END IF
                    END FOR
                END IF
            END FOR
            ////////// END TOP LEVEL LOOP //////////

        RETURN same_delivery_address
------------------------------------------------------------------------------------------------------------------------
BIG O Total => O(N) => O(N^5) This is acceptable because all the lists are limited by the load capacity of the truck
                              and the length of the street address (N < 50).
                              Even if in the future trucks could hold 500 packages and the trucks delivered to
                              500 locations it would not cause the run time to reach more than seconds.
    """

    # list to hold package addresses in memory from CLASS PACKAGE
    package_addresses = []

    # check if package_list exists
    if packages_list:

        # limit N to load capacity by creating a list to hold all memory addresses of only the packages in the package list
        # O(N); N = load capacity
        for p in packages_list:
            package_id = p.package_id_number
            package_addresses.append(p)
            address_for_package_found.append(package_id)

    # group packages into bucket list by locations
    # find packages with the same delivery address
    same_delivery_address = []
    found_package_list = []
    # O(N); N = load capacity
    for p in package_addresses:
        street_address = p.delivery_address
        address_id = p.address_id
        package_id = p.package_id_number
        # O(N)(N); ALL N <= load capacity
        if [address_id, street_address] not in same_delivery_address:
            same_delivery_address.append([address_id, street_address, p])
        # O(N)(N); load capacity
        for s in same_delivery_address:
            if s[1] == street_address:
                # O(N)(N)(N)
                index = same_delivery_address.index(s)
                # O(N)(N)(N)(N); ALL N <= load capacity
                if package_id not in found_package_list:
                    found_package_list.append(package_id)
            # O(N)(N)(N)(N); ALL N <= load capacity
            if p not in same_delivery_address[index]:
                same_delivery_address[index].append(p)
    return same_delivery_address


"""
TRUCKS

PRIORITY LISTS
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

"""
TRUCK 1

Load Truck 1 first with lists:
truck_one_only - not used for requirements of this program but exists for scalability 
packages_with_delivery_deadlines - load first because they are top priority
naked_packages - load last to fill the truck to max capacity

THEN find the route with the list T1.all_packages_info
     this list includes all package ids associated with previously loaded packages above

THEN SET the delivery_time for T1

"""

T1 = Truck('T1')
T1.load_truck(package_info.truck_one_only)  # 0 packages
T1.load_truck(package_info.packages_with_delivery_deadlines)  # 14 packages
T1.load_truck(package_info.naked_packages)  # until full
T1.route(0, T1.all_package_info)
T1.set_delivery_time(T1.mileage)

"""
TRUCK 2
Truck 2 shares a driver with Truck 1 and must wait for Truck 1 to return from deliveries
    Truck 2 is set to leave at the time T1 returns (10:27)
"""
T2 = Truck('T2')
T2.leave_time_hour = T1.hours
T2.leave_time_minutes = T1.minutes

"""
TRUCK 3 
- delivers all remaining packages after Truck 1 and Truck 2 are loaded
- leaves the hub at 8:00 AM
- uses master package list to make sure no packages are missed during loading
"""

# Truck 3
T3 = Truck('T3')
T3.load_truck(package_info.packages_with_delivery_deadlines)
T3.load_truck(package_info.grouped_deliveries)
T3.load_truck(package_info.naked_packages)
T3.load_truck(package_info.packages_without_delivery_deadlines)
T3.route(0, T3.all_package_info)
T3.set_delivery_time(T3.mileage)  # set self.delivery_time to calculated delivery time

"""
Truck 2 is used to deliver delayed packages and #9 with the wrong address because it leaves after the address is reset
The wrong delivery address for package #9, 
Third District Juvenile Court, will be corrected at 10:20 a.m. 
The correct address is 410 S State St., Salt Lake City, UT 84111.
"""

# check for missed packages and add them back to the master_package_id_list
undelivered_packages = package_info.master_package_id_list
undelivered_packages.insert(0, "undelivered")

# SET package #9 to new address; truck leaves after 10:20 AM so this correction takes place at the appropriate time
package_info.master_package_list[8].delivery_address = '410 S State St'
package_info.master_package_list[8].address_id = 19
T2.leave_time_minutes = T1.minutes
T2.load_truck(undelivered_packages)  # make sure no packages were missed
# T2.load_truck(['wrong', 9])  # 1 package - 9
T2.route(0, T2.all_package_info)
T2.set_delivery_time(T2.mileage)  # set self.delivery_time to calculated delivery time

# PRINT the total miles for all 3 trucks
total_miles = T1.mileage + T2.mileage + T3.mileage
print('Total Mileage for All 3 Trucks:', total_miles)

# PRINT a list of delivered packages in ascending order
delivered_packages.sort()
print('Delivered Packages:', delivered_packages)

if len(delivered_packages) == len(package_info.master_package_list):
    print("All packages were delivered.")
else:
    for p in package_info.master_package_list:
        if p.package_id_number not in delivered_packages:
            print("Undelivered:", p.package_id_number)



