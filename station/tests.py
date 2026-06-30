from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from station.models import Station, TrainType, Train


class ModelTests(TestCase):
    def test_station_str(self):
        station = Station.objects.create(
            name="London",
            latitude=51.5074,
            longitude=-0.1278,
        )

        self.assertEqual(str(station), "London")

    def test_train_type_str(self):
        train_type = TrainType.objects.create(
            name="High-speed"
        )

        self.assertEqual(str(train_type), "High-speed")

    def test_train_str(self):
        train_type = TrainType.objects.create(
            name="Regional"
        )

        train = Train.objects.create(
            name="Intercity",
            cargo_num=10,
            places_in_cargo=50,
            train_type=train_type,
        )

        self.assertEqual(str(train), "Intercity")


class PublicApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_auth_required(self):
        response = self.client.get("/api/station/")
        self.assertEqual(response.status_code, 401)


class PrivateApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.client.force_authenticate(self.user)

    def test_orders(self):
        response = self.client.get("/api/station/orders/")
        self.assertEqual(response.status_code, 200)
