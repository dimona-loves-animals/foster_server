from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from foster.serializers import AngelSerializer


@csrf_exempt
def angels_add(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AngelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
