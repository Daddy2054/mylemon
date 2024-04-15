from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse

# Create your tests here.


# class MenuTest(TestCase):
#     def setUp(self):
#         Menu.objects.create(title="IceCream", price=80, inventory=100)

#     def test_menu_page_status_code(self):
#         response = self.client.get("/restaurant/menu/")
#         self.assertEqual(response.status_code, 200)

#     def test_get_item(self):
#         item = Menu.objects.get(title="IceCream")
#         print(item)
#         self.assertEqual(item, "IceCream : 80.00")


class MenuEndpointTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_menu_page_status_code(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)

    # def test_menu_page_uses_correct_template(self):
    #     response = self.client.get(reverse("menu"))
    #     self.assertTemplateUsed(response, "restaurant/menu.html")

    def test_menu_page_contains_correct_context(self):
        response = self.client.get(reverse("menu"))
        self.assertContains(response, "IceCream")
        self.assertContains(response, "80.00")
        self.assertContains(response, "100")

class MenuModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title='Pizza', price=10.99, inventory=10)

    def test_title_label(self):
        menu = Menu.objects.get(title="Pizza")
        # menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_price_label(self):
        menu = Menu.objects.get(title="Pizza")

        field_label = menu._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_inventory_label(self):
        menu = Menu.objects.get(title="Pizza")

        field_label = menu._meta.get_field('inventory').verbose_name
        self.assertEquals(field_label, 'inventory')

    def test_title_max_length(self):
        menu = Menu.objects.get(title="Pizza")
        max_length = menu._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_price_max_digits(self):
        menu = Menu.objects.get(title="Pizza")
        max_digits = menu._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_price_decimal_places(self):
        menu = Menu.objects.get(title="Pizza")
        decimal_places = menu._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)

    # def test_inventory_default(self):
    #     menu = Menu.objects.get(title="Pizza")
    #     default_value = menu._meta.get_field('inventory').default
    #     self.assertEquals(default_value, 0)

    def test_object_name_is_title(self):
        menu = Menu.objects.get(title="Pizza")
        expected_object_name = f'{menu.title} : {str(menu.price)}'
        self.assertEquals(expected_object_name, str(menu))
