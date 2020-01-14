import csv

# import distance data
distance_table = './WGU Dist Table.csv'

"""
Start Format Distance Data

O(1)    SET EMPTY LIST dist_table_hash
O(1)    SET EMPTY LIST distances
O(1)    SET EMPTY LIST address_hash
        
        // open the file and clean the unnecessary information and spaces
        // https://stackoverflow.com/questions/57467837/what-is-time-complexity-of-python3s-open-function
            // open() returns a string file object which is a pointer to the actual data block in memory
O(1)    WITH OPEN(distance_table) AS dt
            // REMOVE new lines in strings from csv and REPLACE with empty strings
O(N)        SET STRING filtered = PYTHON BUILT IN FUCNTIONS line.replace('\n', '') for line in dt)
            // feed the filtered data into the python built in function `reader`
            SET STRING reader = PYTHON BUILT IN FUNCTION csv.reader(filtered)
            
            // row_id is hash for dist_tbl_hash
            SET INT row_id = 0
   
            // skip first row
O(1)        CALL readline() ON dt
            
            // append each row to dist_tbl_hash
O(N)        FOR EACH row IN reader:
                // hash each row with row_id and then row data
                
                // base case
O(1)            IF row_id == 0
                    THEN SET address_id = 0
O(N^2)                FOR EACH column IN row
O(1)                    IF column IS NOT 0
                            THEN
                            SET LIST temp_col = col
                            SET LIST column = [address_id + 1, temp]
                            
                            // set the current row as the new col data
                            SET LIST row[address_id] = column
                            
                            // increment address_id by 1
                            SET address_id = address_id + 1               
                        END IF
                    END FOR
                END IF
                
                SET LIST temp_list = LIST row_id
                // use built in function extend method to iterate over row and add each element of the row
                CALL EXTEND(row) ON LIST temp_list
                APPEND temp_list TO LIST dist_tbl_hash
                
                // increment row_id by 1
                SET row_id = row_id + 1
            END FOR
        END WTIH
TOTAL COMPLEXITY FOR BLOCK = O(N^2)
        
        //start new for loop for readability on dist_tbl_hash
O(N)    FOR EACH row IN dist_tbl_hash
            //base case - the hub
O(1)        IF row ELEMENT 0 is 0
                DELETE row[0]
                SET STRING street_address = "4001 South 700 East"
                
O(N)    FOR EACH LIST row IN LIST dist_tbl_hash:
            //    base case  //
O(1)        IF INT row[0] IS 0:
                DELETE row[0]
                SET STRING street_address = "4001 South 700 East"
                SET STRING row[0][1] = street_address
                APPEND LIST [1, street_address] TO LIST address_hash
            SET STRING s = TO_STRING(row[2])
            # https://stackoverflow.com/questions/10059554/inserting-characters-at-the-start-and-end-of-a-string
            SET STRING street_address = EMPTY STRING
            
            // https://mindmajix.com/python-enumerate-with-example
            // enumerate has a BIG O time complexity of O(N) because it iterates over the length of the list by an  //
            // index and then further making use of this index to get the value at the location:                    //
            //      EXAMPLE                                                                                         //            
            //      for i in length(list):                                                                          //            
            //         for j in length(i:                                                                           //
            //                  do stuff                                                                            //        
O(N^2)      FOR EACH character IN ENUMERATE(s)
O(1)            IF character IS "(":
                    # https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/
                    // extract zipcode                                          //
                    // i = location of "(" because of the IF statement above    //
                    // -1 = location of the last element in the list and is ")" //
                    SET STRING zipcode = s[i:-1]
                    
                    // extract street address from character
                    // get all characters up to the first "("
                    SET STRING street_address = s[1:(i)]
                    
                    SET STRING row[2] = street_address
                    APPEND LIST [row[0], street_address, zipcode] TO LIST address_hash
                    BREAK
                END IF
            END FOR
            
            // build distances_graph //
O(1)        IF row[0] IS NOT A LIST:
                SET LIST temp_list = [row[0]]
                
                // row[3::] is only the distances (miles) between points //
                EXTEND LIST temp_list WITH row[3::]
                APPEND LIST temp_list TO distances
            END IF
        
        // initialize counter for column numbers                //
        //    use for creating symmetrical graph                //
        //    if col is empty then replace with row[0] -> count //
O(N)    FOR EACH LIST row INT LIST distances:
            // fix last element from ' ' to '' //
            SET row[-1] = ''
O(N^3)      FOR EACH column IN ENUMERATE(row):
O(1)           IF column IS EMPTY STRING:

                    // get hash id for current_row  //
                    SET INT current_row_id = row[0]
                    
                    // set col to distance from distance A -> B //
                    // distances[i-1] is the previous row       //
                    // the index of the current_row is also the //
                    // index of the column of the previous row  //
                    // this is the way a bidirectional graph is //
                    SET STRING a_to_b = distances[i-1][current_row_id]
                    
                    // set the current_column (i) to the correct mileage (a_to_b) //
                    SET row[i] = a_to_b
                END IF
            END FOR
            
            // remove the row id because which serves as the location id        //
            // the location id (vertex) is assumed as the list element number   //
            // i.e row[0] (HUB) is index 0/location_id 0,                       // 
            //     row[1] index 1/location_id 1 ... row[N]                      //
            
            DELETE row[0]
            
        END FOR
        # END format distance data
B3:SPACE-TIME AND BIG-O
O(N^3)
"""
# hash for distances
dist_tbl_hash = []
# distance graph for algorithm
distances = []
# address hash
address_hash = []

