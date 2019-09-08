import random

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.views import View

from blog.models import Fact


class FactView(View):

    def get(self, request):
        payload = {}

        if request.is_ajax():
            facts = get_list_or_404(Fact)

            rand = random.randint(0, len(facts) - 1)
            fact = facts[rand]
            payload['body'] = fact.body
            payload['image'] = fact.image.url

        return JsonResponse(payload)
