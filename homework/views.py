import json
from decimal import Decimal

from django.http import Http404, HttpResponse

from homework.models import Cube


def convert(request):
    if request.method != 'GET':
        raise Http404('Not found')
    amount = request.GET['amount']
    src_currency = request.GET['src_currency']
    dest_currency = request.GET['dest_currency']
    reference_date = request.GET['reference_date']
    src_cube = Cube.find_one_by_date_and_currency(reference_date, src_currency)
    dest_cube = Cube.find_one_by_date_and_currency(reference_date, dest_currency)
    return HttpResponse(json.dumps({
        'amount': float(Decimal(amount) * src_cube.rate / dest_cube.rate),
        'currency': dest_currency,
    }), content_type='application/json')
