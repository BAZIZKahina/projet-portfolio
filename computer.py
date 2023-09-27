
class computer:

    # class variable

    def __init__(self, computer_name, internet, keyboard, computer_mouse, screen, program, software, file, antivirus):

        # Attribus d'instance
        self.computer_name = computer_name
        self.internet = internet
        self.keyboard = keyboard
        self.computer_mouse = computer_mouse
        self.screen = screen
        self.program = program
        self.software = software
        self.file = file
        self.antivirus = antivirus

       
        # Méthodes
        def get_computer_name (self):
            return self.computer_name

        def set_computer_name (self, computer_name):
            self.computer_name = computer_name

        def get_internet (self):
            return self.internet

        def set_internet (self, internet):
            self.internet = internet

        def get_keyboard (self):
            return self.keyboard

        def set_keyboard (self, keyboard):
            self.keyboard = keyboard

        def get_computer_mouse (self):
            return self.computer_mouse

        def set_computer_mouse (self, computer_mouse):
            self.computer_mouse = computer_mouse

        def get_screen (self):
            return self.screen

        def set_screen (self, screen):
            self.screen = screen

        def get_program (self):
            return self.program

        def set_programl (self, program):
            self.program = program

        def get_software (self):
            return self.software

        def set_software (self, software):
            self.software = software

        def get_file (self):
            return self.file

        def set_file (self, file):
            self.file = file

        def get_antivirus (self):
            return self.antivirus

        def set_antivirus (self, antivirus):
            self.antivirus = antivirus

        
        # file

        if file >= 1000:
            self.is_file = True
        else:
            self.is_file = False
    

        # software
        if software <= 8:
            self.is_software = True
        else:
            self.is_software = False