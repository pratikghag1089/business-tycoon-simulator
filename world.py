from config import TOWNS

class Town:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.market_conditions = 1.0  # Base multiplier for demand
    
    def __str__(self):
        return f"{self.name} (Pop: {self.population})"

class World:
    def __init__(self):
        self.towns = []
        self._initialize_towns()
        self.game_time = 0.0  # in days
    
    def _initialize_towns(self):
        """Create town objects from configuration"""
        for town_data in TOWNS:
            town = Town(town_data["name"], town_data["population"])
            self.towns.append(town)
    
    def update(self, delta_time):
        """Update world state"""
        # For now, just advance internal time
        # Future: update market conditions, process events, etc.
        pass
    
    def get_towns(self):
        """Return list of all towns"""
        return self.towns
    
    def get_town_by_name(self, name):
        """Find a town by name"""
        for town in self.towns:
            if town.name == name:
                return town
        return None