# open the file and clean the unnecessary information and spaces
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
        # hash each row with row_id and row
        if row_id is 0:
            address_id = 0
            for col in row:
                if col is not 0:
                    temp = col
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
"""
START BUILD BIDIRECTIONAL DISTANCES GRAPH

        // SET STRING street_address FOR EACH NODE IN LIST dist_tbl_hash 
O(N)    FOR EACH row IN LIST dits_tbl_hash

            //base case - the hub - manually set address because csv file is weird
O(1)        IF row[0] IS 0:
                REMOVE FIRST ELEMENT
                SET street_address = "4001 South 700 East"
                SET LIST first_element OF LIST dist_tbl_hash AND second_element OF LIST first_element = street_address
                APPEND LIST [0 AND street_address] TO LIST address_hash
            END IF
            
            // initialize a variable to hold the street address for each remaining node in dist_tbl_hash - placeholder
                // to clean the zipcode off of the element
            SET STRING s = STRING ELEMENT 3 OF current_node
            SET STRING street_address = EMPTY STRING
            
O(N)       FOR EACH letter IN ENUMERATE(s)
                // find th"e first '(' to signal the start of the zipcode
O(1)            IF c IS "("
                    // extract zipcode - START at "(" and END before ")"
                    SET STRING zipcode = s[i+1:-1]
                    
                    // extract street address - START at first letter END end before "("       
                    SET STRING street_address = s[1:i]
                    
                    // remove zipcode from current node
                    SET current_node ELEMENT 2 = street_address
                    
                    APPEND LIST [address_id, street_address, zipcode] TO LIST address_hash
                    
                    BREAK
                END IF
            END FOR
            // build bidirectional distances_graph
            
            // convert each node to a list
O(1)        IF first_element OF current_node IS NOT A LIST
                THEN 
                SET LIST temporary_list = LIST first_element    
                SET LIST all_miles_in_current_node = current_node[3::] - START AT 4th ELEMENT END AT LAST ELEMENT
                EXTEND LIST temp_list WITH LIST all_miles_in_current_node
                APPEND LIST temp_list TO LIST distances 
            END IF
END BUILD BIDIRECTIONAL DISTANCES GRAPH
TOTAL BIG O = O(N^2)      
"""
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
            # extract zipcode from the street address
            address_id = row[0]
            zipcode = s[i+1:-1]
            street_address = s[1:i]
            row[2] = street_address
            address_hash.append([address_id, street_address, zipcode])
            break
    # build distances_graph
    if isinstance(row[0], list) is False:
        temp_list = [row[0]]
        all_miles_in_current_node = row[3::]
        temp_list.extend(all_miles_in_current_node)
        distances.append(temp_list)

