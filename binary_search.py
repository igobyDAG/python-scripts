class BinarySearch:

    def search(self, item, start=0, end=100):
        # I want this to be a method that can be used on an iterable.
        # pseudocode:
        # a = ['a', 'b', 'c', 'y', 'z']
        # a.search('b')
        # Lets test this out first on a list.
        # Then lets see if it works as well for a tuple.
        pass


if __name__ == '__main__':
    binary_search = BinarySearch()
    a = ['a', 'b', 'c', 'x', 'y', 'z']
    a.index()
