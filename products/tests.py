from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    """
    Tests will be defined here to run against the Product models 
    """
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')