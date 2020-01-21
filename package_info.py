import csv
from graph import address_hash
pkgFile = './WGUPS Package File.csv'

"""
PACKAGE DATA BIG O ANALYSIS

BIG O NOTES:
RESOURCE: https://wiki.python.org/moin/TimeComplexity
Addition:
INITIALIZE AND SET = one operation = 1 
Multiplication:
FOR = N operations if each element of data needs to be accessed
FOR = LogN if it cuts down the amount of data that needs to be accessed (merge sort)
WHILE = LogN because it potentially runs shorter than the length of all the data elements

>>> PURPOSE: format the package data from the provided csv file into a hash table
>>> FORMAT: HASH ID = package ID. All package id's must be unique to enter a new package into the system.

------------------------------------------------------------------------------------------------------------------------
BIG O       |                                           PSEUDOCODE                                                     |
------------------------------------------------------------------------------------------------------------------------


O(1)........INITIALIZE AND SET EMPTY LIST pkg_tbl_hash

            * *************************************************************** *
            * OPEN is just accessing a pointer in memory allowing access to   *
            * the data file as variable 'dt'.                                 *
            * This does not require any iterations therefore it has a run     *
            * time of O(1).                                                   *
            * *************************************************************** *
O(1)........OPEN pkg_tbl_hash AS pf:

                * *************************************************************************************************** *
                * Return a reader object which will iterate over lines in the given csvfile. csvfile can be any object*
                * which supports the iterator protocol and returns a string each time its __next__() method is called *
                * To iterate over each line means it must include a for loop like this example:                       *
                *      for index in range(0, len(filtered), 1): add filtered row to reader[index]                     *
                * index = N                                                                                           *
                * len(filtered) = N                                                                                   *
                * O(f(index) * f(filtered)) = N * N = O(N^2)                                                          *
                * *************************************************************************************************** *
O(N)............INITIALIZE AND SET LIST reader = csv.reader(pf)
                INITIALIZE AND SET INT line_number = 0
                INITIALIZE AND SET STRING delivery_status = 'at hub'
            >>> skip first line of csv
                pf.readline()
O(8N)...........FOR EACH row IN reader
                >>> PART E: set variables for insert function with corresponding column in each row
                >>> delivery_address, delivery_deadline, delivery_city, delivery_state, 
                >>> ...delivery_zip_code, package_weight, delivery_status
                
                >>> this is the unique hash id
                    INITIALIZE AND SET INT package_id_number = INT(row[0])
                    
                    INITIALIZE AND SET STRING delivery_address = row[1]
                    INITIALIZE AND SET STRING delivery_deadline = row[5]
                    INITIALIZE AND SET delivery_city = row[2]
                    INITIALIZE AND SET STRING delivery_state = row[3]
                    INITIALIZE AND SET STRING delivery_zip_code = row[4]
                    INITIALIZE AND SET STRING package_weight = row[6]
                
                    APPEND LIST [package_id_number, delivery_address, delivery_deadline, delivery_city, delivery_state,
                             delivery_zip_code, package_weight, delivery_status, special_notes]
                    TO LIST pkg_tbl_hash
O(N)............END FOR
                
            >>> create global lists to use throughout the program
                INITIALIZE AND SET LIST packages_with_delivery_deadlines = ["Delivery Deadlines"]
                INITIALIZE AND SET LIST packages_without_delivery_deadlines = ["No Delivery Deadline"]
                
            >>> list of packages with special notes
                INITIALIZE AND SET LIST packages_with_special_notes = ["Special Notes"]
                INITIALIZE AND SET LIST naked_packages = ["No Special Needs"]
                
            >>> separate lists for packages with special notes
                INITIALIZE AND SET LIST delayed_flight = ["Delayed Flights"]
                INITIALIZE AND SET LIST grouped_deliveries = ["Grouped Deliveries"]
                INITIALIZE AND SET LIST truck_one_only = ["Load on this Truck one only"]
                INITIALIZE AND SET LIST truck_two_only = ["Load on this Truck two only"]
                INITIALIZE AND SET LIST truck_three_only = ["Load on this Truck two only"]
                INITIALIZE AND SET LIST wrong_address = ["Wrong Address"]
                
            >>> by zipcode
                INITIALIZE AND SET LIST zipcode_sort = ["By Zipcode"]
                
            >>> used by Class Trucks in trucks.py to flag loaded, delivered, and undelivered packages
                INITIALIZE AND SET LIST master_package_id_list = []
                
            >>> master package list - p1...pN memory addresses to be accessed in trucks.py
            >>> _ flags other users that this list should not be changed unless absolutely necessary
                INITIALIZE AND SET LIST _master_package_list = []



* *************************************************************** *
*                       COMMENT BLOCK                             *
* *************************************************************** *
"""
# PART E: Develop a hash table
pkg_tbl_hash = []
with open(pkgFile) as pf:
    reader = csv.reader(pf)
    line_number = 0
    delivery_status = 'at hub'
    pf.readline()
    for row in reader:
        # set variables for insert function
        # delivery_address, delivery_deadline, delivery_city, delivery_state, delivery_zip_code, package_weight,
        #                delivery_status
        package_id_number = int(row[0])
        delivery_address = row[1]
        delivery_deadline = row[5]
        delivery_city = row[2]
        delivery_state = row[3]
        delivery_zip_code = row[4]
        package_weight = row[6]
        special_notes = row[7]
        # PART E: use an insertion function that takes the listed components and inserts them into the hash table
        pkg_tbl_hash.append([package_id_number, delivery_address, delivery_deadline, delivery_city, delivery_state,
                             delivery_zip_code, package_weight, delivery_status, special_notes])


