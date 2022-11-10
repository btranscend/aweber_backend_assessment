import json
import unittest
from urllib import request

from crud_rest_api.models import Widgets
from rest_framework.test import APITestCase

# Create your tests here.


class WidgetTestCase(APITestCase):
    def test_get_widgets(self):
        """
        Tests the get_widgets function.
        """
        response = self.client.get('/widget/')

        # Checking the count
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Widgets.objects.count(), 0)

        # Creating mock entities
        Widgets.objects.create(name='widget1', number_of_parts=1)
        Widgets.objects.create(name='widget2', number_of_parts=2)
        Widgets.objects.create(name='widget3', number_of_parts=3)

        # Testing the count
        self.assertEqual(Widgets.objects.count(), 3)
        response =  self.client.get('/widget/')

        # Checking status OK 200
        self.assertEqual(response.status_code, 200)


    def test_add_widget(self):
        """
        Tests the add_widget function.
        """

        # Making mock POST request
        data = {'name': 'test_widget', 'number_of_parts': 1}
        response = self.client.post('/widget/add', data=data, format='json')

        # Checking status CREATED 201
        self.assertEqual(response.status_code, 201)

        # Checking it the presence of the entity
        widget = Widgets.objects.get(name='test_widget')
        self.assertEqual(widget.name, 'test_widget')
        self.assertEqual(widget.number_of_parts, 1)

        widget.delete()


    def test_get_widget(self):
        """
        Tests the get_widget function.
        """
        widget = Widgets.objects.create(name='superFancyName', number_of_parts=1)

        response = self.client.get(f'/widget/{widget.pk}')
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['name'], 'superFancyName')
        self.assertEqual(data['number_of_parts'], 1)

        widget.delete()


    def test_delete_widget(self):
        """
        Tests the delete_widget function.
        """
        widget = Widgets(name='test_widget', number_of_parts=1)
        widget.save()
        prevCount = widgets = Widgets.objects.count()

        widget = Widgets.objects.get(name='test_widget')
        response = self.client.delete(f'/widget/{widget.pk}/delete')

        self.assertEqual(response.status_code, 204)
        newCount = widgets = Widgets.objects.count()

        self.assertEqual(newCount, prevCount - 1)



    def test_update_widget(self):
        """
        Tests the update_widget function.
        """
        widget = Widgets(name='test_widget', number_of_parts=1)
        widget.save()

        data = {'name': 'modified_name', 'number_of_parts': 2}
        self.client.put(f'/widget/{widget.pk}/update', data=data, format='json')

        widget = Widgets.objects.get(pk=widget.pk)

        self.assertEqual(widget.name, 'modified_name')
        self.assertEqual(widget.number_of_parts, 2)

        widget.delete()
