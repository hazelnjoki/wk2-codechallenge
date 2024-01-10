class Restaurant:
    restaurants = []



    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)
  
def all(cls):
    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum([review.rating() for review in self.reviews])
        return total_rating / len(self.reviews)