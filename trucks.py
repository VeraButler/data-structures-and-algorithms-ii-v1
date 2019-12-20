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
from package_info import *
from graph import g


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


T1 = Truck()
T1.add_package(p1.package_info_list)
print(T1.all_package_info)
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()
# T1.add_package()


print(T1.number_of_packages)




