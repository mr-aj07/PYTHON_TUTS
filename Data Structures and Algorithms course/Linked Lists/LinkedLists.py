#Class to create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        #Create a node
        new_node = Node(value) #Calls the Node class to create the new node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):     # Add item to the end of the LL: O(n)
        #Create a Node
        new_node = Node(value)
        if self.head is None:    #In case the structure is empty and both head and tail point to None
            self.head = new_node  # Make the head point to the node to be appended
            self.tail = new_node   #Make the Tail point to the node to be appended
        else:
            self.tail.next = new_node # Make Last node point to the new node
            self.tail = new_node   #Make the Tail point to the node to be appended
        self.length += 1
        return True

    def Print_List(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print("\n")

    def Pop_List(self):                # Remove Last item of the LL: O(n)
        if self.length == 0:           #In case the list is empty
            #print("No Item to pop!!")
            return None
        else:
            temp = self.head            # Make two temporary variables equal to head
            pre = self.head
            while temp.next is not None:     # Loop to check while the node does not point to the node
                pre = temp                    
                temp=temp.next                # Move to the next node
                if temp.next == None:         #If the node points to none,
                    self.tail = pre           # Make pre equal to tail,
                    self.tail.next = None     # And then make that tail point to None
                    break
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
            
    def prepend(self, value):     # Add Element to the start of the LL: O(1)
        #Create a node
        new_node = Node(value)
        #Add node to beginning
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            new_node.next = self.head  # make the new node point to the head
            self.head = new_node       # Make the head equal to the new node
        self.length += 1
        return True

    def Pop_First(self):     # Pop the first Element of the LL: O(1)
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp
    
    def Get(self, index):  # To get a value at an index: O(n)
        if index<0 or index>=self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp

    def set_value(self, index, value):   #Set value at an index
        if index<0 or index>=self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        temp.value = value
                   
    def Insert(self, index, value):  #Insert value at an index
        #Create a node
        new_node = Node(value)
        #Insert a node
        if index<0 or index>self.length:
            return None

        elif index==0:
            return self.prepend(value)
        
        elif index == self.length:
            return self.append(value)
        
        else:
            # temp = self.head
            # for _ in range(index-1):    
            #     temp = temp.next
            temp = self.Get(index-1)
            new_node.next = temp.next
            temp.next = new_node
    
        self.length += 1
        return True

    def Remove(self, index):  # Removes an element at an index
        if index<0 or index>=self.length:
            return None
        
        elif index==0:
            return self.Pop_First()

        elif index == self.length-1:
            return self.Pop_List()
        
        else:
            pre = self.Get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None

        self.length -= 1
        return temp



            
            

            


'''         Testing Methods        '''

'''
def MakeLinkedList():
    a = input("Enter the First element of the linked List: ")
    My_Linked_List = LinkedList(a)
    while True:
        b = input("Enter the next element of the linked List: ")
        if a=="ok" or a=="OK" or a=="Ok":
            break
        else:
            My_Linked_List = LinkedList.append(b)
    
    return My_Linked_List
'''

Linked_List1 = LinkedList(1)  #Calls the class new node and assigns 4 as the value of the new node
Linked_List1.append(2)  # Appends the value of 2 in the Linked List
#Linked_List1.Print_List()

# Pop Method Test
# print(Linked_List1.Pop_List()) # When two nodes present
# print(Linked_List1.Pop_List()) # When single node present
# print(Linked_List1.Pop_List()) # When no node present

#LL1 = MakeLinkedList()
#print(LL1.Print_List())

''' Pop First'''
# print(Linked_List1.Pop_First())
# print(Linked_List1.Pop_First())
# print(Linked_List1.Pop_First())

LL3 = LinkedList(0)
for i in range(1,20):
    if i%2 == 0:
        LL3.append(i)

''' Insert Element'''
LL3.Print_List()
#print(LL3.get(3).value)
LL3.Insert(4, 7)
LL3.Print_List()

LL3.Remove(8)
LL3.Print_List()



