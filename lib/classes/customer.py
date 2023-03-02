class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = [] 

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
    
    def set_first_name(self, first_name):
        if type(first_name) == str and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else: 
            raise Exception("First name must be between 1 and 25 characters long")
    
    def set_last_name(self, last_name):
        if type(last_name) == str and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            raise Exception("Last name must be between 1 and 25 characters long")

    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    

    def get_num_reviews(self):
        return len(self.reviews)

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)




        