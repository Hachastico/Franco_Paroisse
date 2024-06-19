class Rebel:
    def __init__(self, name, fleet, lat, lon):
        self.name = name
        self.fleet = fleet
        self.lat = lat
        self.lon = lon
    
    def get_nombre(self):
        return self.name
    
    def get_fleet(self):
        return self.fleet
    
    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon