"""Test functions for APIs and validation"""
import json
import unittest

from app import app
from app.models.orders import Orders, ORDERS
from app.views import views


class BaseTestCase(unittest.TestCase):
    """
    BaseTestCase Class is the base class doing the initial set up for testing requirements.
    It inherits from TestCase from unittest library.
    """
    def setUp(self):
        """Set up of test_client for flask app"""
        self.client = app.test_client(self)

    def tearDown(self):
        """Clears the orders list"""
        ORDERS[:] = []

    def post_order(self, orderId, location, name, price, date, status):
        """Defines from post method in JSON format"""
        return self.client.post('/api/v1/orders',
            data=json.dumps(dict(
                orderId=orderId,
                location=location,
                name=name,
                price=price,
                date=date,
                status=status
            )
        ),
        content_type='application/json')

    def get_orders(self):
        """Return all orders"""
        return self.client.get('api/v1/orders')

    def get_an_order(self):
        """Return one order"""
        return self.client.get('api/v1/orders/1')

    def edit_order_status(self, orderId, location, name, price, date, status):
        """Edit and return data-order"""
        return self.client.put('api/v1/orders/1',
            data=json.dumps(dict(
                orderId=orderId,
                location=location,
                name=name,
                price=price,
                date=date,
                status=status
            )
        ),
        content_type='application/json')

class TestOrdersApi(BaseTestCase):
    """
    TestOrdersApi inherits initial setup from BaseTestCase class.
    It defines methods to test API endpoints.
    """
    def test_can_get_all_orders_list(self):
        """Tests if all orders can be retrieved"""
        self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        response = self.get_orders()
        self.assertEqual(response.status_code, 200)

    def test_get_nonexisting_orders_list(self):
        """Tests status response to retrieving non existing order list"""
        response = self.get_orders()
        self.assertEqual(response.status_code, 404)

    def test_get_nonexisting_orders_list_message(self):
        """Tests message response to retrieving non existing orders"""
        response = self.get_orders()
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'No orders')

    def test_get_existing_order(self):
        """Tests response status to rerieving existing order"""
        self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        response = self.get_an_order()
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_order(self):
        """Tests response status to getting existing order"""
        response = self.get_an_order()
        self.assertEqual(response.status_code, 404)

    def test_get_non_existing_order_message(self):
        """Tests response message to rerieving existing order"""
        response = self.get_an_order()
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order not found')

    def test_can_add_order(self):
        """Tests response status posting a new order"""
        response = self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 201)

    def test_add_order_message(self):
        """Tests response message posting a new order"""
        response = self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), "Order sent successfully")

    def test_can_edit_order_status(self):
        """Tests response status to editing order"""
        self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        response = self.edit_order_status(1, 'Bunga', 'burger', '22000', '12/02/2018', 'Complete')
        self.assertEqual(response.status_code, 201)

    def test_can_edit_order_status_message(self):
        """Tests response message to editing order"""
        self.post_order(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        response = self.edit_order_status(1, 'Bunga', 'burger', '22000', '12/02/2018', 'Complete')
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order status updated')

    def test_edit_nonexisting_order_status(self):
        """Tests response message to editing non-existent order"""
        response = self.edit_order_status(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Complete')
        self.assertEqual(response.status_code, 404)

    def test_edit_nonexisting_order_status_message(self):
        """Tests response status to editing non-existent order"""
        response = self.edit_order_status(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Complete')
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order does not exist')

#Test Order Model Instance
    def test_order_class(self):
        """Test that instance of Order can be created"""
        order1 = Orders(1, 'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertTrue(order1)

class TestValidation(BaseTestCase):
    """
    TestValidation inherits from BaseTestCase.
    It defines methods to test validity of data
    """
    def test_empty_name_string(self):
        """
        Test empty name string in data received in request

        Given all order fields have proper values except name== ''

        Returns 400(bad request)
        """
        response = self.post_order(1, 'Bunga', '', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_invalid_name_string(self):
        """
        Test invalid name string in data received in request

        Given all order fields have proper values, except name=='1234' orname=='@%$^'

        Returns 400(bad request)
        """
        response = self.post_order(1, "Bunga", '78', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_name_not_string(self):
        """
        Test invalid name string in data received in request

        Given all order fields have proper values except name==123

        Returns 400(bad request)
        """
        response = self.post_order(1, "Bunga", 78, 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_empty_price(self):
        """
        Test empty price in data received in request

        Given all order fields have proper values except price = ''

        Returns 400(bad request)
        """
        response = self.post_order(1, 'Bunga', 'burger', '', '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_price_not_integer(self):
        """
        Test empty price in data received in request

        Given all order fields have proper values except price = five

        Returns 400(bad request)
        """
        response = self.post_order(1, "Bunga", 'burger', 'five', '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_empty_location_string(self):
        """
        Test empty location string in data received in request

        Given all order fields have proper values except location== ''

        Returns 400(bad request)
        """
        response = self.post_order(1, '', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_invalid_location_string(self):
        """
        Test empty location string in data received in request

        Given all order fields have proper values except location== '123@'

        Returns 400(bad request)
        """
        response = self.post_order(1, 'n@1ja', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_location_not_string(self):
        """
        Test empty location string in data received in request

        Given all order fields have proper values except location== 123

        Returns 400(bad request)
        """
        response = self.post_order(1, 4567, 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)
