from django.db import models


class Cube(models.Model):
    class Meta:
        unique_together = (
            ('date', 'currency'),
        )

    date = models.DateField()
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=17, decimal_places=7)

    def __str__(self):
        return f'''Cube={{
    id: {self.id},
    date: {self.date},
    currency: {self.currency},
    rate: {self.rate}
}}'''

    @classmethod
    def find_one_by_date_and_currency(cls, date, currency):
        return cls.objects.get(date=date, currency=currency)
