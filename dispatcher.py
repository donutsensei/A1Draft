from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self.fdrivers = []
        self.friders = []
        self.dic = {}


    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        return str(len(self.fdrivers)) + " drivers are available and " + str(len(self.friders)) + " riders are available."



    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """

        if rider not in self.friders:
            self.friders.append(rider)

        if self.fdrivers != []:

           # self.dic[self.fdrivers[0]] = rider

            return self.fdrivers.pop(0)


        return None



    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """


        if (driver not in self.fdrivers) and (driver.destination is None):

            self.fdrivers.append(driver)

        if self.friders != []:

            #self.dic[driver] = self.friders[0]

            return self.friders.pop(0)

        return None




    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        for key in self.dic:

            if self.dic[key] == rider:

                self.friders.append(rider)

                self.fdrivers.append(key)

                self.dic.pop(key)




