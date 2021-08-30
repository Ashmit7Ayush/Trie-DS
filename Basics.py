class Node:
    def __init__(self) -> None:
        self.child=[None for x in range(26)]
        self.is_end=False


class Trie:
    def __init__(self)->None:
        # this is root
        self.root = Node()

    # search
    def search(self, string):
        temp = self.root

        # traverse through all the string 
        for x in string:
            # find the index
            index = ord(x)-ord('a')

            # chek if the index is there or not
            if temp.child[index]==None:
                return False

            # have the temp that is update it
            temp=temp.child[index]

        # we have to check the temp is end or not
        return temp.is_end

    # insert
    def insert(self, string):
        temp = self.root

        for x in string:
            # have the index to be searched
            index = ord(x)-ord('a')

            if temp.child[index]==None:
                temp.child[index]=Node()

            temp = temp.child[index]

        # make it as the keyword
        temp.is_end=True

    
    # node check for the empty
    def empty_node(self, node):
        for x in range(26):
            if node.child[x]==True:
                return False

        return True


    # delete
    def delete(self, node, string, index):
        # check for the node
        if not node:
            return node
        else:
            # check for the index match with the ength of the stsring
            if index==len(string):
                # amke the end to be the False
                node.is_end=False

                # fursther check for the that no any child of this node 
                if self.empty_node(node):
                    node=None

                return node

            else:
                # first check for the index
                i = ord(string[index])-ord('a')

                # go and  look for the node at index i and processs recursively
                node.child[i] = self.delete(node.child[i], string, index+1)

                # now after the success delete now check for the node is not having any another node or character
                if self.empty_node(node) and not node.is_end and node!=self.root:
                    node=None

                return node

    # prefix 
    def prefix_search(self, prefix):
        # try to find the prefix
        temp = self.root
        
        for x in prefix:
            index = ord(x)-ord('a')
            
            # check if it is present or not
            if not temp.child[index]:
                return 
            
            temp = temp.child[index]

        self.print_after_prefix(temp, prefix)

    # for prefix
    def print_after_prefix(self, temp, prefix):
        if temp.is_end:
            print(prefix)

        for x in range(26):
            if temp.child[x]:
                self.print_after_prefix(temp.child[x], prefix+chr(97+x))
        
        

            
            


if __name__=='__main__':
    trie = Trie()
    while(True):
        print('1 --> insert')
        print('2 --> search')
        print('3 --> delete')
        print('4 --> prefix search')
        print('5 --> multiple insertion')
        print('0 --> EXIT')

        user = int(input())

        if user==1:
            trie.insert(input('insert --> \t'))
        elif user==2:
            print(trie.search(input('search -->\t')))
        elif user==3:
            trie.delete(trie.root,input('delete -->\t'), 0)
        elif user==4:
            trie.prefix_search(input('prefix -->\t'))
        elif user==5:
            array = [x for x in input('give arrayy of strings-->\n').split()]
            for x in array:
                trie.insert(x)
        elif user==0:
            break
        else:
            pass




