import unittest
from app.models.orders import Orders


class TestFastFoodFastAPI(unittest.TestCase):
    def setUp(self):
        #self.app = create_app(config_name="testing")
        self.client = self.client
        self.order=Orders()
        self.sample_orders= dict(orderId='A1', 
        fname='veggie burger', 
        fprice='12,000', 
        location='Bunga', 
        payment='card', 
        date='12/04/2018')

    def test_can_fetch_all_orders(self):
        res=self.client().post('/orders', data=self.order)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/orders')
        self.assertEqual(res.status_code, 200)
        self.assertIn('veggie burger', str(res.data))


    