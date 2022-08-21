import json

import unittest
from app import app

CLASSES = ['setosa', 'versicolor', 'virginica']

class TestFlask(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_health(self):
        rv = self.app.get('/health')
        self.assertEqual(rv.status, '200 OK')

    def test_predict(self):
        params = {
            "sepal_length": 6.5,
            "sepal_width": 3.0,
            "petal_length": 4.7,
            "petal_width": 2.5
        }
        rv = self.app.get(
            "/predict",
            data=json.dumps(params),
            content_type="application/json"
        )

        data = json.loads(rv.data)
        self.assertEqual(rv.status, '200')
        self.assertIn(data['class'], CLASSES)

if __name__ == '__main__':
    unittest.main()