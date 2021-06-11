from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer, Comment
from django.http import HttpResponse
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  
    page_obj = paginator.get_page(page)



    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
