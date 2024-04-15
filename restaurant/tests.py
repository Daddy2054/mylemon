# from django.test import TestCase
# from restaurant.models import Menu

# # Create your tests here.


# class MenuItemTest(TestCase):
#     def setUp(self):
#         Menu.objects.create(title="IceCream", price=80, inventory=100)

#     def test_menu_page_status_code(self):
#         response = self.client.get("/restaurant/menu/")
#         self.assertEqual(response.status_code, 200)

#     def test_get_item(self):
#         item = Menu.objects.get(title="IceCream")
#         print(item)
#         self.assertEqual(item, "IceCream : 80.00")
