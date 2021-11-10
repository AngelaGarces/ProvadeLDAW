from django import urls
from django.urls import path
from .views import HomeView, SobreView, MilitarView, CivilView, PenalView, BombeirosView, GuardaView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('sobre/', SobreView.as_view(), name='Sobre'),
    path('bombeiros/', BombeirosView.as_view(), name='Bombeiros'),
    path('militar/', MilitarView.as_view(), name='Militar'),
    path('civil/', CivilView.as_view(), name='Civil'),
    path('guarda/', GuardaView.as_view(), name='Guarda'),
    path('penal/', PenalView.as_view(), name='Penal'),
]