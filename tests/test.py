import json
import unittest

from app import app
from app.models.orders import Orders, orders
from app.views import views


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
       orders[:]=[]

    def post_order(self, orderId, location, name, price, date, status):
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
            content_type='application/json'
        )
    
    def get_orders(self):
        return self.client.get('api/v1/orders')

    def get_an_order(self):
        return self.client.get('api/v1/orders/1')

    def edit_order_status(self,orderId, location,name, price, date, status):
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
            content_type='application/json'
            )
#Test API Endpoints
class TestOrdersApi(BaseTestCase):

    def test_can_get_all_orders_list(self):
        self.post_order(1,'Bunga','burger',22000, '12/02/2018', 'Pending')
        response=self.get_orders()
        self.assertEqual(response.status_code, 200)

    def test_get_nonexisting_orders_list(self):
        response=self.get_orders()
        self.assertEqual(response.status_code, 404)

    def test_get_nonexisting_orders_list_message(self):
        response=self.get_orders()
        data=json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'No orders')#data['message']

    def test_get_existing_order(self):
        self.post_order(1,'Bunga','burger',22000, '12/02/2018', 'Pending')
        response=self.get_an_order()
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_order(self):
        response=self.get_an_order()
        self.assertEqual(response.status_code, 404)

    def test_get_non_existing_order_message(self):
        response=self.get_an_order()
        data=json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order not found')
   
    def test_can_add_order(self):
        response=self.post_order(1,'Bunga','burger',22000, '12/02/2018','Pending')
        self.assertEqual(response.status_code, 201)
        
    def test_add_order_message(self):
        response=self.post_order(1,'Bunga','burger',22000, '12/02/2018', 'Pending')
        data=json.loads(response.data.decode())
        self.assertEqual(data.get('message'), "Order sent successfully")

    def test_can_edit_order_status(self):
        self.post_order(1,'Bunga','burger',22000, '12/02/2018', 'Pending')
        response=self.edit_order_status(1,'Bunga','burger','22000', '12/02/2018', 'Complete')
        self.assertEqual(response.status_code, 200)

    def test_can_edit_order_status_message(self):
        self.post_order(1,'Bunga','burger',22000, '12/02/2018', 'Pending')
        response=self.edit_order_status(1,'Bunga','burger','22000', '12/02/2018', 'Complete')
        data=json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order status updated')

    def test_edit_nonexisting_order_status(self):
        response=self.edit_order_status(1,'Bunga','burger',22000, '12/02/2018', 'Complete')
        self.assertEqual(response.status_code, 404)

    def test_edit_nonexisting_order_status_message(self):
        response=self.edit_order_status(1,'Bunga','burger',22000, '12/02/2018', 'Complete')
        data=json.loads(response.data.decode())
        self.assertEqual(data.get('message'), 'Order does not exist')

#Test Order Model Instance
    def test_order_class(self):
        order1=Orders(1,'Bunga', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertTrue(order1)

#Test Validation of Data

    def test_empty_name_string(self):
        response=self.post_order(1,'Bunga','',22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_name_string(self):
        response=self.post_order(1, "Bunga", '78', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_name_not_string(self):
        response=self.post_order(1, "Bunga", 78, 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_empty_price(self):
        response=self.post_order(1,'Bunga','burger','', '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_price_not_integer(self):
        response=self.post_order(1, "Bunga", 78,'five' , '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_empty_location_string(self):
        response=self.post_order(1,'','burger',22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_location_string(self):
        response=self.post_order(1, 'n@1ja', 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)

    def test_location_not_string(self):
        response=self.post_order(1, 4567, 'burger', 22000, '12/02/2018', 'Pending')
        self.assertEqual(response.status_code, 400)
