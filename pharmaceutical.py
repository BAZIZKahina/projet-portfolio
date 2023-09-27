
class pharmaceutical:

    # class variable
    

    def __init__(self, pharmaceutical_name, agri_food, pharmacy, medication, cosmetic, prescription, orthopedic, pharmacy_cash_register, pharmacist):

       
       
        # Attribus d'instance
        self.pharmaceutical_name = pharmaceutical_name
        self.agri_food = agri_food
        self.pharmacy = pharmacy
        self.medication = medication
        self.cosmetic = cosmetic
        self.prescription = prescription
        self.orthopedic = orthopedic
        self.pharmacy_cash_register = pharmacy_cash_register
        self.pharmacist = pharmacist

       
        # Méthodes
        def get_pharmaceutical_name (self):
            return self.phamaceutical_name

        def set_pharmaceutical_name (self, pharmaceutical_name):
            self.pharmaceutical_name = pharmaceutical_name

        def get_agri_food (self):
            return self.agri_food

        def set_agri_food (self, agri_food):
            self.agri_food = agri_food

        def get_pharmacy (self):
            return self.pharmacy

        def set_pharmacy (self, pharmacy):
            self.pharmacy = pharmacy

        def get_medication (self):
            return self.medication

        def set_medication (self, medication):
            self.medication = medication

        def get_cosmetic (self):
            return self.cosmetic

        def set_cosmetic (self, cosmetic):
            self.cosmetic = cosmetic

        def get_prescription (self):
            return self.prescription

        def set_prescription (self, prescription):
            self.prescription = prescription

        def get_orthopedic (self):
            return self.orthopedic

        def set_orthopedic (self, orthopedic):
            self.orthopedic = orthopedic

        def get_pharmacy_cash_register (self):
            return self.pharmacy_cash_register

        def set_pharmacy_cash_register (self, pharmacy_cash_register):
            self.pharmacy_cash_register = pharmacy_cash_register

        def get_pharmacist (self):
            return self.pharmacist

        def set_pharmacist (self, pharmacist):
            self.pharmacist = pharmacist

        
        # pharmacy_cash_register

        if pharmacy_cash_register >= 1000:
            self.is_pharmacy_cash_register= True
        else:
            self.is_pharmacy_cash_register = False
    

        # prescription
        if prescription <= 10:
            self.is_prescription = True
        else:
            self.is_prescription = False

        
        
    