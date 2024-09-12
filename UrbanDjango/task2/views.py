from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def strat_page(request):
    return render(request,'second_task/func_template.html')


class Next_page(TemplateView):
    template_name = 'second_task/class_template.html'
