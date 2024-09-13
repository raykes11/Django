from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Mather(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dict"] = {'Title':Title,"Live":Live,"NotLive":NotLive}
        context["other"] = [Title,Live,NotLive]
        return context


class Menu(Mather):
    template_name = 'fourth_task/menu.html'


class Title(Mather):
    template_name = 'fourth_task/title.html'
    extra_context={
        "title": "Игра началась",
        'text' : 'Ахалай махалай',
        'url'  : '/title',
        'name' : 'Главная страница'
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Live(Mather):
    template_name = 'fourth_task/live.html'
    extra_context={
        "title": "Ты выйграл",
        'text' : 'Возьми с полки приражек',
        'url'  : '/title/live',
        'name' : 'Выйграть'
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = ['Черствый','Свежий','Подозрительный']
        return context
class NotLive(Mather):
    template_name = 'fourth_task/not_live.html'
    extra_context={
        "title": "Ты проиграл",
        'text' : 'С тебя  пиражек',
        'url'  : '/title/not_live',
        'name' : 'Проиграть'
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = []
        return context