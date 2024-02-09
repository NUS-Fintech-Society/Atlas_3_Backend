from django.test import TestCase, Client


class DemoTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_can_get_resource(self):
        response = self.client.get("/resource")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"result": "Hello Django!"})
