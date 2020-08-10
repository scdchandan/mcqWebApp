from django.shortcuts import render
from django.http import HttpResponse
from first_App.models import UserProfileInfo,Test,Scores
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

def stud_home(request):
    return render(request,'first_App/stud_home.html')

def teacher_home(request):
    return render(request,'first_App/teacher_home.html')

def takeaquiz(request):
    return render(request,'first_App/takeaquiz.html')

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


def html_quiz(request,pk):
    context = {}
    tests = Test.objects.filter(pk = pk)

    data = [{'pk':t.pk,
             'q1':t.questiona,'q1o1':t.optiona1,'q1o2':t.optiona2,'q1o3':t.optiona3,'q1o4':t.optiona4,
             'q2':t.questionb,'q2o1':t.optionb1,'q2o2':t.optionb2,'q2o3':t.optionb3,'q2o4':t.optionb4,
             'q3':t.questionc,'q3o1':t.optionc1,'q3o2':t.optionc2,'q3o3':t.optionc3,'q3o4':t.optionc4,
             'q4':t.questiond,'q4o1':t.optiond1,'q4o2':t.optiond2,'q4o3':t.optiond3,'q4o4':t.optiond4,
             'q5':t.questione,'q5o1':t.optione1,'q5o2':t.optione2,'q5o3':t.optione3,'q5o4':t.optione4,

            } for t in tests]

    context.update({'data' : data})
    print(data)
    return render(request,'first_App/html_quiz.html',context)

def create_css_quiz(request):
    return render(request,'first_App/create_css_quiz.html')

def create_html_quiz(request):
    return render(request,'first_App/create_html_quiz.html')

def create_nodejs_quiz(request):
    return render(request,'first_App/create_nodejs_quiz.html')

def create_javascript_quiz(request):
    return render(request,'first_App/create_javascript_quiz.html')

def create_python_quiz(request):
    return render(request,'first_App/create_python_quiz.html')

def available_quiz(request,category,username):
    context = {}
    tests = Test.objects.filter(category = category)

    data = [{'category': t.category,
            'pk':t.pk,
           'teacher_name' : t.teacher_name,
           'appeared' : t.appeared_by.split(":").count(username) } for t in tests]
    print(data)
    context.update({'data' : data})
    return render(request,'first_App/available_quiz.html',context)



def css_quiz(request):
    context = {}
    # css_question = Question.objects.filter(category = 'css')
    # data = [{'category': q.category,
    #        'question' : q.question,
    #        'option1' : q.option1,
    #        'option2' : q.option2,
    #        'option3' : q.option3,
    #        'option4' : q.option4,
    #        'option_correct' : q.option_correct } for q in css_question]
    # print(data)
    # context.update({'data' : data})
    return render(request,'first_App/css_quiz.html',context)

def nodejs_quiz(request):
    context = {}
    # nodejs_question = Question.objects.filter(category = 'nodejs')
    # data = [{'category': q.category,
    #        'question' : q.question,
    #        'option1' : q.option1,
    #        'option2' : q.option2,
    #        'option3' : q.option3,
    #        'option4' : q.option4,
    #        'option_correct' : q.option_correct } for q in nodejs_question]
    # print(data)
    # context.update({'data' : data})
    return render(request,'first_App/nodejs_quiz.html',context)

def javascript_quiz(request):
    context = {}
    # javascript_question = Question.objects.filter(category = 'javascript')
    # data = [{'category': q.category,
    #        'question' : q.question,
    #        'option1' : q.option1,
    #        'option2' : q.option2,
    #        'option3' : q.option3,
    #        'option4' : q.option4,
    #        'option_correct' : q.option_correct } for q in javascript_question]
    # print(data)
    # context.update({'data' : data})
    return render(request,'first_App/javascript_quiz.html',context)

def python_quiz(request):
    context = {}
    # python_question = Question.objects.filter(category = 'python')
    # data = [{'category': q.category,
    #        'question' : q.question,
    #        'option1' : q.option1,
    #        'option2' : q.option2,
    #        'option3' : q.option3,
    #        'option4' : q.option4,
    #        'option_correct' : q.option_correct } for q in python_question]
    # print(data)
    # context.update({'data' : data})
    return render(request,'first_App/python_quiz.html',context)

def submit_quiz(request,category,pk,username):
    if request.method == 'POST':
        score = 0
        i = 10
        tests = Test.objects.get(pk = pk)
        s = tests.appeared_by
        tests.appeared_by = s + username + ":"
        print(tests.appeared_by)

        if(request.POST.get("q1ans") == tests.option_a_correct):
            score = score + 2
        if(request.POST.get("q3ans") == tests.option_b_correct):
            score = score + 2
        if(request.POST.get("q3ans") == tests.option_c_correct):
            score = score + 2
        if(request.POST.get("q4ans") == tests.option_d_correct):
            score = score + 2
        if(request.POST.get("q5ans") == tests.option_e_correct):
            score = score + 2

        c = tests.scores
        tests.scores = c + str(score) + ":"
        tests.save()
        result = Scores()
        result.test_pk = pk
        result.username = username
        result.score = str(score)
        result.save()
        print(score)
        return render(request,'first_App/submit.html',{'category':category, 'score' : score, 'total' : i})

def create_quiz(request,category,name):
    created = False
    if request.method == "POST" :
        test = Test()
        test.category = category
        test.teacher_name = name

        test.questiona = request.POST.get('q1')
        test.optiona1 = request.POST.get('q1o1')
        test.optiona2 = request.POST.get('q1o2')
        test.optiona3 = request.POST.get('q1o3')
        test.optiona4 = request.POST.get('q1o4')
        test.option_a_correct = request.POST.get('q1c')

        test.questionb = request.POST.get('q2')
        test.optionb1 = request.POST.get('q2o1')
        test.optionb2 = request.POST.get('q2o2')
        test.optionb3 = request.POST.get('q2o3')
        test.optionb4 = request.POST.get('q2o4')
        test.option_b_correct = request.POST.get('q2c')

        test.questionc = request.POST.get('q3')
        test.optionc1 = request.POST.get('q3o1')
        test.optionc2 = request.POST.get('q3o2')
        test.optionc3 = request.POST.get('q3o3')
        test.optionc4 = request.POST.get('q3o4')
        test.option_c_correct = request.POST.get('q3c')

        test.questiond = request.POST.get('q4')
        test.optiond1 = request.POST.get('q4o1')
        test.optiond2 = request.POST.get('q4o2')
        test.optiond3 = request.POST.get('q4o3')
        test.optiond4 = request.POST.get('q4o4')
        test.option_d_correct = request.POST.get('q4c')

        test.questione = request.POST.get('q5')
        test.optione1 = request.POST.get('q5o1')
        test.optione2 = request.POST.get('q5o2')
        test.optione3 = request.POST.get('q5o3')
        test.optione4 = request.POST.get('q5o4')
        test.option_e_correct = request.POST.get('q5c')

        test.save()



    else:
        created = False
        return render(request,'first_App/create_html_quiz.html')
    return render(request,'first_App/created.html',{'category' : category})

def myscores(request,username):
    context = {}
    result = Scores.objects.filter(username = username)
    for r in result:
        print(r.test_pk)
        print(r.username)
        print(r.score)
    data = [{'category': Test.objects.get(pk = r.test_pk).category,
           'teacher_name' : Test.objects.get(pk = r.test_pk).teacher_name,
           'score' : r.score} for r in result]
    context.update({'data' : data})
    return render(request,'first_App/myscores.html',context)

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
