from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(requests):
    transaction = {'id': 'MPQ2345', 'category': 'Savings', 'amount': 2500}
    return Response(transaction)
