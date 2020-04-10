# ****************************************************#
# Created By: Ravi Damodaran
# Organization: Vaayoo
# Link lists
# ****************************************************#

# Import the class Node from the file Linklists.py
from Linklists import Node


############ Functions in the program ####################
# A funtion to count the total number
# of nodes in the link lists
def count_nodes(head):
    # assuming that head != None
    count = 1                                           # counter for counting the number of nodes. Initial value is one
    current = head                                      # Implying the head object to variable current
    while current.next is not None:                     # A while loop loops while the node.next is not none
        current = current.next                          # Changing the current node to next linked node
        count += 1                                      # Incrementing the counter
    return count                                        # Returning the counter at the end of the loop


# A function to get the data from each node
def get_contents(node):
    return node.data                                    # Returns the data of the node from the node object


########## Start of Program ##############################


nodes = [Node(6),
         Node(3),
         Node(4),
         Node(2),
         Node(1)]

# A loop to connect the node links
index=0
for i in nodes:                                     # Iterating through the nodes dictionary, where i is the key value
    # print(i)
    try:                                            # There is chances to get error hence try and except used
        if index <(len(nodes)-1):                   # An if to compare the index is less than the length to avoid error in index addition
            nodes[index].next = nodes[index+1]      # Assigning the "next" variable in the object as the next object in dictionary
        if index >0:                                # An if to  compare the index is greater than 0 to avoid error in index subtraction
            nodes[index].prev = nodes[index - 1]    # Assigning the "prev" variable in the object as the previous object in dictionary
        index+=1
    except IndexError:
        pass                                        # Even if there is an error pass that and move to next step
        # print("An error occured")

# Print the length of the linked list
print("The linked list length is: " + str(count_nodes(nodes[1])))

# A for loop to print the data stored in the liked list
for node in nodes:
    print(get_contents(node))
# A for loop to print the contents and values of the attributes of the linked list
for node in nodes:
    print("Printing the values of Nodes\n" +
          "Data = " + str(node.data) + "\n" +
          "Next = " + str(node.next) + "\n" +
          "Previous = " + str(node.prev) + "\n"
          )
    # print(nodes[node])
