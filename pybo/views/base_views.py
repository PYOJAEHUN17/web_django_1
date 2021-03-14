import math

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.db.models import Q

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page','1')  #페이지 초깃값
    kw = request.GET.get('kw','')

    # 조회
    question_list = Question.objects.order_by('-create_date') #order_by('-a'):a를 역순으로 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)|
            Q(subject__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(answer__author__username__icontains=kw)
        ).distinct()
    #페이징 처리
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    page_range = 10 # 페이지 범위 지정 1~10
    current_block = math.ceil(int(page)/page_range) #해당페이지의 블럭

    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]

    end_page = math.ceil(page_obj.paginator.count / page_range)
    context = {
        'question_list' : page_obj,
        'p_range' : p_range,
        'end_page' : end_page,
        'page': page,
        'kw': kw,
    }
    return render(request, 'pybo/question_list.html', context) # render 화면 출력

def detail(request, question_id):
    """
    pybo 출력 내용
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
