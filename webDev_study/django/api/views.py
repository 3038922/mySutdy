from django.http import JsonResponse
from django.views import View


# Create your views here.
class Book(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse('get ok', safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse('post ok', safe=False)