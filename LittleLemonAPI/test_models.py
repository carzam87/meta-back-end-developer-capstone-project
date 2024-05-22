from django.test import TestCase
from LittleLemonAPI.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Ice Cream", price=80, inventory=100
        )
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Ice Cream : 80")