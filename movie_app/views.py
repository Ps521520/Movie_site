from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Registration,Movie_Data
import pandas as pd


# Create your views here.
logined=[]

def dataset():
    data=Movie_Data.objects.all()
    movie_name=[]
    movie_type=[]
    movie_region=[]
    movie_language=[]
    rating=[]
    links=[]
    for movie in data:
        movie_name.append(movie.MOVIES_NAME)
        movie_type.append(movie.MOVIES_TYPE)
        movie_region.append(movie.MOVIES_REGION)
        movie_language.append(movie.MOVIES_LANGUAGE)
        rating.append(movie.RATINGS)
        links.append(movie.LINKS)
    df={'MOVIES_NAME':movie_name,'MOVIES_TYPE':movie_type,'MOVIES_LANGUAGE':movie_language,'MOVIES_REGION':movie_region,'RATINGS':rating,'LINKS':links}
    df=pd.DataFrame(df)
    print(df)
def home(request):
    return render(request,'home.html')

def login_register(request):
    if 'login' in request.POST:
        return render(request,'login_page.html')
    else:
        return render(request,'register_page.html')

def movie_selection(request):
    data=Movie_Data.objects.all()
    movies=[]
    if 'regional' in request.POST:
        for movie in data:
            if movie.MOVIES_REGION.lower() == request.POST['regional'].lower() or movie.MOVIES_LANGUAGE.lower() == request.POST['regional'].lower():
                movies.append(movie)
        return render(request,'selected.html',{'movies':movies})
    else:
        for movie in data:
            if request.POST['movie_type'].lower() in movie.MOVIES_TYPE.lower():
                movies.append(movie)
        return render(request,'selected.html',{'movies':movies})

def data_page(request):
    if 'login' in request.POST:
        useremail=request.POST['email']
        pwd=request.POST['password']
        users=Registration.objects.all()
        for user in users:
            if useremail == user.email and pwd == user.password:
                movies=Movie_Data.objects.all()
                logined.append(user)
                return render(request,'data_page.html',{'movies':movies,'user':logined[len(logined)-1]})

        return HttpResponse('WRONG PASSWORD')
    elif 'register' in request.POST:
        return render(request,'register_page.html')

def registered(request):
    name=request.POST['name']
    number=request.POST['number']
    state=request.POST['state']
    country=request.POST['country']
    movie_choice=request.POST['movie_choice']
    email=request.POST['email']
    password=request.POST['password']
    user=Registration(name=name,number=number,state=state,country=country,movie_choice=movie_choice,email=email,password=password)
    user.save()
    return HttpResponse('successfully registered')
def profile(request):
    return render(request,'profile.html',{'user':logined[len(logined)-1]})
def history(request):

    return render(request,'history.html')
def recently_viewed(request):
    return render(request,'recently_viewed.html')
def logout(request):
    logined.clear()
    return render(request,'home.html')
