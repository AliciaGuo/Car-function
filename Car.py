class Car:
    FUEL_TYPES=("Gasoline","Diesel")
    OCTANE_LEVEL=(87,89,91)

    def __init__(self):
        self.color="black"
        self.brand="Ford"
        self.headlights=False
        self.engine=False
        self.license_plate=""

    #getting methods
    def get_color(self):
        return self.color
    def is_headlights(self):
        return self.headlights
    def get_brand(self):
        return self.brand
    def is_engine(self):
        return self.engine
    def get_license_plate(self):
        return self.license_plate

    #setting methods
    def set_color(self,color):
        self.color=color
    def set_headlights(self,headlights):
        self.headlights=headlights
    def set_brand(self,brand):
        self.brand=brand
    def set_engine(self,engine):
        self.engine=engine
    def set_lp(self,lp):
        self.license_plate=lp
    @staticmethod
    def honk(duration):
        for i in range(duration):
            print("Honk!")
