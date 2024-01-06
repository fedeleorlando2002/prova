class Vehicle: 
    def _init_(self, name, mileage, capacity): 
        self.name= name
        self.mileage = mileage
        self.capacity = capacity

        def fare(self):
            return self.capacity * 100 
        
        class Bus(Vehicle):
           def _init_(self, name, mileage): 
               return super()._init_( name, mileage)
               self.capacity = 50
           
