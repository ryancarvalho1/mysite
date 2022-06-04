from multiprocessing import context
from re import template
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

    # Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pud_date')[:1]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))