import requests
import unittest


class TestFastAPIEndpoints(unittest.TestCase):
    BASE_URL = "http://localhost:8000"

    def test_1_create_users(self):
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
                "last_name": "Lopes",
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
            response = requests.post(f"{self.BASE_URL}/users/users/", json=user)
            self.assertEqual(response.status_code, 200)
            self.assertIn(user["login"], response.json()["login"])

    def test_2_create_services(self):
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
            response = requests.post(f"{self.BASE_URL}/services/services/", json=service)
            self.assertEqual(response.status_code, 200)
            self.assertIn(service["name"], response.json()["name"])

    def test_3_create_orders(self):
        order_data = [
            {"user_id": 1, "service_ids": [1], "date_created": "2023-10-10"},
            {"user_id": 2, "service_ids": [2], "date_created": "2023-11-15"},
            {"user_id": 3, "service_ids": [3], "date_created": "2023-09-20"},
        ]

        for order in order_data:
            response = requests.post(f"{self.BASE_URL}/orders/orders/", json=order)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(order["user_id"], response.json()["user_id"])

    def test_4_read_user(self):
        login = "john123"
        url = f"{self.BASE_URL}/users/users/{login}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["login"], login)

    def test_5_search_users(self):
        url = f"{self.BASE_URL}/users/users/search/?first_name=J*&last_name=*o*"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_6_get_services(self):
        url = f"{self.BASE_URL}/services/services/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_7_get_user_orders(self):
        user_id = 1
        url = f"{self.BASE_URL}/orders/orders/{user_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_8_add_service_to_order(self):
        order_id = 1
        url = f"{self.BASE_URL}/orders/orders/{order_id}/add_service"
        service_data = {"service_id": 2}
        response = requests.post(url, json=service_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            service_data["service_id"],
            [service["id"] for service in response.json()["services"]],
        )


if __name__ == "__main__":
    unittest.main()
