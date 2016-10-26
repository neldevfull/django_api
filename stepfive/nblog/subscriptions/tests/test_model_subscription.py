from django.test import TestCase
from datetime import datetime

from nblog.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.subscription = Subscription(
            name='John Deer',
            cpf='01234567891',
            email='john@example.com',
            phone='12-78745789'
        )

        self.subscription.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscripton must have an auto created at attr."""
        self.assertIsInstance(self.subscription.created_at, datetime)
