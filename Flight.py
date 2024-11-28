from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, departure, destination, date, ticket_price):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.date = date
        self.ticket_price = ticket_price
        self.passengers = []
    
    @abstractmethod
    def is_booked_by_passenger(self, passenger_name):
        pass
    
    @abstractmethod
    def book_flight(self, passenger_name):
        pass
    
    @abstractmethod
    def cancel_flight(self, passenger_name):
        pass
    
    @abstractmethod
    def get_details(self):
        pass