# from django.shortcuts import render

# # Create your views here.
# def index(request):
#   return HttpResponse("Hello , 这里是polls的主页")
# from django.http import HttpResponse,HttpResponseRedirect,Http404
# from django.template import loader
# from .models import Question,Choice
# from django.shortcuts import render,get_object_or_404
# from django.core.urlresolvers import reverse

# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = {
#     'latest_question_list': latest_question_list
#   }
#   # output = ','.join([q.question_text for q in latest_question_list])
#   return HttpResponse(template.render(context,request))
# def detail(request,question_id):
#   try:  
#     question = Question.objects.get(pk=question_id)
#   except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#   return render(request,'polls/detail.html',{'question':question})
#   # return HttpResponse("You are looking at %s" %question_id)
# def results(request,question_id):
#   # response = "You are looking at the results of question %s"
#   # return HttpResponse(response %question_id)
#   question = get_object_or_404(Question,pk=question_id)
#   return render(request, 'polls/results.html', {'question': question})
# def vote(request,question_id):
#   question = get_object_or_404(Question,pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError,Choice.DoesNotExist):
#     return render(request,'polls/detail.html',{
#       'question':question,
#       'error_message':"you didn't select a choice."
#       })
#   else:
#     selected_choice.votes +=1
#     selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
from django.contrib.auth.models import User, Group
from polls.models import Question
from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer,QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset =Question.objects.all()
    serializer_class = QuestionSerializer