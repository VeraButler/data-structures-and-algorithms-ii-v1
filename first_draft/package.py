import csv
from typing import List, Any

pkgFile = '../WGUPS Package File.csv'

# https://stackoverflow.com/questions/34008527/csv-in-hashtable-then-calculate-sum
# https://docs.python.org/3/library/csv.html


# format package table into a matrix
# hash is the package_id at index 0 of each row
# PART E: Develop a hash table
pkg_tbl_hash = []
# list to hold all Packages created
master_package_list = []
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


class Package:
    # init class
    def __init__(self, package_key):
        # assign values to class properties
        self.package_list = pkg_tbl_hash
        self.package_id_number = package_key
        # print(self.package_id_number)
        # subtract 1 from package key to access hash table in the right index
        package_key -= 1
        # print(package_key)
        # print(self.package_list[0])
        # print(self.package_list[package_key])
        self.delivery_address = self.package_list[package_key][1]
        self.address_id = -1
        # print(self.delivery_address)
        self.delivery_deadline = self.package_list[package_key][2]
        self.delivery_city = self.package_list[package_key][3]
        self.delivery_state = self.package_list[package_key][4]
        self.delivery_zip_code = self.package_list[package_key][5]
        self.package_weight = self.package_list[package_key][6]
        self.delivery_status = self.package_list[package_key][7]
        self.special_notes = self.package_list[package_key][8]

    def info(self):
        return '''
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


def get_pkg_list():
    return pkg_tbl_hash


# to lookup information about a package create a Package object with
# package_object = Package() with the associated pkg_tbl_hash and the package id
# then package_obj.attribute_you_are_looking_for

# def get_id(self):
#     if package_id_number:
#         return package_id_number
#     else:
#         return "Missing Package ID"
#
# def get_delivery_address(self):
#     if delivery_address:
#         return delivery_address
#     else:
#         return "Missing Street Address"
#
# def get_delivery_city(self):
#     if delivery_city:
#         return delivery_city
#     else:
#         return "Missing City"
#
# def get_delivery_state(self):
#     if delivery_state:
#         return delivery_state
#     else:
#         return "Missing State"
#
# def get_delivery_zip_code(self):
#     if delivery_zip_code:
#         return delivery_zip_code
#     else:
#         return "Missing Zip Code"
#
# def get_deadline(self):
#     if delivery_deadline:
#         return delivery_deadline
#     else:
#         return "No Deadline"
#
#
# def get_package_weight(self):
#     if package_weight:
#         return package_weight
#     else:
#         return "Missing Weight"
#
#
# def get_delvery_status(self):
#     if delivery_address:
#         return delivery_state
#     else:
#         return "Missing Address"
#
# def get_special_notes(self):
#     if special_notes:
#         return self.special_notes
#     else:
#         return "No notes."
# print(package1.get_delivery_address())
# print(package1.get_deadline())
# print(package1.get_delivery_city())
# print(package1.get_delivery_state())
# print(package1.get_delivery_zip_code())
# print(package1.get_delvery_status())
# print(package1.get_id())
# print(package1.get_package_weight())
# print(package1.get_special_notes())








