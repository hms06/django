from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):

    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)
    return HttpResponse("안녕하세요")

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)