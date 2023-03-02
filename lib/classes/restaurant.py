class Restaurant:
    all = []
    
    def __init__(self, name):
        if type(name) == str:
                self._name = name

                Restaurant.all.append(self)
        else:
            raise Exception("Restaurant name must be a string")
        
        self.reviews = []
        self.customers = []

        
    def get_name(self):
        return self._name
    
    name = property(get_name)

    def get_average_rating(self):
        sum = 0
        
        for review in self.reviews:
            sum += review.rating

        average = sum / len(self.reviews)

        return average

            

    @classmethod
    def get_all_restaurants(cls):
        return cls.all
    
