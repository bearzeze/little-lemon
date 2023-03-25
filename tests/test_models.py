from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="Cheesburger", price=5.6, inventory=20)
        print(item)
        
        self.assertEqual(item, "Cheesburger - 5.6 €")
        

class MenuViewTest(TestCase):
    pass