"""
START ADD VERTEX IDS AND COMPLETE MILEAGE FOR EACH VERTEX
// used for quick access to each address in the distance graph
// if col is empty then replace with row[0] count

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Currently the distance_table looks like:
[1, '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[2, '7.2', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[3, '3.8', '7.1', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[4, '11.0', '6.4', '9.2', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[5, '2.2', '6.0', '4.4', '5.6', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[6, '3.5', '4.8', '2.8', '6.9', '1.9', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[7, '10.9', '1.6', '8.6', '8.6', '7.9', '6.3', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[8, '8.6', '2.8', '6.3', '4.0', '5.1', '4.3', '4.0', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[9, '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[10, '2.8', '6.3', '1.6', '7.3', '2.6', '1.5', '8.0', '9.3', '4.8', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[11, '6.4', '7.3', '10.4', '1.0', '6.5', '8.7', '8.6', '4.6', '11.9', '9.4', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[12, '3.2', '5.3', '3.0', '6.4', '1.5', '0.8', '6.9', '4.8', '4.7', '1.1', '7.3', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[13, '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.6', '5.1', '12.0', '4.7', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
[14, '5.2', '3.0', '6.5', '3.9', '3.2', '3.9', '4.2', '1.6', '7.6', '4.6', '4.9', '3.5', '7.3', '0.0', '', '', '', '', '', '', '', '', '', '', '', '', '']
[15, '4.4', '4.6', '5.6', '4.3', '2.4', '3.0', '8.0', '3.3', '7.8', '3.7', '5.2', '2.6', '7.8', '1.3', '0.0', '', '', '', '', '', '', '', '', '', '', '', '']
[16, '3.7', '4.5', '5.8', '4.4', '2.7', '3.8', '5.8', '3.4', '6.6', '4.0', '5.4', '2.9', '6.6', '1.5', '0.6', '0.0', '', '', '', '', '', '', '', '', '', '', '']
[17, '7.6', '7.4', '5.7', '7.2', '1.4', '5.7', '7.2', '3.1', '7.2', '6.7', '8.1', '6.3', '7.2', '4.0', '6.4', '5.6', '0.0', '', '', '', '', '', '', '', '', '', '']
[18, '2.0', '6.0', '4.1', '5.3', '0.5', '1.9', '7.7', '5.1', '5.9', '2.3', '6.2', '1.2', '5.9', '3.2', '2.4', '1.6', '7.1', '0.0', '', '', '', '', '', '', '', '', '']
[19, '3.6', '5.0', '3.6', '6.0', '1.7', '1.1', '6.6', '4.6', '5.4', '1.8', '6.9', '1.0', '5.4', '3.0', '2.2', '1.7', '6.1', '1.6', '0.0', '', '', '', '', '', '', '', '']
[20, '6.5', '4.8', '4.3', '10.6', '6.5', '3.5', '3.2', '6.7', '1.0', '4.1', '11.5', '3.7', '1.0', '6.9', '6.8', '6.4', '7.2', '4.9', '4.4', '0.0', '', '', '', '', '', '', '']
[21, '1.9', '9.5', '3.3', '5.9', '3.2', '4.9', '11.2', '8.1', '8.5', '3.8', '6.9', '4.1', '8.5', '6.2', '5.3', '4.9', '10.6', '3.0', '4.6', '7.5', '0.0', '', '', '', '', '', '']
[22, '3.4', '10.9', '5.0', '7.4', '5.2', '6.9', '12.7', '10.4', '10.3', '5.8', '8.3', '6.2', '10.3', '8.2', '7.4', '6.9', '12.0', '5.0', '6.6', '9.3', '2.0', '0.0', '', '', '', '', '']
[23, '2.4', '8.3', '6.1', '4.7', '2.5', '4.2', '10.0', '7.8', '7.8', '4.3', '4.1', '3.4', '7.8', '5.5', '4.6', '4.2', '9.4', '2.3', '3.9', '6.8', '2.9', '4.4', '0.0', '', '', '', '']
[24, '6.4', '6.9', '9.7', '0.6', '6.0', '9.0', '8.2', '4.2', '11.5', '7.8', '0.4', '6.9', '11.5', '4.4', '4.8', '5.6', '7.5', '5.5', '6.5', '11.4', '6.4', '7.9', '4.5', '0.0', '', '', '']
[25, '2.4', '10.0', '6.1', '6.4', '4.2', '5.9', '11.7', '9.5', '9.5', '4.8', '4.9', '5.2', '9.5', '7.2', '6.3', '5.9', '11.1', '4.0', '5.6', '8.5', '2.8', '3.4', '1.7', '5.4', '0.0', '', '']
[26, '5.0', '4.4', '2.8', '10.1', '5.4', '3.5', '5.1', '6.2', '2.8', '3.2', '11.0', '3.7', '2.8', '6.4', '6.5', '5.7', '6.2', '5.1', '4.3', '1.8', '6.0', '7.9', '6.8', '10.6', '7.0', '0.0', '']
[27, '3.6', '13.0', '7.4', '10.1', '5.5', '7.2', '14.2', '10.7', '14.1', '6.0', '6.8', '6.4', '14.1', '10.5', '8.8', '8.4', '13.6', '5.2', '6.9', '13.1', '4.1', '4.7', '3.1', '7.8', '1.3', '8.3', '']
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 // The purpose of this block of code is to fill in the empty strings with the corresponding mileage from the matching 
    node. In order to do this it is necessary to:
        hold the vertex id of the current node
        then look up the element number that matches the current node vertex id of the previous node
    In other words the column_id (element number) that matches the previous address_id will hold the distance from the 
    current_address to the previous_address.
    
    // set the distance from NODE A -> NODE B = matching_distance_in_corresponding_node
O(N)    FOR EACH row IN distances
            SET LAST ELEMENT to ''
O(N^2)      FOR EACH column IN ENUMERATE(row)
O(1)            IF column IS EMPTY
                    THEN 
                    // save current vertex id
                    SET INT current_vertex_id = INT row[0]
                    
                    // row[i-1] is the previous row
                    // column[current_vertex_id] of the previous row is the matching mileage
                    SET STRING a_to_b = STRING row[i-1][u]
                    
                    SET STRING row OF ELEMENT i = STRING a_to_b
                END IF
            END FOR
            
            // fix vertex id to be 0 based indexing
O(1)        DELETE row[0]
            
END ADD VERTEX IDS AND COMPLETE MILEAGE FOR EACH VERTEX           
TOTAL BIG O = O(N^2)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The bidirectional distance table now looks like this:
vertex_id/location_id is assumed as the row_id, python built in index is 0 based
from_current_location_to_hub = row[1]
from_current_location_to_location_1 = row[2]
....
from_current_location_to_location_N = row[N+1]

[0, '0.0', '7.2', '3.8', '11.0', '2.2', '3.5', '10.9', '8.6', '7.6', '2.8', '6.4', '3.2', '7.6', '5.2', '4.4', '3.7', '7.6', '2.0', '3.6', '6.5', '1.9', '3.4', '2.4', '6.4', '2.4', '5.0', '3.6']
[1, '7.2', '0.0', '7.1', '6.4', '6.0', '4.8', '1.6', '2.8', '4.8', '6.3', '7.3', '5.3', '4.8', '3.0', '4.6', '4.5', '7.4', '6.0', '5.0', '4.8', '9.5', '10.9', '8.3', '6.9', '10.0', '4.4', '13.0']
[2, '3.8', '7.1', '0.0', '9.2', '4.4', '2.8', '8.6', '6.3', '5.3', '1.6', '10.4', '3.0', '5.3', '6.5', '5.6', '5.8', '5.7', '4.1', '3.6', '4.3', '3.3', '5.0', '6.1', '9.7', '6.1', '2.8', '7.4']
[3, '11.0', '6.4', '9.2', '0.0', '5.6', '6.9', '8.6', '4.0', '11.1', '7.3', '1.0', '6.4', '11.1', '3.9', '4.3', '4.4', '7.2', '5.3', '6.0', '10.6', '5.9', '7.4', '4.7', '0.6', '6.4', '10.1', '10.1']
[4, '2.2', '6.0', '4.4', '5.6', '0.0', '1.9', '7.9', '5.1', '7.5', '2.6', '6.5', '1.5', '7.5', '3.2', '2.4', '2.7', '1.4', '0.5', '1.7', '6.5', '3.2', '5.2', '2.5', '6.0', '4.2', '5.4', '5.5']
[5, '3.5', '4.8', '2.8', '6.9', '1.9', '0.0', '6.3', '4.3', '4.5', '1.5', '8.7', '0.8', '4.5', '3.9', '3.0', '3.8', '5.7', '1.9', '1.1', '3.5', '4.9', '6.9', '4.2', '9.0', '5.9', '3.5', '7.2']
[6, '10.9', '1.6', '8.6', '8.6', '7.9', '6.3', '0.0', '4.0', '4.2', '8.0', '8.6', '6.9', '4.2', '4.2', '8.0', '5.8', '7.2', '7.7', '6.6', '3.2', '11.2', '12.7', '10.0', '8.2', '11.7', '5.1', '14.2']
[7, '8.6', '2.8', '6.3', '4.0', '5.1', '4.3', '4.0', '0.0', '7.7', '9.3', '4.6', '4.8', '7.7', '1.6', '3.3', '3.4', '3.1', '5.1', '4.6', '6.7', '8.1', '10.4', '7.8', '4.2', '9.5', '6.2', '10.7']
[8, '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.0', '4.8', '11.9', '4.7', '0.6', '7.6', '7.8', '6.6', '7.2', '5.9', '5.4', '1.0', '8.5', '10.3', '7.8', '11.5', '9.5', '2.8', '14.1']
[9, '2.8', '6.3', '1.6', '7.3', '2.6', '1.5', '8.0', '9.3', '4.8', '0.0', '9.4', '1.1', '5.1', '4.6', '3.7', '4.0', '6.7', '2.3', '1.8', '4.1', '3.8', '5.8', '4.3', '7.8', '4.8', '3.2', '6.0']
[10, '6.4', '7.3', '10.4', '1.0', '6.5', '8.7', '8.6', '4.6', '11.9', '9.4', '0.0', '7.3', '12.0', '4.9', '5.2', '5.4', '8.1', '6.2', '6.9', '11.5', '6.9', '8.3', '4.1', '0.4', '4.9', '11.0', '6.8']
[11, '3.2', '5.3', '3.0', '6.4', '1.5', '0.8', '6.9', '4.8', '4.7', '1.1', '7.3', '0.0', '4.7', '3.5', '2.6', '2.9', '6.3', '1.2', '1.0', '3.7', '4.1', '6.2', '3.4', '6.9', '5.2', '3.7', '6.4']
[12, '7.6', '4.8', '5.3', '11.1', '7.5', '4.5', '4.2', '7.7', '0.6', '5.1', '12.0', '4.7', '0.0', '7.3', '7.8', '6.6', '7.2', '5.9', '5.4', '1.0', '8.5', '10.3', '7.8', '11.5', '9.5', '2.8', '14.1']
[13, '5.2', '3.0', '6.5', '3.9', '3.2', '3.9', '4.2', '1.6', '7.6', '4.6', '4.9', '3.5', '7.3', '0.0', '1.3', '1.5', '4.0', '3.2', '3.0', '6.9', '6.2', '8.2', '5.5', '4.4', '7.2', '6.4', '10.5']
[14, '4.4', '4.6', '5.6', '4.3', '2.4', '3.0', '8.0', '3.3', '7.8', '3.7', '5.2', '2.6', '7.8', '1.3', '0.0', '0.6', '6.4', '2.4', '2.2', '6.8', '5.3', '7.4', '4.6', '4.8', '6.3', '6.5', '8.8']
[15, '3.7', '4.5', '5.8', '4.4', '2.7', '3.8', '5.8', '3.4', '6.6', '4.0', '5.4', '2.9', '6.6', '1.5', '0.6', '0.0', '5.6', '1.6', '1.7', '6.4', '4.9', '6.9', '4.2', '5.6', '5.9', '5.7', '8.4']
[16, '7.6', '7.4', '5.7', '7.2', '1.4', '5.7', '7.2', '3.1', '7.2', '6.7', '8.1', '6.3', '7.2', '4.0', '6.4', '5.6', '0.0', '7.1', '6.1', '7.2', '10.6', '12.0', '9.4', '7.5', '11.1', '6.2', '13.6']
[17, '2.0', '6.0', '4.1', '5.3', '0.5', '1.9', '7.7', '5.1', '5.9', '2.3', '6.2', '1.2', '5.9', '3.2', '2.4', '1.6', '7.1', '0.0', '1.6', '4.9', '3.0', '5.0', '2.3', '5.5', '4.0', '5.1', '5.2']
[18, '3.6', '5.0', '3.6', '6.0', '1.7', '1.1', '6.6', '4.6', '5.4', '1.8', '6.9', '1.0', '5.4', '3.0', '2.2', '1.7', '6.1', '1.6', '0.0', '4.4', '4.6', '6.6', '3.9', '6.5', '5.6', '4.3', '6.9']
[19, '6.5', '4.8', '4.3', '10.6', '6.5', '3.5', '3.2', '6.7', '1.0', '4.1', '11.5', '3.7', '1.0', '6.9', '6.8', '6.4', '7.2', '4.9', '4.4', '0.0', '7.5', '9.3', '6.8', '11.4', '8.5', '1.8', '13.1']
[20, '1.9', '9.5', '3.3', '5.9', '3.2', '4.9', '11.2', '8.1', '8.5', '3.8', '6.9', '4.1', '8.5', '6.2', '5.3', '4.9', '10.6', '3.0', '4.6', '7.5', '0.0', '2.0', '2.9', '6.4', '2.8', '6.0', '4.1']
[21, '3.4', '10.9', '5.0', '7.4', '5.2', '6.9', '12.7', '10.4', '10.3', '5.8', '8.3', '6.2', '10.3', '8.2', '7.4', '6.9', '12.0', '5.0', '6.6', '9.3', '2.0', '0.0', '4.4', '7.9', '3.4', '7.9', '4.7']
[22, '2.4', '8.3', '6.1', '4.7', '2.5', '4.2', '10.0', '7.8', '7.8', '4.3', '4.1', '3.4', '7.8', '5.5', '4.6', '4.2', '9.4', '2.3', '3.9', '6.8', '2.9', '4.4', '0.0', '4.5', '1.7', '6.8', '3.1']
[23, '6.4', '6.9', '9.7', '0.6', '6.0', '9.0', '8.2', '4.2', '11.5', '7.8', '0.4', '6.9', '11.5', '4.4', '4.8', '5.6', '7.5', '5.5', '6.5', '11.4', '6.4', '7.9', '4.5', '0.0', '5.4', '10.6', '7.8']
[24, '2.4', '10.0', '6.1', '6.4', '4.2', '5.9', '11.7', '9.5', '9.5', '4.8', '4.9', '5.2', '9.5', '7.2', '6.3', '5.9', '11.1', '4.0', '5.6', '8.5', '2.8', '3.4', '1.7', '5.4', '0.0', '7.0', '1.3']
[25, '5.0', '4.4', '2.8', '10.1', '5.4', '3.5', '5.1', '6.2', '2.8', '3.2', '11.0', '3.7', '2.8', '6.4', '6.5', '5.7', '6.2', '5.1', '4.3', '1.8', '6.0', '7.9', '6.8', '10.6', '7.0', '0.0', '8.3']
[26, '3.6', '13.0', '7.4', '10.1', '5.5', '7.2', '14.2', '10.7', '14.1', '6.0', '6.8', '6.4', '14.1', '10.5', '8.8', '8.4', '13.6', '5.2', '6.9', '13.1', '4.1', '4.7', '3.1', '7.8', '1.3', '8.3', '']
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# initialize counter for vertex ids
    # use for creating symmetrical graph
    # if col is empty then replace with row[0] -> count
for row in distances:
    # fix last element from ' ' to ''
    row[-1] = ''
    for i, col in enumerate(row):
        if col is '':
            # get hash id for row
            u = row[0]
            # set col to distance from distance A -> B
            a_to_b = distances[i-1][u]

            row[i] = a_to_b
    # remove vertex_id, location_id is assumed to be row_id
    del row[0]

# convert all miles to type float
i = 0
for row in distances:
    j =0
    for col in row:
        if i == 26 and j == 26:
            break
        print(i, j, col)
        col = float(col)
        j += 1
    i += 1


"""
    DEFINE PRINT FUNCTION print_street_address_only()
    
