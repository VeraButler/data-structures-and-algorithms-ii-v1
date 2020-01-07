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
# for p in package_info.master_package_list:
#     print('loaded', p.package_id_number, p.load_time)
#     print('delivered', p.delivery_time)
start_time = input("Enter the start time in the format HH:MM AM or PM (8:00 AM)")
end_time = input("Enter the end time in the format HH:MM AM or PM (8:00 PM)")
# save start and end time as strings for printing later
start_time_string = start_time
end_time_string = end_time

# split start and end time strings into hours and minutes
st_split = start_time.split(':')
start_time_hour = int(st_split[0])
start_time_minutes = int(start_time[-5:-3])/60
start_time = start_time_hour + start_time_minutes

end_time_split = end_time.split(':')
end_time_hours = int(end_time_split[0])
end_time_minutes = int(end_time[-5:-3])/60
end_time = end_time_hours + end_time_minutes



"""
G.  Provide an interface for the insert and look-up functions to view the status of any package at any time. 
This function should return all information about each package, including delivery status.

1.  Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.

2.  Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.

3.  Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.
"""

print('PACKAGES DELIVERED BETWEEN', start_time_string, 'AND', end_time_string)
status_list = []
for p in package_info.master_package_list:
    # check for missed packages
    if p.delivery_time is '' or p.delivery_status is not 'delivered':
        print('Trucks failed to deliver this package.', p.info())

    # format STRING package load time into INT hours and INT minutes
    lt_split = p.load_time.split(':')
    load_time_hour = int(lt_split[0])
    load_time_minutes = int(p.load_time[-5:-3]) / 60

    load_time = load_time_hour + load_time_minutes

    # format STRING package delivery time into INT hours and INT minutes
    pkg_time_split = p.delivery_time.split(':')
    delivery_hours = int(pkg_time_split[0])
    delivery_minutes = int(p.delivery_time[-5:-3])/60

    delivery_time = delivery_hours + delivery_minutes

    if p.load_time is not '' and (start_time >= load_time) and (delivery_time > end_time):
        status_list.append(p.package_id_number)
        print('Package #' + str(p.package_id_number), 'status: en route')

    if p.delivery_time is not '' and delivery_time < end_time:
        status_list.append(p.package_id_number)
        print('Package #' + str(p.package_id_number), 'status: delivered')

    if p.package_id_number not in status_list:
        print('Package #' + str(p.package_id_number), 'status: at hub')




