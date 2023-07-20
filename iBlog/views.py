from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from .forms import usersForms

def blogsPage(request) :
    if request.method == "POST":
        return render(request, "allBlogs.html")

@login_required(login_url="login")
def allBlogs(request):

    categorydata = Category.objects.all()

    data={
        'categorydata':categorydata
    }

    return render(request, "allBlogs.html",data)


def logout_page(request):
    logout(request)
    return redirect('/login/')
def homePage(request):
    data={}
    try:
        if request.method=="POST":
        # n1 = request.GET['num1']
        # n2 = request.GET['num2']
            if request.POST.get('num1')=="":
                return render(request, "index.html",{'error':True})
            elif request.POST.get('num2')=="":
                return render(request, "index.html", {'error': True})
            elif request.POST.get('num3')=="":
                return render(request, "index.html", {'error': True})
            elif request.POST.get('num4')=="":
                return render(request, "index.html", {'error': True})
            elif request.POST.get('num5')=="":
                return render(request, "index.html", {'error': True})
            username = request.POST.get('num1')
            email = request.POST.get('num2')
            password = request.POST.get('num3')
            first_name = request.POST.get('num4')
            last_name = request.POST.get('num5')
            # data={
            #     'username' : username,
            #     'email' : email,
            #     'password' : password,
            #     'first_name' : first_name,
            #     'last_name' : last_name
            # }

            user = User.objects.filter(username = username)

            if user.exists():
                messages.info(request,'Username already exist')
                return redirect('/')

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username
            )

            user.set_password(password)
            user.save()
            messages.info(request, 'Account created successfully')
            return redirect('/login/')

    except:
        pass
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse("<b>Welcome</b>")

def course(request):
    return HttpResponse("Welcome to Django course")

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def login_page(request):
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request, "login.html", {'error': True})
        elif request.POST.get('num2') == "":
            return render(request, "login.html", {'error': True})

        username = request.POST.get('num1')
        password = request.POST.get('num2')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            # messages.info(request, 'Account created successfully')
            return redirect('/blogs/')

    return render(request,'login.html')

@login_required(login_url="login")
def saveBlog(request):
    if request.method=="POST":
        title = request.POST.get('num5')
        description = request.POST.get('num1')
        url =request.POST.get('num2')
        en = Category(title = title , description = description , url = url )
        en.save()
        return render(request, "allBlogs.html")
    return render(request,"blogs.html")
