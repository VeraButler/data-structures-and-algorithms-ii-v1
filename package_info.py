import csv
from typing import List, Any

pkgFile = './WGUPS Package File.csv'

# https://stackoverflow.com/questions/34008527/csv-in-hashtable-then-calculate-sum
# https://docs.python.org/3/library/csv.html


# format package table into a matrix
# hash is the package_id at index 0 of each row
# PART E: Develop a hash table
pkg_tbl_hash = []
with open(pkgFile) as pf:
    reader = csv.reader(pf)
    line_number = 0
    delivery_status = 'en route'
    pf.readline()
    for row in reader:
        # set variables for insert function
        # delivery_address, delivery_deadline, delivery_city, delivery_state, delivery_zip_code, package_weight,
        #                delivery_status
        # print(row)
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
# print(pkg_tbl_hash)


def add_package_to_list(pkg_id, address, deadline, city, state,
                        zip_code, weight, status, notes):
    package_info_list = [pkg_id, address, deadline, city, state, zip_code, weight, status, notes]

    # special case for first package
    if not master_package_list:
        master_package_list.append(package_info_list)
        print("Package added successfully")
    else:
        if not master_package_list[package_id_number]:
            master_package_list.append(package_info_list)
            print("Package added successfully")
        else:
            print("Package already exists.")


# list for delivery deadlines
packages_with_delivery_deadlines = ["Delivery Deadlines"]
packages_without_delivery_deadlines = ["No Delivery Deadline"]

# list of packages with special notes
packages_with_special_notes = ["Special Notes"]
naked_packages = ["No Special Needs"]

# separate lists for packages with special notes
delayed_flight = ["Delayed Flights"]
truck_one_only = ["Load on this Truck one only"]
truck_two_only = ["Load on this Truck two only"]
truck_three_only = ["Load on this Truck two only"]
wrong_address = ["Wrong Address"]


# inlcude package list to make this class work for future additions of packages
class Package:
    # init class
    def __init__(self, package_list, package_key):
        # assign values to class properties
        # individual package information list
        self.package_info_list = package_list[package_key - 1]
        self.package_id_number = package_key
        # print(self.package_id_number)
        # subtract 1 from package key to access hash table in the right index
        package_key -= 1
        # print(package_key)
        # print(self.package_list[0])
        # print(self.package_list[package_key])
        self.delivery_address = self.package_info_list[1]
        self.address_id = -1
        # print(self.delivery_address)
        self.delivery_deadline = self.package_info_list[2]
        self.delivery_city = self.package_info_list[3]
        self.delivery_state = self.package_info_list[4]
        self.delivery_zip_code = self.package_info_list[5]
        self.package_weight = self.package_info_list[6]
        self.delivery_status = self.package_info_list[7]
        self.special_notes = self.package_info_list[8]
        self.required_truck = ''

        if self.delivery_deadline != 'EOD':
            packages_with_delivery_deadlines.append([self.package_id_number, self.delivery_deadline])
        else:
            packages_without_delivery_deadlines.append([self.package_id_number, self.delivery_deadline])

        if self.special_notes:
            packages_with_special_notes.append([self.package_id_number, self.special_notes])

        # sort to correct special notes list and load onto appropriate trucks
        p_id = self.package_id_number
        s = self.special_notes
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

        # check for wrong address info
        if 'Wrong address' in self.special_notes:
            wrong_address.append([p_id, s])

        # add packages with no delivery deadline or special notes to a list
        #   the packages in this list will be added last to fill the remaining spots in the trucks
        no_deadline = False
        for i in packages_without_delivery_deadlines[1:]:
            if p_id == i[0]:
                no_deadline = True
        # if no deadline is true and special notes do not exist add to no special needs packages list
        if no_deadline and not s:
            naked_packages.append(p_id)

    def info(self):
        info = '''
        Package Id Number: {}
        Delivery Address: {}
        Delivery Deadline: {}
        Delivery City: {}
        Delivery State: {}
        Delivery Zip Code: {}
        Package Weight: {}
        Delivery Status: {}
        Special Notes: {}
        '''.format(self.package_id_number, self.delivery_address, self.delivery_deadline, self.delivery_city,
                   self.delivery_state, self.delivery_zip_code, self.package_weight, self.delivery_status,
                   self.special_notes)
        return info


# create all packages
p1 = Package(pkg_tbl_hash, 1)
p2 = Package(pkg_tbl_hash, 2)
p3 = Package(pkg_tbl_hash, 3)
p4 = Package(pkg_tbl_hash, 4)
p5 = Package(pkg_tbl_hash, 5)
p6 = Package(pkg_tbl_hash, 6)
p7 = Package(pkg_tbl_hash, 7)
p8 = Package(pkg_tbl_hash, 8)
p9 = Package(pkg_tbl_hash, 9)
p10 = Package(pkg_tbl_hash, 10)
p11 = Package(pkg_tbl_hash, 11)
p12 = Package(pkg_tbl_hash, 12)
p13 = Package(pkg_tbl_hash, 13)
p14 = Package(pkg_tbl_hash, 14)
p15 = Package(pkg_tbl_hash, 15)
p16 = Package(pkg_tbl_hash, 16)
p17 = Package(pkg_tbl_hash, 17)
p18 = Package(pkg_tbl_hash, 18)
p19 = Package(pkg_tbl_hash, 19)
p20 = Package(pkg_tbl_hash, 20)
p21 = Package(pkg_tbl_hash, 21)
p22 = Package(pkg_tbl_hash, 22)
p23 = Package(pkg_tbl_hash, 23)
p24 = Package(pkg_tbl_hash, 24)
p25 = Package(pkg_tbl_hash, 25)
p26 = Package(pkg_tbl_hash, 26)
p27 = Package(pkg_tbl_hash, 27)
p28 = Package(pkg_tbl_hash, 28)
p29 = Package(pkg_tbl_hash, 29)
p30 = Package(pkg_tbl_hash, 30)
p31 = Package(pkg_tbl_hash, 31)
p32 = Package(pkg_tbl_hash, 32)
p33 = Package(pkg_tbl_hash, 33)
p34 = Package(pkg_tbl_hash, 34)
p35 = Package(pkg_tbl_hash, 35)
p36 = Package(pkg_tbl_hash, 36)
p37 = Package(pkg_tbl_hash, 37)
p38 = Package(pkg_tbl_hash, 38)
p39 = Package(pkg_tbl_hash, 39)
p40 = Package(pkg_tbl_hash, 40)

print(len(packages_with_delivery_deadlines), packages_with_delivery_deadlines)
print(packages_without_delivery_deadlines)
print(packages_with_special_notes)
print(naked_packages)
print(delayed_flight)
# print(this_truck_only)
print(wrong_address)
print(pkg_tbl_hash)


