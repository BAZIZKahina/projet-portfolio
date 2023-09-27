
class fridge:

    # class variable
    def __init__(self, fridge_name, freezer, temperature, cold, cooler, cold_room, engine, fridge_floor, groceries):

        # Attribus d'instance
        self.fridge_name = fridge_name
        self.freezer = freezer
        self.temperature = temperature
        self.cold = cold
        self.cooler = cooler
        self.cold_room = cold_room
        self.engine = engine
        self.fridge_floor = fridge_floor
        self.groceries = groceries

       
        # Méthodes
        def get_fridge_name (self):
            return self.fridge_name

        def set_fridge_name (self, fridge_name):
            self.fridge_name = fridge_name

        def get_freezer (self):
            return self.freezer

        def set_freezer (self, freezer):
            self.freezer = freezer

        def get_temperature (self):
            return self.temperature

        def set_temperature (self, temperature):
            self.temperature = temperature

        def get_cold (self):
            return self.cold

        def set_cold (self, cold):
            self.cold = cold

        def get_cooler (self):
            return self.cooler

        def set_cooler (self, cooler):
            self.cooler = cooler

        def get_cold_room (self):
            return self.cold_room

        def set_cold_room (self, cold_room):
            self.cold_room = cold_room

        def get_engine (self):
            return self.engine

        def set_engine (self, engine):
            self.engine = engine

        def get_fridge_floor (self):
            return self.fridge_floor

        def set_fridge_floor (self, fridge_floor):
            self.fridge_floor = fridge_floor

        def get_groceries (self):
            return self.groceries

        def set_groceries (self, groceries):
            self.groceries = groceries


        
        # temperature

        if temperature >= 8:
            self.is_temperature= True
        else:
            self.is_temperature = False
    

        # groceries
        if groceries <= 6:
            self.is_groceries = True
        else:
            self.is_groceries = False
