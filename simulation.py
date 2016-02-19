from container import PriorityQueue
from dispatcher import Dispatcher
from event import Event, create_event_list
from monitor import Monitor


class Simulation:
    """A simulation.

    This is the class which is responsible for setting up and running a
    simulation.

    The API is given to you: your main task is to implement the two methods
    according to their docstrings.

    Of course, you may add whatever private attributes and methods you want.
    But because you should not change the interface, you may not add any public
    attributes or methods.

    This is the entry point into your program, and in particular is used for
    auto-testing purposes. This makes it ESSENTIAL that you do not change the
    interface in any way!
    """

    # === Private Attributes ===
    # @type _events: PriorityQueue[Event]
    #     A sequence of events arranged in priority determined by the event
    #     sorting order.
    # @type _dispatcher: Dispatcher
    #     The dispatcher associated with the simulation.

    def __init__(self):
        """Initialize a Simulation.

        @type self: Simulation
        @rtype: None
        """
        self._events = PriorityQueue()
        self._dispatcher = Dispatcher()
        self._monitor = Monitor()

    def run(self, initial_events):
        """Run the simulation on the list of events in <initial_events>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: Simulation
        @type initial_events: list[Event]
            An initial list of events.
        @rtype: dict[str, object]
        """


        while len(initial_events) != 0:



            for event in initial_events:

                parse = str(event).split()



                # "REQUEST A RIDER"
                if parse[-1] == 'rider':

                    if event.driver.destination is None:

                        events = event.do (self._dispatcher, self._monitor)


                        if events != []:

                            for pickup in events:

                                events = pickup.do(self._dispatcher, self._monitor)

                                for dropoff in events:

                                    dropoff.do(self._dispatcher, self._monitor)

                                    initial_events.remove(initial_events[0])




                # "REQUEST A DRIVER"
                if parse[-1] == 'driver':

                    if event.rider.status is None:

                        events = event.do (self._dispatcher, self._monitor)

                        event.rider.status = 'waiting'

                        if len(events) == 2:

                            if events[0].driver.get_travel_time(events[0].rider.destination) <= int(events[0].rider.patience):

                                pickup = events[0].do(self._dispatcher, self._monitor)

                                for dropoff in pickup:

                                    dropoff.do(self._dispatcher, self._monitor)

                            else:
                                events[1].do(self._dispatcher, self._monitor)


                        if len(events) == 1:

                            for event in events:

                                if event.timestamp > event.rider.patience:

                                    event.do(self._dispatcher, self._monitor)





            # Add all initial events to the event queue.

            # Until there are no more events, remove an event
            # from the event queue and do it. Add any returned
            # events to the event queue.


            print(self._monitor._activities['driver'].values())
            print(self._dispatcher.friders)
            print(self._dispatcher.fdrivers)


            return self._monitor.report()


if __name__ == "__main__":
    events = create_event_list("events.txt")
    sim = Simulation()
    final_stats = sim.run(events)
    print(final_stats)
