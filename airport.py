
class airport:

    # class variable
    def __init__(self, airport_name, planes, travelers, terminal, registration, luggage, shop, crew, airport_police_control, display_bord):

        # Attribus d'instance
        self.airport_name = airport_name
        self.planes = planes
        self.travelers = travelers
        self.terminal = terminal
        self.registration = registration
        self.luggage = luggage
        self.shop = shop
        self.crew = crew
        self.airport_police_control = airport_police_control
        self.display_bord = display_bord

       
        # Méthodes
        def get_airport_name (self):
            return self.airport_name

        def set_airport_name (self, airport_name):
            self.airport_name = airport_name

        def get_planes (self):
            return self.planes

        def set_planes (self, planes):
            self.planes = planes

        def get_travelers (self):
            return self.travelers

        def set_travelers (self, travelers):
            self.ftravelers = travelers

        def get_terminal (self):
            return self.terminal

        def set_terminal (self, terminal):
            self.terminal = terminal

        def get_registration (self):
            return self.registration

        def set_registration (self, registration):
            self.registration = registration

        def get_luggage (self):
            return self.luggage

        def set_luggage (self, luggage):
            self.luggage = luggage

        def get_shop (self):
            return self.shop

        def set_shop (self, shop):
            self.shop = shop

        def get_crew (self):
            return self.crew

        def set_crew (self, crew):
            self.crew = crew

        def get_airport_police_control (self):
            return self.airport_police_control

        def set_airport_police_control (self, airport_police_control):
            self.airport_police_control = airport_police_control

        def get_display_bord (self):
            return self.display_bord

        def set_display_bord (self, display_bord):
            self.display_bord = display_bord

        
        # planes

        if planes >= 500:
            self.is_planes = True
        else:
            self.is_planes = False
    

        # terminal
        if terminal <= 8:
            self.is_terminal = True
        else:
            self.is_terminal = False
