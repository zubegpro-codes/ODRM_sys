from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import CustomUser,Comments, Category, Location, Report
from django.db.models import Q
from  django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from base.forms import Categoryform, MyUserCreationForm, Commentform, ReportForm, UserForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
import json
from django.shortcuts import get_object_or_404

def loginpage(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=email, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html',context)


def registerPage(request):
    page = 'Register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            print('login')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was an error in the form submission.')
    return render(request, 'base/login_register.html', {'form':form, 'page':page})


def logoutUser(request):
    logout(request)
    return redirect('home')


def userProfile(request, pk):
    user = CustomUser.objects.get(id=pk)
    report = user.reports.all()
    reports_comment = user.comments_set.all()
    topics = Category.objects.all()
    context = {'user':user, 'reports': report, 'reports_comment':reports_comment, 'topics': topics}
    return render(request, 'base/user_profile.html', context)


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    context ={'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', context)


def home(request):
    q = request.GET.get('h') if request.GET.get('h') != None else ''
    print(q)
    reports = Report.objects.filter(
        Q( topic__name__icontains=q)|
        Q( user__username__icontains = q)|
        Q( description__icontains = q)
    )
    reports_count = reports.count()
    d_repo= 'Disaster Report'
    rate = 'Rate'
    chart_data = [[d_repo, rate]]
    topics = Category.objects.all()[0:5]
    charttopics = Category.objects.all()
    for charttopic in charttopics:
        chart_data.append([charttopic.name, charttopic.report_set.all().count()])


    d_repo_json = json.dumps(d_repo)
    rate_json = json.dumps(rate)
    chart_data_json =json.dumps(chart_data)

    reports_comment = Comments.objects.filter(Q(report__topic__name__icontains=q))
    
    
    
    
    context={
        'reports':reports,
        'topics': topics,
        'reports_comment': reports_comment,
        'reports_count': reports_count,
        'd_repo_json':d_repo_json,
        'rate_json':rate_json,
        'chart_data_json':chart_data_json,
    }
    return render(request, 'base/index.html', context)


def topicspage(request):
    q = request.GET.get('h') if request.GET.get('h') != None else ''
    topics= Category.objects.filter(name__icontains=q)
    context ={'topics':topics}
    return render(request, 'base/topics.html', context)


def activitypage(request):
    q = request.GET.get('h') if request.GET.get('h') != None else ''
    report_comments = Comments.objects.filter(Q(report__topic__name__icontains=q))[0:8]
    context ={'report_comments':report_comments}
    return render(request, 'base/activity.html', context)


@login_required(login_url='login')
def createReport(request):
    topics = Category.objects.all()
    user = request.user
    form = ReportForm()
    

    if request.method == 'POST':
        print(request.POST)
        topic_name = request.POST.get('topic')
        form = ReportForm(request.POST, request.FILES,)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = user
            report.save()
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'There was an error in the form submission.')
            
        
    context = {'form': form, 'topics': topics}
    return render(request, 'base/report_form.html', context)


@login_required(login_url='login')
def deleteReport(request, pk):
    report = Report.objects.get(id = pk)
    if request.user != report.user:
        return render(request, 'base/permision.html', {'obj': report})
    
    if request.method == 'POST':
        report.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': report})


def report(request, pk):
    form= Commentform()
    reports= Report.objects.filter(id=pk)
    report = Report.objects.get(id=pk)
    comentors = report.contributors.all()
    coments = Comments.objects.filter(report=report).order_by('-updated')
    if request.method == 'POST':
        formdata= Commentform(request.POST)
        if formdata.is_valid():
            data = formdata.cleaned_data
            message = Comments.objects.create(
                user = request.user,
                report = report,
                body = data['coment_body'],
            )
        report.contributors.add(request.user)
        return redirect('report', pk= report.id)
    context = {'reports': reports, 'coments':coments, 'commentform':form, 'comentors ':comentors, }
    return render(request, 'base/report.html',context)


def update_report_status(request):
    data= json.loads(request.body)
    reportId= data['reportId']
    action= data['action']  
    instance = get_object_or_404(Report, id = reportId) 
    if action == 'Inprogres':
        instance.status = action
        instance.save()
    elif action == 'Resolved':
        instance.status = action
        instance.save()

    print('action', action)
    print('reportId', reportId)
    
    return JsonResponse({'message':'itemwasadded' })


def createTopic(request):
    form= Categoryform()
    if request.method == 'POST':
        formReturn = Categoryform(request.POST)
        if formReturn.is_valid():
            toptopic = formReturn.save(commit=False)
            
            changeTopicCase = toptopic.name.title()
            toptopic.name = changeTopicCase
    
            topic, created = Category.objects.get_or_create(name=changeTopicCase)
            topic.save()
            return redirect('home')
    return render(request, 'base/create_topic.html', context = {'form': form})

            
def creatgroup(request):
    if request.method == 'POST':
        print(request)
    makestaff =0
    # instance = get_object_or_404(CustomUser, is_staff = makestaff) 
    



    return render(request, 'base/create_group.html')
    


