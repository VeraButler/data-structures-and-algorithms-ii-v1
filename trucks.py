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

# number of drivers available is 2
total_number_of_drivers_available = 2
# SET number_of_drivers = 2
number_of_drivers = 2
def check_driver_count():
    if number_of_drivers < total_number_of_drivers_available:
        return False
    else:
        return True

class Truck:
    # init class with data members
    def __init__(self, truck):

        # SET STRING truck name = ARGUMENT STRING truck - used to track packages
        self.name = truck

        # Track the number of packages on each truck
        # SET INT self.number_of_packages = INT 0
        self.number_of_packages = 0

        # Maximum number of packages allowed on each Truck is 16
        # SET INT max_packages = INT 16
        self.max_packages = 16

        # Trucks travel at an average speed of 18 miles per hour.
        # SET FLOAT self.average_speed = FLOAT 18
        self.average_speed = float(18)

        # Each driver stays with the same truck as long as that truck is in service.
        self.driver = 0

        # Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
        # The day ends when all 40 packages have been delivered.
        # SET INT self.time = INT 8 -> 8 for 8:00 AM
        self.time = 8

        # There is up to one special note for each package.
        # SET STRING self.package_notes = DEFAULT STRING 'No notes.'
        self.package_notes = 'No notes.'

        # track the distance driven
        # SET FLOAT self.distance = FLOAT 0
        self.distance = float(0)

        # Package list to hold package ids on the truck
        # SET LIST self.all_package_info = EMPTY LIST
        self.all_package_info = []

        # Boolean to track if truck is at the hub or en route
        # SET BOOLEAN self.at_hub = TRUE
        self.at_hub = True

        # Boole to track the trucks max capacity of 16 packages
        # SET self.full_truck = FALSE
        self.full_truck = False

        """
        Track Mileage and Time
        
        SET self.mileage = 0
        SET self.leave_time_hour = 8
        SET self.leave_time_minutes = 0
        SET self.hours = 0 
        SET self.hours_str = ''
        SET self.minutes = 0
        SET self.minutes_str = ''
        SET delivery_time = 0
        """
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

    def get_package_delivery_deadline(self, package, delivered):
        pd = package.delivery_deadline

        deadline_hours = pd[0:2]
        deadline_minutes = pd[3:5]
        deadline_meridies = pd[-2:]

        delivered.split(":")
        delivered_hours = delivered[0]
        delivered_minutes = delivered[2]+delivered[3]
        delivered_meridies = delivered[-2:]

        if (deadline_hours >= delivered_hours and deadline_minutes >= delivered_minutes) \
            or\
            (deadline_meridies is 'AM' and delivered_meridies is 'PM'):
            # if false the package is late
            return False
        else:
            return True


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

            BIG O => O(1)
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
                # package_info.master_package_id_list.remove(package_id)
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
        O(1)    IF BOOLEAN package_list IS NOT EMPTY
        O(1)        IF BOOLEAN self.at_hub IS TRUE AND BOOLEAN self.full_truck IS FALSE
                        THEN PRINT "Loading truck..." + STRING self.name

        O(N)            FOR EACH package_id in LIST package_list
        N = [1-inf]
        O(1)                IF BOOLEAN self.truck_full IS TRUE
                                THEN RETURN
                            ELSE
        O(1)                    IF package IS LIST
                                    THEN
                                    SET INT package_id == package[0]

        O(1)                        IF INT package_id IS IN package_info.master_id_package_list
                                        THEN
                                        CALL FUNCTION self.add_package(INT package_id)
                                        REMOVE LIST package from LIST package_list
                                    ELSE
                                        SET INT package_id = INT package
        O(1)                            IF INT package_id IS IN LIST package_info.master_id_list
                                            THEN CALL FUNCTION self.add_package(INT package_id)
        BIG O => O(N)

        B.2 Apply programming models to the scenario.
        B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
                O(N)
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
                SET self.driver = 1
                SET number_of_drivers = number_of_drivers - self.driver
        O(1)    IF LIST package_list IS EMPTY
                    RETURN

                // set all packages in the list delivery status to 'en route'
                    // packages have already been loaded with load_truck
        O(N)    FOR EACH STRING package_delivery_status IN LIST package_list
        N = [1-16]
                    SET STRING package_delivery_status == STRING 'en route'
                END FOR

                // initialize and set empty unvisited queue list
                SET EMPTY LIST unvisited_queue

                // set package list argument to new address list with find_Address_list()
        O(N)    SET LIST package_list = CALL FUNCTION find_address_list(package_list)
        N = [1-16]



                // build a list of address ids from CLASS GRAPH.sorted_bidirectional to track unvisited package locations

        O(N)    FOR EACH TUPLE vertex IN Graph.sorted_bidirectional
        N = 27

        O(N^2)      FOR EACH MEMORY ADDRESS package IN LIST package_list
        N = truckload

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
        N = [1-16]
                    SET LIST hub = Graph.sorted_bidirectional[0][2]

                    // base case - hub has the vertex id of 0
                    IF INT start_vertex IS 0:
                        APPEND 0 to LIST route
                        SET BOOLEAN flag TO FALSE
        O(N*logN)       FOR EACH TUPLE vertex IN LIST hub:
        N = 27
        O(log[1-16] * 27)

        O(N^2 * logN)       FOR EACH LIST package IN LIST package_list:
        N = [1-16]
        O(log[1-16]*(27+[1-16])^2)
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
        N = 27
        O(log[1-16] * 27)

                        SET INT vertex_id = INT vertex[0]
                        SET FLOAT miles = vertex[1]

                        IF INT vertex_id IS IN LIST unvisited_queue AND INT vertex_id != 0 AND FLOAT miles != 0.0
                            THEN
                            SET INT adj_vertex = INT vertex_id
                            SET FLOAT self.mileage = FLOAT self.mileage + FLOAT miles

                            // deliver package
        O(N^2*logN)         FOR EACH LIST package IN LIST package_list:
        N = [1-16]
        O(log[1-16]*(27+[1-16])^2)

                                SET INT package_id = INT p[0]
                                IF INT package_id == INT adj_vertex:
        O(N^3*logN)                FOR EACH MEMORY ADDRESS package_memory_address in package[2:]:
        N = [1-16]
        O(log[1-16] * (inf + [1-16] + [1-16])^3
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
        N = 27      SET INT location_id = INT vertex[0]
        O(27)       SET FLOAT miles_for_current_vertex = FLOAT vertex[1]
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

        BIG O => O(N^3 * LogN)
        B.2 Apply programming models to the scenario.
        B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
                O(N^3 * LogN)
        B.4 Discuss the ability of your solution to adapt to a changing market and to scalability.
        B.5 Discuss the efficiency and maintainability of the software.
        """
        if check_driver_count() is True:
            self.driver = 1

        # if the package_list parameter is empty return
        if not package_list:
            return
        # set all packages in the list delivery status to 'en route'
        for p in package_list:
            p.delivery_status = 'en route'
            p.load_time = self.set_load_time()

        unvisited_queue = []
        # vertex_id = g.sorted_bidirectional[start_vertex][0]
        # set package list to address list
        package_list = find_address_list(package_list)
        # build a list of address ids to track unvisited package locations
        for p in package_list:
            package_location = p[0]
            if package_location not in unvisited_queue:
                unvisited_queue.append(package_location)


        route = []
        while len(unvisited_queue) > 0:
            # Visit vertex with closest distance from current location
            # smallest index is also the next_vertex
            hub = g.sorted_bidirectional[0]
            if start_vertex is 0:
                # # look for packages with high priority
                # for p in package_list:
                #     for q in p[2:]:
                #         if q.delivery_deadline == '9:00 AM':
                #             route.append(q.address_id)
                # TODO FIX route for new graph
                route.append(0)
                flag = False
                for vertex in hub:
                    for p in package_list:
                        if p[0] == vertex[0]:
                            address_id = p[0]
                            package = p[2]
                            miles = vertex[1]
                            self.mileage += miles
                            # add time of delivery for truck and package
                            # deliver package
                            if package.package_id_number in package_info.master_package_id_list:
                                delivered_packages.append(package.package_id_number)
                                package.delivery_status = 'delivered'
                                package_info.master_package_id_list.remove(p[2].package_id_number)
                                package.delivery_time = self.set_delivery_time(self.mileage)
                                print(package.info())
                            flag = True
                            break
                    if flag:
                        break
                unvisited_queue.remove(address_id)
                route.append(address_id)
                next_vertex = g.sorted_bidirectional[address_id]
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
                    self.mileage += miles
                    # deliver package
                    for p in package_list:
                        if p[0] == adj_vertex:
                            for package in p[2:]:
                                if package.package_id_number in package_info.master_package_id_list:
                                    delivered_packages.append(package.package_id_number)
                                    package.delivery_status = 'delivered'
                                    package_info.master_package_id_list.remove(package.package_id_number)
                                if package.delivery_status is 'delivered':
                                    package.delivery_time = self.set_delivery_time(self.mileage)
                                if self.get_package_delivery_deadline(package, '9:00 AM') is False:
                                    print("Package", package.package_id_number, "was delivered late.")
                                else:
                                    print("Package", package.package_id_number, "was delivered on time.")
                            package_list.remove(p)
                    break
            route.append(unvisited_queue.pop(unvisited_queue.index(adj_vertex)))
            next_vertex = g.sorted_bidirectional[adj_vertex]

        # go back to hub - use adjacency list which is just a list of the miles in order of location id
        hub = g.sorted_bidirectional[0]
        for vertex in hub:
            miles_for_current_vertex = vertex[1]
            last_index_in_route = route[-1]
            if vertex[0] == last_index_in_route:
                self.mileage += miles_for_current_vertex
                route.append(0)
        self.delivery_time = self.set_delivery_time(self.mileage)

        self.driver = 0

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
    O(N)    FOR EACH ADDRESS package IN LIST packages_list:
                SET INT package_id == INT package.package_id_number

                APPEND ADDRESS package TO LIST address_bucket_list
                APPEND INT package_id TO LIST address_for_package_found
            END FOR

         //list for boolean use to enforce unique data entries
         SET EMPTY LIST same_delivery_address

         // list for boolean use to flag that a package has been found and no packages are missed
         SET EMPTY LIST found_package_list

    O(N) FOR EACH ADDRESS package IN LIST address_bucket_list
    N = [1-16]??? is this the number of locations or packages in the list

            // set and initialize variables street_address, address_id, package_id to associated package information
            SET STRING street_address = STRING package.delivery_address
            SET INT address_id = INT package.address_id
            SET INT package_id = INT package.package_id_number

            // check if the address_id and street_address variables are not in same_delivery_address list then then
            // build the same_delivery_address and found_packages lists
    O(1)    IF LIST [address_id, street_address] IS NOT IN LIST same_delivery_address
                APPEND LIST [address_id, street_address] TO LIST same_delivery_address

    O(N)        FOR LIST s IN same_delivery_address
    N = [1-16]??? see above ???

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

    BIG O Total => O(N) => O([1-16])


    B.2 Apply programming models to the scenario.

    B.3 Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
          O(N)

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
            same_delivery_address.append([address_id, street_address, p])
        for s in same_delivery_address:
            if s[1] == street_address:
                index = same_delivery_address.index(s)
                if package_id not in found_package_list:
                    found_package_list.append(package_id)
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


# SET package #9 to new address
package_info.p9.delivery_address = '410 S State St'
package_info.p9.address_id = 19
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
    print(package_info.master_package_id_list)
    for p in package_info.master_package_list:
        if p.package_id_number not in delivered_packages:
            print("Undelivered:", p.package_id_number)






