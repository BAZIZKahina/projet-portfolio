class television:

    # class variable
    def __init__(self, television_name, tv_channel, animator, emission, remote, reporting, viewer, antenna, satellite, media):

        # Attribus d'instance
        self.television_name = television_name
        self.tv_channel = tv_channel
        self.animator = animator
        self.emission = emission
        self.remote = remote
        self.reporting = reporting
        self.viewer = viewer
        self.antenna = antenna
        self.satellite = satellite
        self.media = media

       
        # Méthodes
        def get_television_name (self):
            return self.television_name

        def set_television_name (self, television_name):
            self.television_name = television_name

        def get_tv_channel (self):
            return self.tv_channel

        def set_tv_channel (self, tv_channel):
            self.tv_channel = tv_channel

        def get_animator (self):
            return self.animator

        def set_animator (self, animator):
            self.animator = animator

        def get_emission (self):
            return self.emission

        def set_emission (self, emission):
            self.emission = emission

        def get_remote (self):
            return self.remote

        def set_remote (self, remote):
            self.remote = remote

        def get_preporting (self):
            return self.reporting

        def set_reporting (self, reporting):
            self.reporting = reporting

        def get_viewer (self):
            return self.viewer

        def set_viewer (self, viewer):
            self.viewer = viewer

        def get_antenna (self):
            return self.antenna

        def set_antenna (self, antenna):
            self.antenna = antenna

        def get_satellite (self):
            return self.satellite

        def set_satellite (self, satellite):
            self.satellite = satellite
        
        def get_media (self):
            return self.media

        def set_media (self, media):
            self.media = media

        
        # tv_channel

        if tv_channel >= 1000:
            self.is_tv_channel = True
        else:
            self.is_tv_channel = False
    

        # semission
        if emission <= 100:
            self.is_emission= True
        else:
            self.is_emission = False
