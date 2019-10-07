
from new.week2.Data.utility import readfile, update, write


class Node :  # class to create node for a list
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkedList :  # linked list class /link list operational classs
    def __init__(self) :
        self.head = None

    def addnode(self, data) :  # adding new node
        newnode = Node(data)
        if self.head == None :
            self.head = newnode
        else :
            tempnode = self.head
            while tempnode.next is not None :
                tempnode = tempnode.next
            tempnode.next = newnode

    def disply(self) :  # displaying nodes which present in a list
        tempnode = self.head
        if tempnode is None :
            print("List is empty")
            return
        while tempnode.next is not None :
            print(tempnode.data, " ")
            tempnode = tempnode.next
        print(tempnode.data, " ", )

    def search1(self, data) :  # Seaching for the node to find string equal or not
        self.disply()
        tempnode = self.head
        print(data)
        while tempnode is not None :
            if tempnode.data == data :
                return True
            tempnode = tempnode.next
        return False

    def delete1(self, data) :  # delete node in a list
        prvnode = tempnode = self.head
        if tempnode.data == data :
            self.head = tempnode.next
        else :
            while tempnode.data != data :
                prvnode = tempnode
                tempnode = tempnode.next
            prvnode.next = tempnode.next


if __name__ == "__main__" :
    list = LinkedList()
    word = readfile('text.txt')
    for item in word :
        list.addnode(item)
    print("Current list is :")
    list.disply()
    val = input("\nEnter a word to search:\n")
    if list.search1(val):
        print("Element found and deleting from the file\n")
        word.remove(val)
        list.delete1(val)
        write(word, 'file.txt')
    else :
         print("Element not found in a list\n")
         word.append(val)
         list.addnode(val)
         update(val, 'file.txt')  # updating string into file
print("File updated success:\n")
list.disply()
