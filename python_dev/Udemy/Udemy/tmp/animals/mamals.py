#class that we will create
class mamals:
    def __init__(self):
        self.memers = ['tiger','elephant','wild cat']
    def printMembers(self):
        print("Printing members of the Mamels class")
        for member in self.memers:
            print('%s' %member)