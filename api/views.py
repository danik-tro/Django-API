from django.http import JsonResponse, HttpResponse
from django.views import View
import json


class APIView(View):
    @staticmethod
    def get(request):
        data = {
            'name': request.user.username,
            'skills': ['Python', 'Django'],
        }

        return HttpResponse(json.dumps(data))


def api_view(request):
    data = {
        'name': request.user.username,
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }

    return HttpResponse(json.dumps(data))

