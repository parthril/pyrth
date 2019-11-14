class Naruto:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member Dept
        self.members = ['Naruto', 'Sasuke', 'Kakashi']
 
 
    def printMembers(self):
        print('Printing members of the Naruto class')
        for member in self.members:
            print('\t%s ' % member)