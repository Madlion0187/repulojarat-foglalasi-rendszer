class Airline:
    def __init__(self, name):
        self._name = name
        self._flights = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def flights(self):
        for flight in self._flights:
            print(flight.get_details())

    @flights.setter
    def flights(self, flight):
        self._flights.append(flight)
    
    def get_flight_by_flight_number(self, flight_number):
        flight = None
        for flight in self._flights:
            if flight.flight_number == flight_number:
                flight = flight
                break
        return flight
    
    def get_flight_numbers(self):
        flight_numbers = []
        for flight in self._flights:
            flight_numbers.append(flight.flight_number)
        return flight_numbers
    
    def book_by_flight_number(self, flight_number, passenger_name):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                flight.book_flight(passenger_name)
            
    def cancel_by_flight_number(self, flight_number, passenger_name):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                flight.cancel_flight(passenger_name)
                
    def get_all_bookings_for_passenger(self, passenger_name):
        ret = {}
        for flight in self._flights:
            if flight.is_booked_by_passenger(passenger_name):
                ret[flight.flight_number] = flight.ticket_price
        return ret
    