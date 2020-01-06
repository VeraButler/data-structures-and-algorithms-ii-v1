"""
TRUCK CLASS ASSUMPTIONS

Trucks have a “infinite amount of gas” with no need to stop.
The package ID is unique; there are no collisions.
Delivery time is instantaneous, i.e., no time passes while at a delivery
    (that time is factored into the average speed of the trucks).
No further assumptions exist or are allowed.
The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m.
    The correct address is 410 S State St., Salt Lake City, UT 84111.
--------------------------------------------------------------------------------------------------------
PART B
B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
B.2 Apply programming models to the scenario.
        The application of programming models includes the communication protocol that is used to exchange data;
        the target host environment used to host the server application program; and the interaction semantics defined
        by the application to control connect, data exchange, and disconnect sequences.
B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
B.5 Discuss the efficiency and maintainability of the software.
B.6 Discuss the self-adjusting data structures chosen and their strengths and weaknesses based on the scenario.
"""

# imports
import package_info
from graph import g
import math

"""
B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
        SET GLOBAL EMPTY LISTS delivered_packages, address_for_packages_found, loaded_packages
            *These lists need to be global so that all Trucks can access them throughout the software solution
"""
delivered_packages = []
address_for_package_found = []
loaded_packages = []


class Truck:
    # init class
    def __init__(self, truck):
        # truck name
        self.name = truck
        # SET self.number_of_packages = 0
        self.number_of_packages = 0
        # Maximum number of packages allowed on each Truck is 16
        # SET max_packages = 16
        self.max_packages = 16
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

    def set_delivery_time(self, miles):
        """
        B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
                SET FLOAT frac, whole = PYTHON BUILT IN FUNCTION math.modf(miles / self.average_speed)
                SET FLOAT self.hours = INT ROUND(whole) + INT self.leave_time_hour
                SET FLOAT self.minutes = INT round(frac * 60) + INT self.leave_time_minutes

        O(1)    IF INT self.hours > 11:
                    meridies = ' PM'
                ELSE:
                    meridies = ' AM'

                 # add zero for single digit minutes
        O(1)    SIZE = LENGTH(STRING(self.minutes))
                IF SIZE < 2:
                    STRING self.minutes = '0' + STRING(self.minutes)

                SET STRING self.delivery_time = STRING(self.hours) + ':' + STRING(self.minutes) + meridies

                RETURN self.delivery_time

        B.2 Apply programming models to the scenario.
        Simple mathematical calculations are used to convert 18/miles per hour into fractional time variables which are
        then converted to stings to be used to track total delivery time of each truck and the delivered time of each
        package. Both total delivery time of each truck and the delivered time of each package are held in memory with
        their associated locations in memory. Without the use of classes for both Truck and Package it would be
        necessary to loop through all the data of each member and would decrease performance of the method from
        O(1) to O(N^2).

        B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
              O(1)

        B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
              Upgrades to the physical trucks, the amount of packages that need to be delivered daily, or the expansion
              of the region of the delivery system may mean a change in miles per hour or the time it would take to
              complete a delivery route. See B.5 for why this method can be easily updated for these types of changes.

        B.5 Discuss the efficiency and maintainability of the software.
              This method is efficient and maintainable because it enables the miles per hour to be
              changed globally in the program within the Truck class. The time element is dependent upon the
              miles per hour, therefore, it will also be updated globally.
        """

        # calculate the time based on 18 miles per hour - O(1)
        frac, whole = math.modf(miles / self.average_speed)
        self.hours = round(whole) + self.leave_time_hour
        self.minutes = round(frac * 60) + self.leave_time_minutes

        # add zero for single digit minutes
        if len(str(self.minutes)) < 2:
            self.minutes = '0' + str(self.minutes)

        if self.hours > 11:
            meridies = ' PM'
        else:
            meridies = ' AM'

        self.delivery_time = str(self.hours) + ':' + str(self.minutes) + meridies

        return self.delivery_time

    def add_package(self, package_id):
        # find complete package information
        # check for full truck, if not full then add package_info to truck
        """
        B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
            O(1)    IF self.number_of_packages < self.max_packages AND package _id NOT IN self.all_package_info
                    THEN SET self.number_of_packages == self.number_of_packages + 1
            O(1)        IF package_id in package_info.master_package_id_list
                            THEN
                            SET INT package_index = package_id - 1
                            SET MEMORY ADDRESS package_memory_address == master_package_list[package_index]
                            SET STRING package_memory_address.loaded_on_truck == self.name

                            APPEND package_memory_address TO LIST self.all_package_info
                            APPEND package_id TO LIST loaded_packages
                            REMOVE package_id FROM LIST master_package_id_list
                        END IF

                    ELSE
                        SET BOOLEAN self.truck_full == TRUE
                    END IF

            O(1)    IF self.truck_full == TRUE
                        THEN PRINT "Truck is full."
                    END IF
        """
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
                package_info.master_package_id_list.remove(package_id)
        else:
            self.full_truck = True
        # else the truck is full, set boolean full_truck to True
        if self.full_truck is True:
            #  Truck is full. Fill next truck.
            print("Truck is full.")

    # function to load the trucks
    def load_truck(self, package_list):
        """
        B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
        IF BOOLEAN package_list IS NOT EMPTY
            IF BOOLEAN self.at_hub IS TRUE AND BOOLEAN self.full_truck IS FALSE
                THEN PRINT "Loading truck..." + STRING self.name

                FOR EACH LIST package in LIST package_list FROM element 1 to element N
                    IF BOOLEAN self.truck_full IS TRUE
                        THEN RETURN
                    ELSE
                        IF package IS LIST
                            THEN
                            SET INT package_id == package[0]

                            IF INT package_id IS IN package_info.master_id_package_list
                                THEN
                                CALL FUNCTION self.add_package(INT package_id)
                                REMOVE LIST package from LIST package_list
                            ELSE
                                SET INT package_id = INT package
                                IF INT package_id IS IN LIST package_info.master_id_list
                                    THEN CALL FUNCTION self.add_package(INT package_id)
        B.2 Apply programming models to the scenario.
        B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
        B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
        B.5 Discuss the efficiency and maintainability of the software.
        """
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
                            if package_id in package_info.master_package_id_list:
                                self.add_package(package_id)
                                package_list.remove(package)
                        else:
                            package_id = package
                            if package_id in package_info.master_package_id_list:
                                self.add_package(package_id)

    def route(self, start_vertex, package_list):

        """
        B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.

        O(1)    IF LIST package_list IS EMPTY
                    RETURN

                // set all packages in the list delivery status to 'en route'
        O(N)   FOR EACH STRING package_delivery_status IN LIST package_list
                    SET STRING package_delivery_status == STRING 'en route'
                END FOR

                // initialize and set empty unvisited queue list
                SET EMPTY LIST unvisited_queue

                // set package list argument to new address list with find_Address_list()
                SET LIST package_list = CALL FUNCTION find_address_list(package_list)

                // build a list of address ids from CLASS GRAPH.sorted_bidirectional to track unvisited package locations
        O(N)    FOR EACH TUPLE vertex IN Graph.sorted_bidirectional
        O(N^2)      FOR EACH MEMORY ADDRESS package IN LIST package_list
                        SET INT package_location = p[0]
                        SET INT location_vertex = vertex[0]

                        IF INT package_location == INT location_vertex
                           AND INT package_location IS NOT IN LIST unvisited_queue:
                             APPEND INT package_location TO LIST unvisited_queue
                        END IF
                    END FOR
                END FOR

                 // build the route using the first instance of a matching location id ot vertex id in
                  // sorted_bidirectional graph

                 SET EMPTY LIST route
                 SIZE = LENGTH OF unvisited_queue
        O(log N) WHILE SIZE > 0:
                    SET LIST hub = Graph.sorted_bidirectional[0][2]

                    // base case - hub has the vertex id of 0
                    IF INT start_vertex IS 0:
                        APPEND 0 to LIST route
                        SET BOOLEAN flag TO FALSE
        O(N*logN)       FOR EACH TUPLE vertex IN LIST hub:
        O(N^2 * logN)       FOR EACH LIST package IN LIST package_list:
                                SET INT package_location_id = p[0]
                                SET INT vertex_id = vertex[0]
                                IF INT package_location_id == INT vertex_id:
                                    SET INT address_id = INT package_location_id
                                    SET MEMORY ADDRESS package = p[2]
                                    SET INT miles = INT vertex[1]
                                    SET INT smallest_index = INT address_id

                                    // update mileage for truck
                                    SET INT self.mileage = self.mileage +  miles
                                    // deliver package
                                    SET INT package_id_number = SET INT package.package_id_number
                                    APPEND INT package_id_number TO LIST delivered_packages
                                    //add time of delivery for truck and package
                                    SET STRING package.delivery_status = STRING 'delivered'

                                    IF STRING package.delivery_status is 'delivered':
                                        SET STRING package.delivery_time = STRING self.set_delivery_time(self.mileage)
                                    END IF

                                    SET BOOLEAN flag TO TRUE
                                    BREAK

                                END IF

                            IF flag IS TRUE
                                BREAK
                            END IF

                            END FOR
                        END FOR

                        // remove first location to unvisited_queue
                        REMOVE INT address_id FROM LIST unvisited_queue

                        // add first location to route
                        APPEND INT address_id TO LIST route

                        // save first location to next vertex
                        // graph[address_id][2] accesses just the list of tuples: (vertex_id, miles from base vertex)
                        SET LIST next_vertex = Graph.sorted_bidirectional[address_id][2]

                        // change start vertex to any other integer than 0 - this is being used as a boolean flag
                        SET INT start_vertex = 1
                    END IF


                    // next_vertex is the closest distance in the adjacency list
                    //   it is the first instance of a location that is still in the unvisited list
                    // ex: the entire route algorithm for location 0 -> 26 should return:

                    // [0, 20, 21, 24, 26, 22, 17, 4, 16, 7, 13, 15, 18, \
                    // 11, 5, 9, 2, 25, 19, 8, 12, 6, 1, 13, 14, 3, 23, 10]

                    // Check potential path lengths from the current vertex to all neighbors.
                    // If shorter path from start_vertex to adj_vertex is found,
                    // update adj_vertex's distance and predecessor
        O(N*logN)       FOR EACH TUPLE vertex IN LIST next_vertex
                        SET INT vertex_id = INT vertex[0]
                        SET FLOAT miles = vertex[1]

                        IF INT vertex_id IS IN LIST unvisited_queue AND INT vertex_id != 0 AND FLOAT miles != 0.0
                            THEN
                            SET INT adj_vertex = INT vertex_id
                            SET FLOAT self.mileage = FLOAT self.mileage + FLOAT miles

                            // deliver package
        O(N^2*logN)             FOR EACH LIST package IN LIST package_list:
                                SET INT package_id = INT p[0]
                                IF INT package_id == INT adj_vertex:
        O(N^3*logN)                     FOR EACH MEMORY ADDRESS package_memory_address in package[2:]:
                                        APPEND INT package_memory_address.package_id_number TO LIST delivered_packages
                                        SET STRING package_memory_address.delivery_status = STRING 'delivered'
                                        IF STRING package_memory_address.delivery_status is 'delivered':
                                            SET STRING package_memory_address.delivery_time = \
                                            STRING self.set_delivery_time(self.mileage)
                                        END IF
                                    END FOR
                                    REMOVE LIST package FROM LIST package_list
                                END IF
                            BREAK
                            END FOR
                    END FOR

                    APPEND INT INDEX OF adj_vertex OF LIST unvisited_queue TO LIST route AND REMOVE FROM LIST unvisited_queue
                    SET LIST next_vertex = LIST Graph.sorted_bidirectional[adj_vertex][2]

                END WHILE
                // go back to hub - use adjacency list which is just a list of the miles in order of location id
        O(N)    FOR EACH TUPLE vertex IN LIST hub:
                    SET INT location_id = INT vertex[0]
                    SET FLOAT miles_for_current_vertex = FLOAT vertex[1]
                    SET INT last_index_in_route = INT route[-1]

                    IF INT location_id == INT last_index_in_route:
                        SET FLOAT self.mileage = FLOAT miles_for_current_vertex + FLOAT self.mileage

                        // hub vertex id is 0
                        APPEND 0 TO LIST route
                    END IF
                END FOR

                // set total delivery for truck
                SET STRING self.delivery_time = CALL STRING FUNCTION self.set_delivery_time(FLOAT self.mileage)

                RETURN route
        B.2 Apply programming models to the scenario.
        B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
        B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
        B.5 Discuss the efficiency and maintainability of the software.
        """
        # if the package_list parameter is empty return
        if not package_list:
            return
        # set all packages in the list delivery status to 'en route'
        for p in package_list:
            p.delivery_status = 'en route'

        unvisited_queue = []
        # vertex_id = g.sorted_bidirectional[start_vertex][0]
        # set package list to address list
        package_list = find_address_list(package_list)
        # build a list of address ids to track unvisited package locations
        for vertex in g.sorted_bidirectional:
            for p in package_list:
                package_location = p[0]
                location_vertex = vertex[0]
                if package_location == location_vertex and package_location not in unvisited_queue:
                    unvisited_queue.append(package_location)

        route = []
        while len(unvisited_queue) > 0:
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
                            package = p[2]
                            miles = vertex[1]
                            smallest_index = address_id
                            self.mileage += miles
                            # add time of delivery for truck and package
                            # deliver package
                            delivered_packages.append(p[2].package_id_number)
                            package.delivery_status = 'delivered'
                            if package.delivery_status is 'delivered':
                                package.delivery_time = self.set_delivery_time(self.mileage)
                            flag = True
                            break
                    if flag:
                        break
                unvisited_queue.remove(address_id)
                route.append(address_id)
                next_vertex = g.sorted_bidirectional[address_id][2]
                start_vertex = 1


            # next_vertex is the closest distance in the adjacency list
            #   it is the first occurence of a location that is still in the unvisited list
            #   the entire route algorithm for location 0 -> 26 should return:
            #       0, 20, 21, 24, 26, 22, 17, 4, 16, 7, 13, 15, 18, 11, 5, 9, 2, 25, 19, 8, 12, 6, 1, 13, 14, 3, 23, 10

            # Check potential path lengths from the current vertex to all neighbors.
            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            for vertex in next_vertex:
                vertex_id = vertex[0]
                if vertex_id in unvisited_queue and vertex_id != 0 and vertex[1] != 0.0:
                    adj_vertex = vertex_id
                    miles = vertex[1]
                    self.mileage += float(miles)
                    # deliver package
                    for p in package_list:
                        if p[0] == adj_vertex:
                            for package in p[2:]:
                                delivered_packages.append(package.package_id_number)
                                package.delivery_status = 'delivered'
                                if package.delivery_status is 'delivered':
                                    package.delivery_time = self.set_delivery_time(self.mileage)
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
        self.delivery_time = self.set_delivery_time(self.mileage)
        return route


