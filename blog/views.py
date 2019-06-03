import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from blog.models import Fact


class FactView(View):
    template_name = 'blog/fact.html'

    def get(self, request):
        payload = {}
        if request.is_ajax():
            facts = Fact.objects.all()

            if not facts.exists():
                return HttpResponseNotFound()

            rand = random.randint(0, facts.count()-1)
            payload['fact'] = facts[rand]

        return render(request, self.template_name, payload)
