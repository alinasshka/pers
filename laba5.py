class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):               
        self.amount_of_fuel -= count           
        self.total_weight -= count             
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                      
        return f'Топливо: {self.amount_of_fuel}'
    def get_total_weight(self):                                     
        return f'Масса: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine_status}'

def main():
    Apollon = Rocket(1500, 500, True)
    while Apollon.amount_of_fuel > 0:
        Apollon.spend_fuel(100)
        print(Apollon.get_fuel_level(), end='; ')
        print(Apollon.get_total_weight(), end='; ')
        print(Apollon.get_is_engine_running())
main()
