import csv

# from packages import *

distance_table = './WGU Dist Table.csv'

dist_tbl_hash = []
# distance graph for algorithm
distances = []
# address hash
address_hash = []
with open(distance_table) as dt:
    # remove new line \n
    filtered = (line.replace('\n', '') for line in dt)
    reader = csv.reader(filtered)
    # row_id is hash for dist_tbl_hash
    row_id = 0
    # skip first row
    dt.readline()
    # append each row to dist_tbl_hash
    for row in reader:
        # print(row)
        # hash each row with row_id and row
        if row_id is 0:
            address_id = 0
            for col in row:
                if col is not 0:
                    temp = col
                    # print(col)
                    # print(temp)
                    col = [address_id + 1, temp]
                    row[address_id] = col
                    address_id += 1

        temp_list = [row_id]
        # use built in extend method to iterate over row and add each element of the row
        temp_list.extend(row)
        dist_tbl_hash.append(temp_list)
        row_id += 1
        # for col in row:
        #     # v = col

    # set variables for insert function
    # delivery_address, delivery_deadline, delivery_city, delivery_state, delivery_zip_code, package_weight,
    #                delivery_status

u = 0
v = 0


for row in dist_tbl_hash:
    if row[0] is 0:
        del row[0]
        street_address = "4001 South 700 East"
        row[0][1] = street_address
        address_hash.append([1, street_address])
    s = str(row[2])
    # https://stackoverflow.com/questions/10059554/inserting-characters-at-the-start-and-end-of-a-string
    street_address = ""
    for i, c in enumerate(s):
        if c is "(":
            # https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/
            # clean the street address of it's zipcode
            street_address = s[1:(i)]
            row[2] = street_address
            address_hash.append([row[0], street_address])
            # print(address_hash)
            break
    # build distances_graph
    if isinstance(row[0], list) is False:
        temp_list = [row[0]]
        temp_list.extend(row[3::])
        distances.append(temp_list)
    u += 1
    v += 1

# initialize counter for column numbers
    # use for creating symmetrical graph
    # if col is empty then replace with row[0] -> count
for row in distances:
    # fix last element from ' ' to ''
    row[-1] = ''
    for i, col in enumerate(row):
        if col is '':
            # get hash id for row
            u = row[0]
            # set col to distance from distance b -> a
            # print(distances[count - 1][u])
            a_to_b = distances[i - 1][u]
            row[i] = a_to_b


# print address_hash
def print_street_address_only():
    for a in address_hash:
        print(a)


# build distance graph for algorithm
def build_bidirectional_distance_graph():
    # test variables
    first_line = True
    empty = ''

    # create new distance graph
    new_dist_graph = []
    for u, d in enumerate(dist_tbl_hash):
        if first_line:  # skip key:address line
            first_line = False
            continue
        for v, e in enumerate(dist_tbl_hash[u]):
            # if v is 1:
                # print(dist_tbl_hash[u][v])
                # del dist_tbl_hash[u][v]
            # skip first three elements
            if v > 2:
                if e is '':
                    #  find corresponding value in row to build bidirectional graph
                    d[v] = dist_tbl_hash[v - 2][u + 2] # subtract 2 from v and add 2 to u to correct for skipped lines
                    # print(dist_tbl_hash[v][u + 2])
        new_dist_graph.append(d)

    #  for each row in new_dist_graph
    #       delete address in each row
    #       key:value pairs for address_id:mileage
    for row in new_dist_graph:
        row[0] = row[0] - 1
        del row[1]
    for i, row in enumerate(new_dist_graph):
        for j, el in enumerate(row):
            if j > 1:
                row[j] = (j-2, float(el))
        prepare_row_for_sort = row[2::]
        save_row = [row[0], row[1]]
        prepare_row_for_sort.sort(key=lambda x: x[1])
        save_row.append(prepare_row_for_sort)
        print(save_row)
        new_dist_graph[i] = save_row
    return new_dist_graph
# build_bidirectional_distance_graph()


# set dist_tbl_hash to new bidirectional graph
dist_tbl_hash = build_bidirectional_distance_graph()