def find_address_list(packages_list):
    """
    B.1 Comment using pseudocode to show the logic of the algorithm applied to this software solution.
         // list of package address in memory
         SET LIST address_bucket_list = []

         // check if package list exists
    O(1) IF BOOLEAN packages_list IS NOT EMPTY:

            // create a list to hold all memory addresses of packages associated with each package in the package list
            // argument and a list to hold all package ids associated with packages in the package list argument
            FOR EACH ADDRESS package IN LIST packages_list:
                SET INT package_id == INT package.package_id_number

                APPEND ADDRESS package TO LIST address_bucket_list
                APPEND INT package_id TO LIST address_for_package_found
            END FOR

         //list for boolean use to enforce unique data entries
         SET EMPTY LIST same_delivery_address

         // list for boolean use to flag that a package has been found and no packages are missed
         SET EMPTY LIST found_package_list

    O(N) FOR EACH ADDRESS package IN LIST address_bucket_list

            // set and initialize variables street_address, address_id, package_id to associated package information
            SET STRING street_address = STRING package.delivery_address
            SET INT address_id = INT package.address_id
            SET INT package_id = INT package.package_id_number

            // check if the address_id and street_address variables are not in same_delivery_address list then then
            // build the same_delivery_address and found_packages lists
    O(1)    IF LIST [address_id, street_address] IS NOT IN LIST same_delivery_address
                APPEND LIST [address_id, street_address] TO LIST same_delivery_address
    O(N)        FOR LIST s IN same_delivery_address
    O(1)        IF s[1] == street_address
                    SET INT index == INDEX OF same_delivery_address
    O(1)            IF INT package_id IS NOT IN LIST found_package_list:
                        APPEND INT package_id TO LIST found_package_list
                        INSERT MEMORY ADDRESS package TO same_delivery_address AT INDEX index
                    END IF
                END IF
                END FOR
            END IF
         END FOR

        RETURN same_delivery_address


    B.2 Apply programming models to the scenario.

    B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
          O(N^2)

    B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
    B.5 Discuss the efficiency and maintainability of the software.
    """

    # list to hold package addresses in memory from CLASS PACKAGE
    address_bucket_list = []

    # check if package_list exists
    if packages_list:

        # create a list to hold all memory addresses of packages associated with each package in the package list
        # argument and a list to hold all package ids associated with packages in the package list argument
        for p in packages_list:
            package_id = p.package_id_number
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
T1.load_truck(package_info.truck_one_only) # 0 packages
T1.load_truck(package_info.packages_with_delivery_deadlines) # 14 packages
T1.load_truck(package_info.naked_packages) # until full
T1.route(0, T1.all_package_info)
T1.set_delivery_time(T1.mileage)



