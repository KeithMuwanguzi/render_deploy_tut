from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def testEnd(request):
    data = {
        "status":"success",
        "message": "This is working properly"
    }
    return Response(data)