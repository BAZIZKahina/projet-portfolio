
class vehicule:

    # class variable
    university_name = "Golde"

    def __init__(self, vehicule_name, price, speed, flying, engine, traffic, tires, brake, radar, breakdown):

         # Attribus d'instance
        self.vehicule_name = vehicule_name
        self.price = price
        self.speed = speed
        self.flying = flying
        self.engine= engine
        self.traffic = traffic
        self.tires = tires
        self.brake = brake
        self.radar = radar
        self.breakdwon= breakdown


        # méthodes
        def get_vehicule_name  (self):
            return self.vehicule_name 
        
        def set_vehicule_name  (self,vehicule_name ):
            self.vehicule_name  = vehicule_name 

        def get_price (self):
            return self.price

        def set_price (self, price):
            self.price = price

        def get_speed (self):
            return self.speed

        def set_speed (self, speed):
            self.speed = speed

        def get_flying(self):
            return self.flying

        def set_flying (self, flying):
            self.flying = flying

        def get_engine (self):
            return self.engine

        def set_engine (self, engine):
            self.engine = engine

        def get_traffic (self):
            return self.traffic

        def set_traffic (self, traffic):
            self.traffic = traffic

        def get_tires (self):
            return self.tires
            
        def set_tires (self, tires):
            self.tires = tires

        def get_brake (self):
            return self.brake

        def set_brake (self, brake):
            self.brake = brake

        def get_radar (self):
            return self.radar

        def set_radar (self, radar):
            self.radar = radar

        def get_breakdwon (self):
            return self.breakdwon

        def set_breakdwon (self, breakdwon):
            self.breakdwon = breakdwon

        # speed
    
        if speed <= 120:
            speed = True
        else:
            speed = False

        for speed in self.speed:
            return self.speed

        i = 90
        while i < len(self.speed):
            i = 90
            return self.speed

        # engine
        if engine > 20:
            self.engine = True
        else:
            self.engine = False

        for engine in self.engine:
            return self.engine


        i = 25
        while i > len(self.engine):
            i = 25
            return self.engine