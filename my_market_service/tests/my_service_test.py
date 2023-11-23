import requests
import unittest


class TestFastAPIEndpoints(unittest.TestCase):
    BASE_URL = "http://localhost:8000"

    def test_create_user(self):
        url = f"{self.BASE_URL}/users/"
        data = {
            "login": "john123",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("john123", response.json()["login"])

    def test_create_users(self):
        user_data = [
            {
                "login": "john123",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
            },
            {
                "login": "jane567",
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane@example.com",
            },
            {
                "login": "mike789",
                "first_name": "Mike",
                "last_name": "Johnson",
                "email": "mike@example.com",
            },
        ]

        for user in user_data:
            response = requests.post(f"{self.BASE_URL}/users/", json=user)
            self.assertEqual(response.status_code, 200)
            self.assertIn(user["login"], response.json()["login"])

    def test_create_services(self):
        service_data = [
            {
                "name": "Web Development",
                "description": "Professional website development services",
                "cost": 250.00,
            },
            {
                "name": "Graphic Design",
                "description": "Creative graphic design services",
                "cost": 150.00,
            },
            {
                "name": "Digital Marketing",
                "description": "Effective online marketing strategies",
                "cost": 300.00,
            },
        ]

        for service in service_data:
            response = requests.post(f"{self.BASE_URL}/services/", json=service)
            self.assertEqual(response.status_code, 200)
            self.assertIn(service["name"], response.json()["name"])

    def test_create_orders(self):
        order_data = [
            {"user_id": 1, "service_ids": [1], "date_created": "2023-10-10"},
            {"user_id": 2, "service_ids": [2], "date_created": "2023-11-15"},
            {"user_id": 3, "service_ids": [3], "date_created": "2023-09-20"},
        ]

        for order in order_data:
            response = requests.post(f"{self.BASE_URL}/orders/", json=order)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(order["user_id"], response.json()["user_id"])


if __name__ == "__main__":
    unittest.main()
