from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(req):
    d = { "name": "yael", "age": 36}
    return Response(d)