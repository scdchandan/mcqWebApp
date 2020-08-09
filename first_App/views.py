from django.shortcuts import render
from django.http import HttpResponse
from first_App.models import UserProfileInfo,Question
from first_App.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'first_App/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def home(request):
    return render(request,'first_App/home.html')

def register(request):

    registered = False

    if request.method == "POST" :
        user_form = UserForm(data = request.POST)
        # profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() :

             user = user_form.save()
             user.set_password(user.password)
             user.save()

             # profile = profile_form.save(commit = False)
             # profile.user = user
             #
             # if 'profile_pic' in request.FILES:
             #     profile.profile_pic = request.FILES['profile_pic']
             #
             # profile.save()

             registered = True

        else:
            print(user_form.errors)


    else:

        user_form = UserForm()
        # profile_form = UserProfileInfoForm()

    return render(request,'first_App/registration.html',{'user_form' : user_form,

                                                          'registered' : registered})

def user_login(request):

    if request.method == "POST" :

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS")

    else:
        return render(request,'first_App/login.html',{})


def html_quiz(request):
    context = {}
    html_question = Question.objects.filter(category = 'html')
    data = [{'category': q.category,
           'question' : q.question,
           'option1' : q.option1,
           'option2' : q.option2,
           'option3' : q.option3,
           'option4' : q.option4,
           'option_correct' : q.option_correct } for q in html_question]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/html_quiz.html',context)

def css_quiz(request):
    context = {}
    css_question = Question.objects.filter(category = 'css')
    data = [{'category': q.category,
           'question' : q.question,
           'option1' : q.option1,
           'option2' : q.option2,
           'option3' : q.option3,
           'option4' : q.option4,
           'option_correct' : q.option_correct } for q in css_question]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/css_quiz.html',context)

def nodejs_quiz(request):
    context = {}
    nodejs_question = Question.objects.filter(category = 'nodejs')
    data = [{'category': q.category,
           'question' : q.question,
           'option1' : q.option1,
           'option2' : q.option2,
           'option3' : q.option3,
           'option4' : q.option4,
           'option_correct' : q.option_correct } for q in nodejs_question]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/nodejs_quiz.html',context)

def javascript_quiz(request):
    context = {}
    javascript_question = Question.objects.filter(category = 'javascript')
    data = [{'category': q.category,
           'question' : q.question,
           'option1' : q.option1,
           'option2' : q.option2,
           'option3' : q.option3,
           'option4' : q.option4,
           'option_correct' : q.option_correct } for q in javascript_question]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/javascript_quiz.html',context)

def python_quiz(request):
    context = {}
    jpython_question = Question.objects.filter(category = 'python')
    data = [{'category': q.category,
           'question' : q.question,
           'option1' : q.option1,
           'option2' : q.option2,
           'option3' : q.option3,
           'option4' : q.option4,
           'option_correct' : q.option_correct } for q in python_question]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/python_quiz.html',context)

def submit_quiz(request,category):
    if request.method == 'POST':
        score = 0
        i = 0
        questions = Question.objects.filter(category = category)
        data = [{'option_correct' : q.option_correct } for q in questions]
        print(data)
        for d in data:
            i = i + 1
            print(i)
            x = request.POST.get(str(i))
            print(x)
            print(d['option_correct'])
            print(d)
            if x == d['option_correct']:
                score = score + 1
        print(score)
        return render(request,'first_App/submit.html',{'category':category, 'score' : score})




# def login(request):
#
#     form = NewUserForm()
#
#     if request.method == "POST" :
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit = True)
#             return index(request)
#
#         else :
#             print("NOT DONE")
#
#     return render(request,'first_App/login.html',{'form' : form})