O(N)    FOR EACH LIST address IN address_hash:
            // address = [location_id, street_address, zipcode]
            PRINT(address)
"""
def print_street_address_only():
    for a in address_hash:
        print(a)



""" 
CLASS GRAPH

// helper function for class graph  //
        DEFINE FUNCTION build_bidirectional_graph()
            // first line is a boolean flag used to skip the first line of the csv file //
            SET BOOLEAN first_line = True
            
            // build the distance graph
            SET LIST new_dist_graph TO EMPTY LIST
            
            // u = row index    //
            // v = column index //
O(N^2)      FOR EACH vertex IN ENUMERATE(u, dist_tbl_hash)
                // skip first line
O(1)            IF BOOLEAN first_line IS TRUE
                    SET BOOLEAN first_line = FALSE
                    CONTINUE
                END IF
                
                FOR EACH miles IN ENUMERATE(v, dist_tbl_hash[u])
            
"""
def build_bidirectional_distance_graph():
    distances_only_table = dist_tbl_hash[1:]
    for t in distances_only_table:
        del t[0]
        del t[0]
        del t[0]

    # create new distance graph
    new_dist_graph = []
    # u = row index
    # v = 1 => column index, 1 to skip the first column which is already set in each vertex
    u = 0
    v = 1
    for d in distances_only_table:
        # v = column index
        for e in distances_only_table[u]:
            if e is '':
                #  find corresponding value in row to build bidirectional graph
                # offset d[v] by negative one for zero based indexing
                d[v-1] = float(dist_tbl_hash[v][u])  # subtract 2 from v and add 2 to u to correct for skipped lines
            v += 1
        v = 1
        u += 1

        new_dist_graph.append(d)
        new_dist_graph.sort()

        # convert all strings to float
        for row in new_dist_graph:
            for col in row:
                col = float(col)

    return new_dist_graph


class Graph:
    """  Graph formats the distance data in dist_tbl_graph into a bidirectional graph

        class member bidirectional:
            presorted key:value pairs of address_id:mileage in ascending order by mileage
    """
    def __init__(self):
        # data
        self.adjacency_list = distances
        self.sorted_bidirectional = build_bidirectional_distance_graph()
        self.distances_from_hub = []
        self.address_list = address_hash

g = Graph()
