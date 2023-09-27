
class hospital:

    # class variable

    def __init__(self, hospital_name, doctor, nurse, surgery, hospitalized, medical_material, reception, medical_visit, radiology):

        # Attribus d'instance
        self.hospital_name = hospital_name
        self.doctor = doctor
        self.nurse = nurse
        self.surgery = surgery
        self.hospitalized = hospitalized
        self.medical_material = medical_material
        self.reception = reception
        self.medical_visit = medical_visit
        self.radiology = radiology

       
        # Méthodes
        def get_hospital_name (self):
            return self.hospital_name

        def set_hospital_name (self, hospital_name):
            self.hospital_name = hospital_name

        def get_doctor (self):
            return self.doctor

        def set_doctor (self, doctor):
            self.doctor = doctor

        def get_nurse (self):
            return self.nurse

        def set_nurse (self, nurse):
            self.nurse = nurse

        def get_surgery (self):
            return self.surgery

        def set_surgery (self, surgery):
            self.surgery = surgery

        def get_hospitalized (self):
            return self.hospitalized

        def set_hospitalized (self, hospitalized):
            self.hospitalized = hospitalized

        def get_medical_material (self):
            return self.medical_material

        def set_medical_material (self, medical_material):
            self.medical_material = medical_material

        def get_reception (self):
            return self.reception

        def set_reception (self, reception):
            self.reception = reception

        def get_medical_visit (self):
            return self.medical_visit

        def set_medical_visit (self, medical_visit):
            self.medical_visit = medical_visit

        def get_radiology (self):
            return self.radiology

        def set_radiology (self, radiology):
            self.sradiology = radiology

        
        # hospitalized

        if hospitalized >= 1000:
            self.is_hospitalized = True
        else:
            self.is_hospitalized = False
    

        # medical_visit
        if medical_visit <= 2000:
            self.is_medical_visit = True
        else:
            self.is_medical_visit = False

        # doctor
        if doctor <= 150:
            self.is_doctor = True
        elif doctor < 200 and doctor > 150:
            print ("succeed")
        
    