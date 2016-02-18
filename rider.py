"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    def __init__(self, identifier, location, destination, status, patience):

        """
        @type self: Rider
        @type identifier: str
        @type location: Location
        @type destination: Location
        @type status: str
        @type patience: int
        """

        self.identifier = identifier
        self.location = location
        self.destination = destination
        self.status = status
        self.patience = patience







