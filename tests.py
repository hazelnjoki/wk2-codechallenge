import unittest
from customer import Customer
from Restaurant import Restaurant
from review import Review

class TestRestaurantReviewSystem(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("John", "Doe")
        self.customer2 = Customer("Jane", "Smith")

        self.restaurant1 = Restaurant("Awesome Food Place")
        self.restaurant2 = Restaurant("Fantastic Eatery")

        self.review1 = Review(self.customer1, self.restaurant1, 5)
        self.review2 = Review(self.customer2, self.restaurant1, 4)
        self.review3 = Review(self.customer1, self.restaurant2, 3)
        
def all(cls):
    def test_customer_all(self):
        self.assertEqual(Customer.all(), [self.customer1, self.customer2])

    def test_restaurant_all(self):
        self.assertEqual(Restaurant.all(), [self.restaurant1, self.restaurant2])

    def test_review_all(self):
        self.assertEqual(Review.all(), [self.review1, self.review2, self.review3])

    def test_restaurant_customers(self):
        self.assertEqual(self.restaurant1.customers(), [self.customer1, self.customer2])

    def test_restaurant_average_star_rating(self):
        self.assertEqual(self.restaurant1.average_star_rating(), (5 + 4) / 2)

if __name__ == '__main__':
    unittest.main()
