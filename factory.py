
class factory:

    # class variable
    def __init__(self, factory_name, palette, workshop, industrial, laboratory, collaborater, machine, raw_material):

        # Attribus d'instance
        self.factory_name = factory_name
        self.palette = palette
        self.workshop = workshop
        self.industrial = industrial
        self.laboratory = laboratory
        self.collaborater = collaborater
        self.machine = machine
        self.raw_material = raw_material
        

       
        # Méthodes
        def get_factory_name (self):
            return self.factory_name

        def set_factory_name (self, factory_name):
            self.factory_name = factory_name

        def get_palette (self):
            return self.palette

        def set_palette (self, palette):
            self.palette = palette

        def get_workshop (self):
            return self.workshop

        def set_workshop (self, workshop):
            self.workshop = workshop

        def get_industrial (self):
            return self.industrial

        def set_industrial (self, industrial):
            self.industrial = industrial

        def get_laboratory (self):
            return self.laboratory

        def set_laboratory (self, laboratory):
            self.laboratory = laboratory

        def get_collaborater (self):
            return self.collaborater

        def set_collaborater (self, collaborater):
            self.collaborater = collaborater

        def get_machine (self):
            return self.machine

        def set_machine (self, machine):
            self.machine = machine

        def get_raw_material (self):
            return self.raw_material

        def set_raw_material (self, raw_material):
            self.raw_material = raw_material

    

        
        # palette

        if palette >= 1500:
            self.is_palette = True
        else:
            self.is_palette = False
    

        # machine
        if machine <= 200:
            self.is_machine = True
        else:
            self.is_machine = False
