from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """

        self.identifier = identifier
        self.location = location
        self.speed = speed


    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str
        """

        return "The driver ID is" + Driver.identifier + ", with location" + Driver.location

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool
        """

        if self == other:
            return True

        return False


    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int
        """

        self.x = self.location.row - Driver.destination.row
        self.y = self.location.column - Driver.destination.column

        self.distance = abs(self.x) + abs(self.y)

        return self.distance//Driver.speed


    def start_drive(self, location):

        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int
        """

        return (abs(self.location.row - Driver.location.row) + abs(self.location.column - Driver.location.column))//Driver.speed



    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        if self.destination:

            Driver.location = self.destination


    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int
        """
        row = Driver.location.row - Rider.location.row
        column = Driver.location.column - Rider.location.column

        return (abs(Driver.location.row - rider.location.row) + abs(Driver.location.column - rider.location.column))//Driver.speed


    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        if self.destination:

            Driver.location = self.destination