
class plane:

    # class variable
    def __init__(self, plane_name, pilot, flight_attendant, travelers, engine, luggage, plane_seat, plane_ticket, flight):

        # Attribus d'instance
        self.plane_name = plane_name
        self.pilot = pilot
        self.flight_attendant = flight_attendant
        self.travelers = travelers
        self.engine = engine
        self.luggage = luggage
        self.plane_seat = plane_seat
        self.plane_ticket = plane_ticket
        self.flight = flight

       
        # Méthodes
        def get_plane_name (self):
            return self.plane_name

        def set_plane_name (self, plane_name):
            self.plane_name = plane_name

        def get_pilot (self):
            return self.pilot

        def set_pilot (self, pilot):
            self.pilot = pilot

        def get_flight_attendant (self):
            return self.flight_attendant

        def set_flight_attendant (self, flight_attendant):
            self.flight_attendant = flight_attendant

        def get_travelers (self):
            return self.travelers

        def set_travelers (self, travelers):
            self.travelers = travelers

        def get_engine (self):
            return self.engine

        def set_engine (self, engine):
            self.engine = engine

        def get_luggage (self):
            return self.luggage

        def set_luggage (self, luggage):
            self.luggage = luggage

        def get_plane_seat (self):
            return self.plane_seat

        def set_plane_seat (self, plane_seat):
            self.plane_seat = plane_seat

        def get_plane_ticket (self):
            return self.plane_ticket

        def set_plane_ticket (self, plane_ticket):
            self.plane_ticket = plane_ticket

        def get_flight (self):
            return self.flight

        def set_flight (self, flight):
            self.flight = flight

        
        # travelers

        if travelers >= 250:
            self.is_travelers = True
        else:
            self.is_travelers = False
    

        # pilot
        if pilot <= 3:
            self.is_pilot = True
        else:
            self.is_pilot = False
