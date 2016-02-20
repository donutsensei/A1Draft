class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """

        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @rtype: str
        """
        return "The Location is at row " + str(self.row) + " and column " + str(self.column)


    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        """
        return self == self.other


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    """
    x = origin.row - destination.row
    y = origin.column - destination.column

    return abs(x) + abs(y)



def deserialize_location(location_str): 
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    """
    location = location_str.split(',')

    return Location(int(location[0]),int(location[1]))

