import datetime
from Airline import Airline
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight

class Booking:
    def __init__(self, flight, passenger_name):
        self.flight = flight
        self.passenger_name = passenger_name
        
    def __str__(self):
        return f"Booking for {self.passenger_name} on flight {self.flight.flight_number} on {self.flight.date} from {self.flight.departure} to {self.flight.destination}"

class BookingSystem:
    def __init__(self):
        self._airline = None
        self._bookings = []
        
    def init_data(self):
        self._airline = Airline("Fast Wings")

        self._airline.flights = DomesticFlight("FWD001", "Sármellék", "Debrecen", "2024-12-01", "10000")
        self._airline.flights = InternationalFlight("FWI001", "Budapest", "Berlin", "2024-12-02", "50000")
        self._airline.flights = InternationalFlight("FWI002", "Pozsony", "London", "2024-12-03", "30000")
        
        self._airline.book_by_flight_number("FWD001", "Soros Gyuri")
        self._airline.book_by_flight_number("FWD001", "Orban Viktor")
        
        self._airline.book_by_flight_number("FWI001", "Donald Trump")
        self._airline.book_by_flight_number("FWI001", "Joe Biden")
        
        self._airline.book_by_flight_number("FWI002", "Kim")
        self._airline.book_by_flight_number("FWI002", "Vlad")
        
    def get_bookings(self):
        for booking in self._bookings:
            print(booking)
    
    def user_interact(self):
        while True:
            print("----------------------")
            print("1. Járatok listázása")
            print("2. Foglalásaim listázása")
            print("3. Járat foglalása")
            print("4. Járat lemondása")
            print("5. Kilépés")
            print("----------------------")

            choice = input("Válassz a fenti menüpontok közül: ")

            if choice == "1":
                print()
                self._airline.flights
            elif choice == "2":
                print("")
                name = input("Add meg a nevedet: ")
                passenger_bookings = self._airline.get_all_bookings_for_passenger(name)
                if len(passenger_bookings) > 0:
                    print("Az alábbi foglalások szólnak a nevedre:")
                    for k, v in passenger_bookings.items():
                        print(f"Járatszám: {k}     Repülőjegy ára: {v} Ft")
                else:
                    print("\nNincs jelenleg foglalásod\n")
            elif choice == "3":
                while True:
                    flight_numbers = self._airline.get_flight_numbers()
                    for i, flight_number in enumerate(flight_numbers):
                        print(f"{i + 1}. {flight_number}")
                    
                    flight_number_input = input("Válassz a fenti járatok közül: ")
                    
                    is_flight_number_option_valid = False
                    try:
                        flight_number_index = int(flight_number_input)

                        if flight_number_index - 1 >= 0 and flight_number_index - 1 < len(flight_numbers): 
                            is_flight_number_option_valid = True
                        else:
                            print(f"\nHiba! \"{flight_number_input}\" nem választható\n")
                    except ValueError:
                        print(f"\nHiba! \"{flight_number_input}\" nem választható\n")
                        
                    if not is_flight_number_option_valid:
                        continue
                    
                    flight_number = flight_numbers[flight_number_index - 1]
                    
                    while True:
                        date_input = input("Add meg a dátumot (YYYY-MM-DD): ")
                        try:
                            date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
                            if date_obj.date() < datetime.date.today():
                                print(f"\nHiba! A dátum nem lehet korábbi, mint a mai nap ({datetime.date.today()})\n")
                            else:
                                break
                        except ValueError:
                            print("\nHiba! A dátum formátuma nem megfelelő\n")
                    name = input("Add meg a nevedet: ")
                    self._airline.book_by_flight_number(flight_number, name)
                    break
            elif choice == "4":
                while True:
                    flight_numbers = self._airline.get_flight_numbers()
                    for i, flight_number in enumerate(flight_numbers):
                        print(f"{i + 1}. {flight_number}")
                    
                    flight_number_input = input("Válassz a fenti járatok közül: ")
                    
                    is_flight_number_option_valid = False
                    try:
                        flight_number_index = int(flight_number_input)
                       
                        if flight_number_index - 1 >= 0 and flight_number_index - 1 < len(flight_numbers): 
                            is_flight_number_option_valid = True
                        else:
                            print(f"\nHiba! \"{flight_number_input}\" nem választható\n")
                    except ValueError:
                        print(f"\nHiba! \"{flight_number_input}\" nem választható\n")
                        
                    if not is_flight_number_option_valid:
                        continue
                    
                    flight_number = flight_numbers[flight_number_index - 1]
                    name = input("Add meg a nevedet: ")
                    self._airline.cancel_by_flight_number(flight_number, name)
                    break
            elif choice == "5":
                break
            else:
                print("\nHiba! Ilyen választási lehetőség nincs\n")
        
        
def main():
    booking_system = BookingSystem()
    booking_system.init_data()
    booking_system.user_interact()

if __name__ == "__main__":
    main()
        