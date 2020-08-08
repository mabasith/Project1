class Birds:
    def __init__(self):
        self.members = ['Sparrow','Robin', 'Duck']
    def printMembers(self):
        print("Printing member of the Birds class")
        for member in self.members:
            print('%s' %member)