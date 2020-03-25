from datetime import datetime
from decimal import Decimal

import requests
import xmltodict
from django.apps import AppConfig
from django.db import IntegrityError


def load_db():
    from homework.models import Cube
    http_response = requests.get(
        'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml')
    if 200 <= http_response.status_code < 300:
        body = http_response.text
        doc = xmltodict.parse(body)
        for data in doc['gesmes:Envelope']['Cube']['Cube']:
            date = datetime.strptime(data['@time'], '%Y-%m-%d').date()
            try:
                Cube(date=date, currency='EUR', rate=Decimal('1')).save()
            except IntegrityError as err:
                pass
            for row in data['Cube']:
                rate = Decimal(row['@rate'])
                try:
                    Cube(date=date, currency=row['@currency'],
                         rate=rate).save()
                except IntegrityError as err:
                    pass


class HomeworkConfig(AppConfig):
    name = 'homework'

    def ready(self):
        load_db()
