'''

The Trie method for solving the Autocompletion problem

'''

# Allows us to make objects of the nodes, giving them unique identifiers
class MakeTrieNode():
    def __init__(self):
        # Allows for the creation of nodes off of this node
        self.children = {}

        # Tells when the current node is the last one in the "path" and you have a key
        self.last = False


class FormTrie():
    def __init__(self):

        # Starts the trie by making a root node that will have children come off of it
        self.root = MakeTrieNode()

        # Initiates a variable that allows to create a list of found words later
        self.word_list = []

    # function that takes in the list of words to process into the node
    def formTrie(self, keys):

        for key in keys:
            self.insert(key)

    # Function to be used in the above function to put the keys in the function
    def insert(self, key):

        # Starts the trie as stated above with a root node that will have children come off of it
        node = self.root

        # Actually goes through the list of characters in the key given to it to put in the trie
        for char in list(key.lower()):
            # Search to see if a node already exists as a child of the previous node
            # If not, make a node for it that is a child of the root

            # Makes the node if it doesn't already exist like for starting the first word, and then dog
            # (which has a different beginning letter than the others)
            if not node.children.get(char):
                node.children[char] = MakeTrieNode()

            # Just point the node variable towards the one that already exists
            node = node.children[char]

        # For when you have accounted for all the nodes
        node.last = True

    # This actually finds the autocomplete suggestions
    def suggestionsRec(self, node, word):

        # If it is the last node (thus last character), it is a full word (in the sense of the program) and just append
        # it to the word list
        if node.last:
            self.word_list.append(word)

        # iterates through the dict, with char being through the literal char e.g. "a" and nodeObject being the instance
        # Simply put: char is the key, and nodeObject is the value
        for char, nodeObject in node.children.items():
            self.suggestionsRec(nodeObject, word + char)

    # Interestingly, uses a mini, one-branch Trie to process the searchTerm. This is why it looks similar to insert()
    def getCompletions(self, prefix):

        # sets the node back to the root
        node = self.root

        # boolean just to use later
        not_found = False

        # This is just used to build off of while searchTerm is being processed.
        temp_word = ''

        # This tells when to break off the search when there is no longer a match

        for char in list(prefix.lower()):
            # if node.children.get(char) = None, that is, if that char is not in children of the root
            if not node.children.get(char):
                not_found = True
                break

            temp_word += char
            node = node.children[char]

        # if not_found is true, this line signals to print the message saying so
        if not_found:
            return 0

        # using the
        self.suggestionsRec(node, temp_word)

        for word in self.word_list:
            print(word)
        return 1


keys = ["Aardvark","A", "aarmory", "antler", "zoology", "orca", "orcas"]
prefix = "zz"
status = ["Not found", "Found"]

t = FormTrie()

t.formTrie(keys)

comp = t.getCompletions(prefix)

if comp == 0:
    print("No string found with this prefix\n")
