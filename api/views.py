from django.http import JsonResponse
from django.views import View


class APIView(View):
    @staticmethod
    def get(request):
        data = {
            'name': request.user.username,
            'skills': ['Python', 'Django'],
        }

        return JsonResponse(data)


def api_view(request):
    data = {
        'name': request.user.username,
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }

    return JsonResponse(data)

