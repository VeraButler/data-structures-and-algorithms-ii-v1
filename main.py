import distance_table
import graph
import package_info
import trucks

"""
G. Provide an interface for the insert and look-up functions to view the status of any package at any time. 
This function should return all information about each package, including delivery status.

1.  Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.

2.  Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.

3.  Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.
"""

print("Hello. Please follow the instructions below.")
start_time = input("Enter the start time in the format HH:MM AM or PM (8:00 AM)")
end_time = input("Enter the end time in the format HH:MM AM or PM (8:00 PM)")

# split start and end time strings into hours and minutes
st_split = start_time.split(':')
start_time_hour = int(st_split[0])
start_time_minutes = int(start_time[-5:-3])/60
start_time = start_time_hour + start_time_minutes

end_time_split = end_time.split(':')
end_time_hours = int(end_time[0])
end_time_minutes = int(end_time[-5:-3])/60
end_time = end_time_hours + end_time_minutes


for p in package_info.master_package_list:
    # check for missed packages
    if p.delivery_time is '' or p.delivery_status is not 'delivered':
        print('Trucks failed to deliver this package.', p.info())
    # format input into hours and minutes
    pkg_time_split = p.delivery_time.split(':')
    package_hours = int(pkg_time_split[0])
    package_minutes = int(p.delivery_time[-5:-3])/60
    package_time = package_hours + package_minutes
    # if package time is greater than start time and less than end time return p.info()
    if start_time < package_time < end_time:
        print(p.info())
