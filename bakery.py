
class bakery:

    # class variable
    def __init__(self, bakery_name, bread, flour, oven, cooking, pastries, seller, baking_powder, kneading):

        # Attribus d'instance
        self.bakery_name = bakery_name
        self.bread = bread
        self.flour = flour
        self.oven = oven
        self.cooking = cooking
        self.pastries = pastries
        self.seller = seller
        self.baking_powder = baking_powder
        self.kneading = kneading

       
        # Méthodes
        def get_bakery_name (self):
            return self.bakery_name

        def set_bakery_name (self, bakery_name):
            self.bakery_name = bakery_name

        def get_bread (self):
            return self.bread

        def set_bread (self, bread):
            self.bread = bread

        def get_flour (self):
            return self.flour

        def set_flour (self, flour):
            self.flour = flour

        def get_oven (self):
            return self.oven

        def set_oven (self, oven):
            self.oven = oven

        def get_cooking (self):
            return self.cooking

        def set_cooking (self, cooking):
            self.cooking = cooking

        def get_pastries (self):
            return self.pastries

        def set_pastries (self, pastries):
            self.pastries = pastries

        def get_seller (self):
            return self.seller

        def set_seller (self, seller):
            self.seller = seller

        def get_baking_powder (self):
            return self.baking_powder

        def set_baking_powder (self, baking_powder):
            self.baking_powder = baking_powder

        def get_kneading (self):
            return self.kneading

        def set_kneading (self, kneading):
            self.kneading = kneading

        
        # bread

        if bread >= 1000:
            self.is_bread = True
        else:
            self.is_bread = False
    

        # seller
        if seller <= 5:
            self.is_seller = True
        else:
            self.is_seller = False
