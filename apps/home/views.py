from django.shortcuts import render

# Create your views here.
from django.views.generic import(TamplateView)


class HomeView(TamplateView):
    tamplate_name = "home/home.html"

    def get_context_data(self, **kwargs):

        context = super[HomeView, self.get_context_data(**kwargs)]

        return context