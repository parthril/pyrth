class Dragonball:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member Dept
        self.members = ['Goku', 'Vegeta', 'Gohan']
 
 
    def printMembers(self):
        print('Printing members of the Dragonball class')
        for member in self.members:
            print('\t%s ' % member)