
class phone:

    # class variable
    def __init__(self, phone_name, call, phone_number, answering, charger, application, communication, connection, battery, aerphone):

        # Attribus d'instance
        self.phone_name = phone_name
        self.call = call
        self.phone_number = phone_number
        self.answering = answering
        self.charger = charger
        self.application = application
        self.communication = communication
        self.connection = connection
        self.battery = battery
        self.aerphone = aerphone

       
        # Méthodes
        def get_phone_name (self):
            return self.phone_name

        def set_phone_name (self, phone_name):
            self.phone_name = phone_name

        def get_call (self):
            return self.call

        def set_call (self, call):
            self.call = call

        def get_phone_number (self):
            return self.phone_number

        def set_phone_number (self, phone_number):
            self.phone_number = phone_number

        def get_answering (self):
            return self.answering

        def set_answering (self, answering):
            self.answering = answering

        def get_charger (self):
            return self.charger

        def set_charger (self, charger):
            self.charger = charger

        def get_application (self):
            return self.application

        def set_application (self, application):
            self.application = application

        def get_communication (self):
            return self.communication

        def set_communication (self, communication):
            self.communication = communication

        def get_connection (self):
            return self.connection

        def set_connection (self, connection):
            self.connection = connection

        def get_battery (self):
            return self.battery

        def set_battery (self, battery):
            self.battery = battery

        def get_aerphone (self):
            return self.aerphone

        def set_aerphone (self, aerphone):
            self.aerphone = aerphone

        
        # battery

        if battery >= 5000:
            self.is_battery = True
        else:
            self.is_battery = False
    
