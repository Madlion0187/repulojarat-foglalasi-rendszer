from Flight import Flight

class DomesticFlight(Flight):
    def __init__(self, flight_number, departure, destination, date, ticket_price):
        super().__init__(flight_number, departure, destination, date, ticket_price)
        self.max_number_of_passangers = 10

    def get_details(self):
        return (f"Járatszám: {self.flight_number}\n----------\nBelföldi járat\nHonnan: {self.departure}\nHova: {self.destination}\nDátum: {self.date}"
                f"\nÁr: {self.ticket_price}Ft\nFoglalások száma/Maximum kapacitás: {len(self.passengers)}/{self.max_number_of_passangers} foglalás\n")
        
    def is_booked_by_passenger(self, passenger_name):
        return (passenger_name in self.passengers)       
        
    def book_flight(self, passenger_name):
        if not len(self.passengers) == self.max_number_of_passangers:
            self.passengers.append(passenger_name)
            print(f"{passenger_name} foglalása teljesítve")
        else:
            print(f"Hiba! A {self.flight_number} járatszámű belföldi járat tele van!")
    
    def cancel_flight(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            print(f"{passenger_name} foglalásának törlése teljesítve")
        else:
            print(f"Hiba! Nem található \"{passenger_name}\" utas az utaslistán!")