"""
TRUCK 2
Truck 2 shares a driver with Truck 1 and must wait for Truck 1 to return from deliveries
    Truck 2 is set to leave at the time T1 returns (10:27)
"""
T2 = Truck('T2')
T2.leave_time_hour = T1.hours

"""
TRUCK 3 
- delivers all remaining packages after Truck 1 and Truck 2 are loaded
- leaves the hub at 8:00 AM
- uses master package list to make sure no packages are missed during loading
"""

# Truck 3
T3 = Truck('T3')
T3.load_truck(package_info.packages_with_delivery_deadlines)
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
for p in package_info.master_package_list:
    # split p.delivery_time into hours and minutes
    if p.delivery_time is '':
        package_info.master_package_id_list.append(p.package_id_number)

package_info.p9.delivery_address = '410 S State St'
package_info.p9.address_id = 19
T2.leave_time_minutes = round(T1.minutes/60)
T2.load_truck(package_info.truck_two_only)  # 4 packages - 2, 18, 36, 38
T2.load_truck(package_info.delayed_flight)  # 4 packages - 6, 25, 28, 32
T2.load_truck(package_info.master_package_id_list)  # make sure no packages were missed
T2.load_truck(package_info.wrong_address)  # 1 package - 9
T2.route(0, T2.all_package_info)
T2.set_delivery_time(T2.mileage)  # set self.delivery_time to calculated delivery time

# total miles for all 3 trucks
total_miles = T1.mileage + T2.mileage + T3.mileage
print('Total Mileage for All 3 Trucks:', total_miles)

# delivered packages
delivered_packages.sort()
print(delivered_packages)