# list for delivery deadlines
packages_with_delivery_deadlines = ["Delivery Deadlines"]
packages_without_delivery_deadlines = ["No Delivery Deadline"]

# list of packages with special notes
packages_with_special_notes = ["Special Notes"]
naked_packages = ["No Special Needs"]

# separate lists for packages with special notes
delayed_flight = ["Delayed Flights"]
grouped_deliveries = ["Grouped Deliveries"]
truck_one_only = ["Load on this Truck one only"]
truck_two_only = ["Load on this Truck two only"]
truck_three_only = ["Load on this Truck two only"]
wrong_address = ["Wrong Address"]

# by zipcode
zipcode_sort = ["By Zipcode"]

# master package id list
master_package_id_list = []

# master package list - p1...pN memory addresses to be accessed in trucks.py
master_package_list = []


class Package:
    # init class
    def __init__(self, package_list, package_key):
        master_package_list.append(self)
        # assign values to class properties
        # individual package information list
        self.package_info_list = package_list[package_key - 1]
        self.package_id_number = package_key
        # subtract 1 from package key to access hash table in the right index
        package_key -= 1
        self.delivery_address = self.package_info_list[1]
        self.zipcode = ''
        self.address_id = -1
        self.delivery_deadline = self.package_info_list[2]
        self.load_time = ''
        self.delivery_time = ''
        self.delivery_city = self.package_info_list[3]
        self.delivery_state = self.package_info_list[4]
        self.delivery_zip_code = self.package_info_list[5]
        self.package_weight = self.package_info_list[6]
        self.delivery_status = 'at hub'
        self.special_notes = self.package_info_list[8]
        self.required_truck = ''
        self.loaded_on_truck = ''

        # find address id and set zipcode
        for a in address_hash:
            if a[1] == self.delivery_address:
                self.address_id = a[0] - 1
                break
        if self.address_id is -1:
            self.address_id = 23


        # place package into correct special notes list to be loaded onto appropriate trucks in trucks.py
        p_id = self.package_id_number
        s = self.special_notes
        d = self.delivery_deadline

        if self.delivery_deadline != 'EOD':
            packages_with_delivery_deadlines.append([p_id, d])
        else:
            packages_without_delivery_deadlines.append([p_id, d])
            # delete EOD
            self.delivery_deadline = ''

        if self.special_notes:
            packages_with_special_notes.append([p_id, s])

        if 'Can only be on truck' in s:
            # split special note for iterable string
            split = s.split()
            # iterate through string, check for int
            for i in split:
                if i.isdigit():
                    # initiate and set truck number
                    truck_number = i
            # append package id and truck number to can only be on truck N
            #  T is for Truck - Trucks are created as T1...TN
            truck = 'T' + str(truck_number)
            self.required_truck = truck
            # load package to correct truck
            # if trucks are added in the future this will need to be edited
            # if truck is not at the HUB then add to a waiting list this_truck_only
            if truck is 'T1':
                truck_one_only.append([p_id, truck])
            elif truck == 'T2':
                truck_two_only.append([p_id, truck])
            elif truck == 'T3':
                truck_three_only.append([p_id, truck])
            else:
                print("Truck does not exist. Check your truck string.")

        # check delayed package info
        if 'Delayed' in s:
            delayed_flight.append([p_id, s])

        if 'Wrong address listed' in s:
            wrong_address.append([p_id, s])

        if 'Must be' in s:
            grouped_deliveries.append([p_id, s])

        # add packages with no delivery deadline or special notes to a list
        #   the packages in this list will be added last to fill the remaining spots in the trucks
        no_deadline = False
        for i in packages_without_delivery_deadlines[1:]:
            if p_id == i[0]:
                no_deadline = True
        # if no deadline is true and special notes do not exist add to no special needs packages list
        if no_deadline and not s:
            naked_packages.append(p_id)

        if p_id not in master_package_id_list:
            master_package_id_list.append(p_id)
        else:
            print("Package Id already exists. Please try again.")


    def info(self):
        info = '''
        Package Id Number: {}
        Delivery Address: {}
        Delivery Address ID: {}
        Delivery Deadline: {}
        Delivery Time: {}
        Delivery City: {}
        Delivery State: {}
        Delivery Zip Code: {}
        Package Weight: {}
        Delivery Status: {}
        Loaded on Truck Number: {}
        Special Notes: {}
        '''.format(self.package_id_number, self.delivery_address, self.address_id, self.delivery_deadline, self.delivery_time,
                   self.delivery_city, self.delivery_state, self.delivery_zip_code, self.package_weight,
                   self.delivery_status, self.loaded_on_truck, self.special_notes)
        return info

# create all packages
# O(N)
def build_master_package_list(package_list):
    for p in package_list:
        package_id = p[0]
        name = Package(package_list, package_id)


def insert_new_package(package_id, delivery_address, delivery_deadline, delivery_city, delivery_zipcode,
                       package_weight, delivery_status):
    """
    Insert package information into pkg_table hash
    Create new Package object
    """
    # O(N) - N = length of master_package_id_list
    if package_id not in master_package_id_list:
        pkg_tbl_hash.append([package_id, delivery_address, delivery_deadline, delivery_city, delivery_state,
                            delivery_zipcode, package_weight, delivery_status, 'no notes'])
    name = Package(pkg_tbl_hash, package_id)


build_master_package_list(pkg_tbl_hash)

# # list for delivery deadlines
# print(packages_with_delivery_deadlines)
# print(packages_without_delivery_deadlines)
#
# # list of packages with special notes
# print(packages_with_special_notes)
# print(naked_packages)
#
# # separate lists for packages with special notes
# print(delayed_flight)
# print(truck_one_only)
# print(truck_two_only)
# print(truck_three_only)
# print(wrong_address)







