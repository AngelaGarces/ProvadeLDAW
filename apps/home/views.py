from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)

        return context


class SobreView(TemplateView):
    template_name = "home/sobre.html"

    def get_context_data(self, **kwargs):

        context = super(SobreView, self).get_context_data(**kwargs)

        return context


class CivilView(TemplateView):
    template_name = "home/civil.html"

    def get_context_data(self, **kwargs):

        context = super(CivilView, self).get_context_data(**kwargs)

        return context


class BombeirosView(TemplateView):
    template_name = "home/bombeiros.html"

    def get_context_data(self, **kwargs):

        context = super(BombeirosView, self).get_context_data(**kwargs)

        return context


class GuardaView(TemplateView):
    template_name = "home/guarda.html"

    def get_context_data(self, **kwargs):

        context = super(GuardaView, self).get_context_data(**kwargs)

        return context


class MilitarView(TemplateView):
    template_name = "home/militar.html"

    def get_context_data(self, **kwargs):

        context = super(MilitarView, self).get_context_data(**kwargs)

        return context


class PenalView(TemplateView):
    template_name = "home/penal.html"

    def get_context_data(self, **kwargs):

        context = super(PenalView, self).get_context_data(**kwargs)

        return context