def get_distances_from_hub():
    """

    creates a list of distances in
        key:value pairs of address_id:miles_from_hub
    these key:value pairs will be used to insert into a circular route
    the packages with address ids closest to the hub will be inserted into to the
     beginning and end of the best_route array

    """
    disances_from_hub = []
    for d in dist_tbl_hash:
        for distances in d[1:]:
            address_id = distances[0][0]
            for pairs in distances:
                if pairs[0] == 0:
                    hub = pairs
        disances_from_hub.append((address_id, hub[1]))
    # remove hub
    disances_from_hub.pop(0)
    disances_from_hub.sort(key=lambda x: x[1])
    return disances_from_hub


# print(get_distances_from_hub())


# print entire dist_table_hash
def print_dist_table_hash():
    for i, d in enumerate(dist_tbl_hash):
        print('f', dist_tbl_hash[i])
# print_dist_table_hash()

# print key:address list
def print_address_keys():
    for row in dist_tbl_hash:
        print(row[0], row[1])
# print_address_keys()


# helper function to take second element for a sort
def take_second(elem):
    return elem[1]


# function to hash and sort a row for distances in ascending order
def sort_graph_for_shortest_distances(row):
    temp_address_id = 1
    # put each row of distance graph in ascending order
    # must keep track of original positions
    for col in row[1:]:
        sorted_dist = row
        # add hash to column to keep track of original location
        sorted_dist[temp_address_id] = (temp_address_id, col)
        # if dist_graph[0][temp_address_id][1] < dist_graph[0][temp_address_id + 1][1]
        temp_address_id += 1
    # remove first element from the sorted_dist row
    sorted_dist.pop(0)
    sorted_dist.sort(key=take_second)
    # temp_graph.sort(key=takeSecond)
    return sorted_dist


# build a sorted distance graph for easier access to the data and program readability
def build_shortest_dists_graph(dist_graph):
    # initialize shortest distances graph
    shortest_dists = []
    # sort rows of dist_graph for shortest distances then append to shortest_dists graph
    for row in dist_graph:
        sorted_row = sort_graph_for_shortest_distances(row)
        shortest_dists.append(sorted_row)
    return shortest_dists


# nearest neighbor algorithm

# initialize and set empty visited locations list
visited_locations = []
# initialize and set empty closest location
current_location = 1
count = 0
# find the package with the closest location relative to current location
def find_next_location(address_list, location, count):
    # build graph of shortest distance in ascending order
    shortest_dists = build_shortest_dists_graph(distances.distances)
    # go to first address from HUB
    # find any package(s) with address ID 21
    distance_driven = 0
    next_location = -1
    # define and set counter
    # todo test for accuracy
    for p in address_list:
        # p[0] is package id
        pkg_id = p[0]
        # p[1] is location id
        p_del_id = p[1]
        # find the nearest neighbor
        next_location = shortest_dists[0][1][0]
        # keep track of visited locations with an array
        visited_locations.append(shortest_dists[0][1][0])
        # the next location id that is not 1 in the list
        if location is 1:
            print('if1')
            print('  c', count)
            # find the shortest distance from the current location
            shortest_dist_miles = shortest_dists[location][count][1]
            distance_driven += float(shortest_dist_miles)
            print("  if1-sd1:", shortest_dist_miles)
        # all other locations besides the HUB (address_id 1)
        if location is not 1:
            print('if2')
            print('  c', count)
            shortest_dist_miles = shortest_dists[next_location][count][1][1]
            print("  if2-sd2:", shortest_dist_miles)
            if count is 2:
                print('  if-if')
                distance_driven = distance_driven + float(shortest_dist_miles)
            else:
                print('  if - else :', shortest_dist_miles)
                distance_driven = distance_driven + float(shortest_dist_miles[1])
                print("  dist driven: ", distance_driven)
        print("sd2outer:", shortest_dist_miles)
        curr_location = next_location
        get_distance_to_closest_location(address_list, curr_location, count)
        next_location = shortest_dists[curr_location][1][0]

    return next_location



# time to get to location (18mi/hr)
#  todo fix me
def get_time_to_location(miles):
    miles_per_hour = 18
    minutes_per_hour = 60
    seconds_per_minute = 60
    distance = miles
    time = miles/18
    return time


def get_distance_to_closest_location(dist_graph, location, count):
    count = count + 1
    # current_location = 1
    # print("distg:", dist_graph)
    # print("alist:", address_ids_list)
    # find next closest location
    closest_location = find_next_location(address_ids_list, location, count)
    # calculate time to get there
    print("c", closest_location)


# print_street_address_only()
# build_bidirectional_distance_graph()
# print_dist_table_hash()
# print_address_keys()
# create a list of distances between pairs
