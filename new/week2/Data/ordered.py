from new.week2.Data.utility import readfile, update, write


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self) :
        self.head = None

    def addnode(self, data) :
        newnode = Node(data)
        if self.head == None :
            self.head = newnode
        else :
            tempnode = self.head
            while tempnode.next is not None :
                tempnode = tempnode.next
            tempnode.next = newnode

    def disply(self) :
        tempnode = self.head
        if tempnode is None :
            print("List is empty")
            return
        while tempnode.next is not None :
            print(tempnode.data, " ")
            tempnode = tempnode.next
        print(tempnode.data, " ")

    def sortlist(self, data) :
        newnode = Node(data)
        if self.head is None :
            self.head = newnode
        else :
            tempnode = self.head
            if tempnode.data > data :
                newnode.next = tempnode
                self.head = newnode
            else :
                prevnode = self.head
                while tempnode is not None :
                    if tempnode.data > data :
                        newnode.next = prevnode.next
                        prevnode.next = newnode
                        return
                    prevnode = tempnode
                    tempnode = tempnode.next
                prevnode.next = newnode


if __name__ == "__main__" :
    list = LinkedList()
    word = readfile('data.txt')
for item in word :
    list.addnode(item)
print("Current list is :")
list.disply()
val = raw_input("\nEnter a word to search:\n")
if list.search(val) :
    print("Element found and deleting from the file\n")
    word.remove(val)
    list.delete(val)
    write(word, 'data.txt')
    print(word)
else :
    print("Element not found in a list\n")
    word.append(val)
    list.addnode(val)
    list.sortlist(val)
    update(val, 'data.txt')
print("File updated success:\n")
list.sortlist()
list.disply()
