from django.http import HttpResponse, Http404, HttpResponseRedirect

 # 이 뷰를 호출하려면 이와 연결된 url이 있어야한다. (같은 디렉토리내의 urls.py를 이용하자)

# views는 클라이언트로 부터 요청받는 request, 응답하는 HttpResponse가 있다!
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # get : request.method == 'GET'
    # post : request.method == 'POST'
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # request.POST['choice']가 없는 경우에 KeyError가 발생한다
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # 뷰안에서 url을 하드코딩하지 않게 하기 위해선 template과 다르게 reverse함수를 이용해야한다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # Question에서 pub_date를 order by 한 결과를 5개 슬라이싱한다.
#     # output = ', '.join([q.question_text for q in latest_question_list]) # , 와 결과를 조인한다. - > 문자열로 변경
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     } # context는 mvc의 model임
#
#     return render(request, 'polls/index.html', context) # render라는 함수로 축약가능 - 코드 줄이기
#     # return HttpResponse(template.render(context, request))
# # 뷰는 HttpResponse 객체를 반환하거나, Http404같은 예외 둘중하나를 응답한다.
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id) # 이런식으로 db에 조회할수 있음
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist") # raise는 throw와 같이 에러 발생시키는 파썬 문법
#
#     # 이렇게 try except를 통해 예외처리할수도 있지만 get_object_or_404() 를통해 shortcut으로 예외처리도 가능하다
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/detail.html', {'question': question}) # 세번째 param은 context임
#
#     # return HttpResponse("You're looking at question %s. " % question_id) body에 문자열 넣어서 응답
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})