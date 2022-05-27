from django.test import TestCase
from .models import Item

class TestDjango(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_tasks.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    # After running coverage package to fix coverage issues
    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')

    # Step 1 in Hello Django test: fails
    # def test_this_thing_works(self):
    #     self.assertEqual(1, 0)

    # Step 2 in Hello Django test: pass (.), fail (F), error (E), fail (F)
    # def test_this_thing_works(self):
    #     self.assertEqual(1, 1)

    # def test_this_thing_works2(self):
    #     self.assertEqual(1, 3)

    # def test_this_thing_works3(self):
    #     self.assertEqual(1, )

    # def test_this_thing_works4(self):
    #     self.assertEqual(1, 4)

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

