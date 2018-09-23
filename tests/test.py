import unittest
from app import app
import json
from app.views import views

#from app.models import food
from app.models.orders import orders, Orders

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
       orders[:]=[]

    def post_order(self, orderId, location, payment,name, price,quantity, date, status):
            return self.client.post('/api/v1/orders',
            data=json.dumps(dict( 
                orderId=orderId,
                location=location, 
                payment=payment, 
                name=name,
                price=price,
                quantity=quantity,
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

    def edit_order_status(self,orderId, location, payment,name, price,quantity, date, status):
        return self.client.put('api/v1/orders/1',
            data=json.dumps(dict(
                orderId=orderId,
                location=location, 
                payment=payment, 
                name=name,
                price=price,
                quantity=quantity,
                date=date,
                status=status
            )
            ),
            content_type='application/json'
            )

class TestOrdersApi(BaseTestCase):

    def test_can_get_all_orders_list(self):
        with self.client:
            self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
            response=self.get_orders()
            self.assertEqual(response.status_code, 200)

    def test_get_nonexisting_orders_list(self):
        with self.client:
            response=self.get_orders()
            self.assertEqual(response.status_code, 404)

    def test_get_nonexisting_orders_list_message(self):
        with self.client:
            response=self.get_orders()
            data=json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'No orders')

    def test_get_existing_order(self):
        with self.client:
            self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
            response=self.get_an_order()
            self.assertEqual(response.status_code, 200)

    def test_get_non_existing_order(self):
        with self.client:
            response=self.get_an_order()
            self.assertEqual(response.status_code, 404)

    def test_get_non_existing_order_message(self):
        with self.client:
            response=self.get_an_order()
            data=json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'Order not found')
   
    def test_can_add_order(self):
        with self.client:
            response=self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018','Pending')
            self.assertEqual(response.status_code, 201)
        
    def test_add_order_message(self):
        with self.client:
            response=self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
            data=json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "Order sent successfully")

    def test_can_edit_order_status(self):
        with self.client:
            self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
            response=self.edit_order_status(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Completed')
            self.assertEqual(response.status_code, 200)

    def test_can_edit_order_status_message(self):
        with self.client:
            self.post_order(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
            response=self.edit_order_status(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Completed')
            data=json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'Order status updated')

    def test_edit_nonexisting_order_status(self):
        with self.client:
            response=self.edit_order_status(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Completed')
            self.assertEqual(response.status_code, 404)

    def test_edit_nonexisting_order_status_message(self):
        with self.client:
            response=self.edit_order_status(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Completed')
            data=json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'Order does not exist')


    def test_order_class(self):
        order1=Orders(1,'Bunga', 'cash','burger','22000',1, '12/02/2018', 'Pending')
        self.assertTrue(order1)
