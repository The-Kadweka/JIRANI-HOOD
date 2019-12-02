from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import messages
from . forms import *
from django.contrib.auth.models import User

# Create your views here.
# Views for hood
@login_required(login_url='/accounts/login/')
def home(request):
    hoods = Hood.objects.all()
    return render(request,'home.html',locals())


@login_required(login_url='/accounts/login/')
def upload_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            hood.owner= current_user
            upload.save()
            return redirect('home')
    else:
        form = HoodForm()
    return render(request, 'upload_hood.html', locals())


@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.profile.hood
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    businesses = Business.get_business(hood_id)
    posts = Post.get_post(hood_id)

    return render(request,'hood.html',locals())


@login_required(login_url='/accounts/login')
def join(request,hood_id):
    hood = Hood.objects.get(id=hood_id)
    current_user = request.user
    current_user.profile.hood = hood
    current_user.profile.save()
    return redirect('hood',hood_id)


@login_required(login_url='/accounts/login')
def leave(request,hood_id):
    current_user = request.user
    current_user.profile.hood = None
    current_user.profile.save()
    return redirect('home')


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_hood = Hood.search_hood(search_term)
        message = f"{search_term}"

        return render(request, 'search_hood.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
    
    
# Views for profile
@login_required(login_url='/accounts/login/')
def profile(request, username):

    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        pass
    user = request.user
    profile = User.objects.get(username=username)
    title = f'@{profile.username} '

    return render(request, 'profile.html', locals()) 


@login_required(login_url='/accounts/login/')
def edit(request):
    current_user = request.user
    user = Profile.objects.get(user=current_user)
    profile = User.objects.get(username=request.user)


    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'edit_profile.html', locals()) 


# business views
@login_required(login_url='/accounts/login')
def upload_business(request):
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.user=request.user
            upload.hood=request.user.profile.hood
            upload.save()
        return redirect('hood',request.user.profile.hood.id)
    else:
        businessform = BusinessForm()
    return render(request,'business.html',locals())  


def search_category(request):
    location = Location.objects.all()
    category = Category.objects.all()
    if 'Category' in request.GET and request.GET["Category"]:
        category = request.GET.get("Category")
        searched_business = Business.search_by_category(category)
        message = f"{category}"

        return render(request,'search_business.html', {"message":message,"Category":searched_business})

    else:
        message = "You haven't searched for anything"
        return render(request,'search_business.html',{"message":message})
    
    
def filter_location(request):
    locations = Location.objects.all()
    location = request.GET.get("location")

    searched_image = Hood.filter_by_location(location)
    message = f"{location}"

    return render(request,'category/location.html', {"message":message,"location":searched_image, "locations":locations})    


# Post view
@login_required(login_url='/accounts/login')
def add_post(request):
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.profile = request.user.profile
            post.user = request.user
            post.hood=request.user.profile.hood
            post.save()
            return redirect('hood',request.user.profile.hood.id)
    else:
        postform = PostForm()
    return render(request,'upload_post.html',locals())