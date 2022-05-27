from django.test import TestCase
from .models import Item

class TestDjango(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    # After running coverage package to fix coverage issues
    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
