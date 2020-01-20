import package_info
import trucks
"""
G.  Provide an interface for the insert and look-up functions to view the status of any package at any time. 
This function should return all information about each package, including delivery status.

1.  Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.

2.  Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.

3.  Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.
"""


def format_time(time):
    if 8 < len(time) < 7:
        print("INVALID ENTRY. PLEASE TRY AGAIN.")
        look_up_package()

    meridies = time[-2:]
    st_split = time.split(':')
    hour = int(st_split[0])
    minutes = int(time[-5:-3])

    if hour not in range(1, 24, 1):
        print("INVALID HOUR. PLEASE TRY AGAIN.")
        look_up_package()

    if minutes not in range(0, 60, 1):
        print("INVALID MINUTES. PLEASE TRY AGAIN.")
        look_up_package()
    # get minutes in decimal format
    minutes = minutes / 60

    if meridies.upper() not in ['AM', 'PM']:
        print("INVALID MERIDIES. PLEASE TRY AGAIN.")
        look_up_package()

    if meridies.upper() == 'PM':
        if hour == 12:
            hour = hour
        else:
            hour = hour + 12

    time = hour + minutes
    return time


def look_up_package():
    get_user_need = -1
    while get_user_need is not 'exit':
        # Create a user menu with two inputs:
        #   1. to look up all information for a single package
        #   2. to look up all information for all packages
        get_user_need = \
            input("USER MENU:\n"
                  "To look up all the information about ONE package: TYPE 1\n"
                  "To look up all the information about ALL packages: TYPE 2\n"
                  "To exit the program: TYPE exit\n"
                  ">")

        if get_user_need.lower() not in ['1', '2', 'exit']:
            print("IMPROPER INPUT. PLEASE TRY AGAIN.")
            look_up_package()

        if get_user_need.lower() == 'exit':
            print("Goodbye.")
            return

        if get_user_need == '1':
            package_id = input("Enter the package id of the package you would like to look up.")

        start_time = input("Enter the start time in the format HH:MM AM or PM (8:00 AM)")
        end_time = input("Enter the end time in the format HH:MM AM or PM (8:00 PM)")


        # save start and end time as strings for printing later
        start_time_string = start_time
        end_time_string = end_time
        print("PACKAGE INFO BETWEEN TIMES", start_time_string, "AND", end_time_string + ".")
        # split start and end time strings into hours and minutes
        start_time = format_time(start_time)
        end_time = format_time(end_time)

        # initialize adn set a status_list to hold packages that are en_route and delivered
        status_list = []

        # Print package information
        for p in package_info.master_package_list:

            # IF the package was undelivered THEN PRINT to the user of undelivered package
            if p.delivery_time is '':
                print('Trucks failed to deliver this package.', p.info())

            # format STRING package load time into INT hours and INT minutes
            load_time = format_time(p.load_time)

            # format STRING package delivery time into INT hours and INT minutes
            delivery_time = format_time(p.delivery_time)

            # IF load time IS NOT EMPTY AND FLOAT start time <= FLOAT load time AND FLOAT delivery time > FLOAT end time
            #   THEN
            #   APPEND INT package.package_id_number TO LIST status_list
            #   SET CLASS PACKAGE DATA MEMBER STRING package.delivery_status = 'en route'
            if p.load_time is not '' and (start_time >= load_time) and (delivery_time > end_time):
                status_list.append(p.package_id_number)
                p.delivery_status = 'en route'

            # IF package.delivery_time IS NOT EMPTY AND delivery_ time < end_time
            #   THEN
            #   APPEND INT package.package_id_number TO LIST status_list
            #   SET CLASS PACKAGE DATA MEMBER STRING package.delivery_status = 'delivered'
            if p.delivery_time is not '' and delivery_time < end_time:
                status_list.append(p.package_id_number)
                p.delivery_status = 'delivered'

            # IF package.package_id_number IS NOT IN status_list
            #   //If the package is not in the status list then it must be the last option of 'at hub' and is not yet
            #   //loaded on a truck
            #   THEN
            #   SET CLASS PACKAGE DATA MEMBER STRING package.delivery_status = 'at hub'
            #   SET CLASS PACKAGE DATA MEMBER STRING package.loaded_on_truck = 'TBD' (to be decided)
            if p.package_id_number not in status_list:
                p.delivery_status = 'at hub'
                p.loaded_on_truck = 'TBD'

            # IF need IS STR '1'
            #   //print information for the package id that the user input
            #   IF package.package_id_number == int(package_id)
            #       THEN PRINT CALL FUNCTION package.info()
            #       RETURN
            if get_user_need == '1':
                if p.package_id_number == int(package_id):
                    print(p.info())
                    break
            # IF need IS '2'
            #   //print information for all packages
            #   THEN PRINT CALL FUNCTION package.info()
            if get_user_need == '2':
                print(p.info())

def check_for_late_packages():
    for p in package_info.master_package_list:
        if p.delivery_deadline and p.delivery_deadline < p.delivery_time:
            late_packages_flag = False
        else:
            late_packages_flag = True
            "THERE ARE LATE PACKAGES!"
    if late_packages_flag:
        ("Package", p.package_id_number, "was delivered late.")
    else:
        print("All packages were delivered ON TIME.")
check_for_late_packages()
look_up_package()




