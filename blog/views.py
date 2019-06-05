import random

from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.views import View

from blog.models import Fact


class FactView(View):
    template_name = 'blog/fact.html'

    def get(self, request):
        payload = {}
        if request.is_ajax():
            facts = get_list_or_404(Fact)

            rand = random.randint(0, facts.count() - 1)
            payload['fact'] = facts[rand]

        return render(request, self.template_name, payload)
