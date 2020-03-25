import json
from datetime import date
from decimal import Decimal
from typing import Any, Dict

from django.db.models import Max
from django.test import TestCase, Client

from homework.apps import load_db
from homework.models import Cube


def get_greater_date() -> date:
    return Cube.objects.all().aggregate(date=Max('date'))['date'].strftime('%Y-%m-%d')


def get_cube(currency) -> Cube:
    return Cube.find_one_by_date_and_currency(get_greater_date(), currency)


def call_view(amount, src_currency, dest_currency, reference_date) -> Dict[str, Any]:
    client = Client()
    response = client.get(f'/convert?amount={amount}&src_currency={src_currency}&dest_currency={dest_currency}&reference_date={reference_date}')
    return json.loads(response.content)


class CubeModelTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        load_db()

    def test_convert_eur_to_eur(self):
        amount = 13.0
        response = call_view(amount, 'EUR', 'EUR', get_greater_date())
        self.assertEqual(amount, response['amount'])

    def test_convert_zero_to_usd(self):
        response = call_view(0, 'EUR', 'USD', get_greater_date())
        self.assertEqual(0, response['amount'])

    def test_convert_usd_to_jpy(self):
        amount = 7.0
        usd_cube = get_cube('USD')
        jpy_cube = get_cube('JPY')
        response = call_view(amount, 'USD', 'JPY', get_greater_date())
        self.assertEqual(float(Decimal(amount) * usd_cube.rate / jpy_cube.rate), response['amount'])
