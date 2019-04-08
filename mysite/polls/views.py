from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Question,Choice

def home(requests):
    all_questions = Question.objects.all()
    data = {
        'questions_list' : all_questions
    }
    return render(requests, 'polls/index.html', context=data)

def detail(requests,question_id):

    question = Question.objects.get(pk=question_id)
    data = {
        'question': question
    }
    return render(requests, 'polls/detail.html', context=data)