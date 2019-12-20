import csv

# import distance data
distance_table = './WGU Dist Table.csv'

# START clean distance data
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
# END clean distance data


# START print functions
def print_street_address_only():
    for a in address_hash:
        print(a)


# Graph class
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
                    d[v] = dist_tbl_hash[v - 2][
                        u + 2]  # subtract 2 from v and add 2 to u to correct for skipped lines
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
                row[j] = (j - 2, float(el))
        prepare_row_for_sort = row[2::]
        save_row = [row[0], row[1]]
        prepare_row_for_sort.sort(key=lambda x: x[1])
        save_row.append(prepare_row_for_sort)
        # print(save_row)
        new_dist_graph[i] = save_row
    return new_dist_graph


class Graph:
    """  Graph formats the distance data in dist_tbl_graph into a bidirectional graph

        class member bidirectional:
            presorted key:value pairs of address_id:mileage in ascending order by mileage
    """
    def __init__(self):
        self.bidirectional = build_bidirectional_distance_graph()
        self.distances_from_hub = []

        self.get_distances_from_hub()


    def get_distances_from_hub(self):
        """

        creates a list of distances in
            key:value pairs of address_id:miles_from_hub
        these key:value pairs will be used to insert into a circular route
        the packages with address ids closest to the hub will be inserted into to the
         beginning and end of the best_route array

        """
        for d in self.bidirectional:
            # print('d', d)
            for distances in d[2:]:
                # print('dist', distances)
                address_id = distances[0][0]
                for pairs in distances:
                    # print(pairs)
                    if pairs[0] == 0:
                        hub = pairs
            self.distances_from_hub.append((address_id, hub[1]))
        # remove hub
        self.distances_from_hub.pop(0)
        self.distances_from_hub.sort(key=lambda x: x[1])



g = Graph()
# print(g.distances_from_hub)

