import unittest
from app import app
import json
from app.views import views

from app.models import food
from app.models.orders import orders


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def tearDown(self):
        orders[:]=[]

    def post_order(self, location, payment,name, price, date):
            return self.client.post('/api/v1/orders',
            data=json.dumps(dict( 
                location=location, 
                payment=payment, 
                name=name,
                price=price,
                date=date
            )
            ),
            content_type='application/json'
        )

class TestOrdersApi(BaseTestCase):
   

    def test_can_add_order(self):
        with self.client:
            response=self.post_order('Bunga', 'cash','burger','22000', '12/02/2018')
            self.assertEqual(response.status_code, 201)
        
    def test_add_order_message(self):
        with self.client:
            
            response=self.post_order('Bunga', 'cash','burger','22000', '12/02/2018')
            data=json.loads(response.data.decode())
            print(data)
            print(response)
            self.assertEqual(data.get('message'), "Order added successfully")



    
