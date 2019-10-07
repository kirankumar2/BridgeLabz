class Node(object) :

    def __init__(self, d, n=None) :
        self.data = d
        self.next_node = n

    def get_next(self) :
        return self.next_node

    def set_next(self, n) :
        self.next_node = n

    def get_data(self) :
        return self.data

    def set_data(self, d) :
        self.data = d

    def has_next(self) :
        if self.get_next() is None :
            return False
        return True

    def to_string(self) :
        return "Node value: " + str(self.data)


class LinkedList(object) :

    def __init__(self, r=None) :
        self.root = r
        self.size = 0

    def get_size(self) :
        return self.size

    def add(self, d) :
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def add_node(self, n) :
        n.set_next(self.root)
        self.root = n
        self.size += 1

    def remove(self, d) :
        this_node = self.root
        prev_node = None

        while this_node is not None :
            if this_node.get_data() == d :
                if prev_node is not None :
                    prev_node.set_next(this_node.get_next())
                else :
                    self.root = this_node.get_next()
                self.size -= 1
                return True  # data removed
            else :
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d) :
        this_node = self.root
        while this_node is not None :
            if this_node.get_data() == d :
                myList.remove(d)
            else :
                file.add(d)

    def print_list(self) :
        print("Print List..........")
        if self.root is None :
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next() :
            this_node = this_node.get_next()
            print(this_node.to_string())

    def sort(self) :
        if self.size > 1 :
            newlist = []
            current = self.root
            newlist.append(self.root)
            while current.has_next() :
                current = current.get_next()
                newlist.append(current)
            newlist = sorted(newlist, key=lambda node : node.get_data(), reverse=True);
            newll = LinkedList()
            for node in newlist :
                newll.add_node(node)
            return newll
        return self


def main() :
    myList = LinkedList()
    file = list()
    with open('text.txt', 'r') as fn :
        file = fn.read().split()
    for i in file :
        # file.add_node(i)
        myList.add(i)
    print("size=" + str(myList.get_size()))
    myList.print_list()
    myList = myList.sort()
    myList.print_list()
    d = input("enter the word to search")
    myList.find(d)

    print("size=" + str(myList.get_size()))
    print("size=" + str(myList.get_size()))
    #print("Find 25", myList.find(25))
    myList.print_list()


main()
