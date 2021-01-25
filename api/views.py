from django.http import HttpResponse
from django.views import View
from elasticsearch import Elasticsearch

from .models import Book

import json


class BookView(View):
    @staticmethod
    def get(request):
        return HttpResponse(json.dumps({
            'books': [
                book.serialize() for book in Book.objects.all()
            ]
        }))

    def post(self, request):
        pass


class APIView(View):
    @staticmethod
    def get(request):
        data = {
            'name': request.user.username,
            'skills': ['Python', 'Django'],
        }

        return HttpResponse(json.dumps(data))


def api_view(request):
    # Kibana
    es = Elasticsearch([{
        "host": "localhost",
        "port": 9200,
    }])

    data = {
        'name': request.user.username,
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }

    return HttpResponse(json.dumps(data))

