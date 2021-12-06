from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Q
from .forms import *


def index(request):
    user = request.user
    username = request.user.username
    try:
        reviews = Review.objects.all().order_by('subject')
    except Review.DoesNotExist:
        reviews = None
    context = {'user': user, 'username': username, 'reviews': reviews}
    return render(request, "index.html", context)


def signup_page(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'signup.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def create_review(request):
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'create_review.html', context)


def review_page(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        review = None
        raise Http404
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            if request.user.is_authenticated:
                comment_form.instance.author = request.user
            else:
                comment_form.instance.author = None
            comment_form.instance.review = review
            comment_form.save()
            return HttpResponseRedirect(request.path_info)
    context = {'author': review.author,
               'genre': review.genre,
               'subject': review.subject,
               'text': review.text,
               'pub_date': review.pub_date,
               'rating': review.rating,
               'review': review,
               'comment_form': comment_form}
    return render(request, 'review_page.html', context)


def profile(request, user_id=None):
    if user_id:
        user_author = User.objects.get(id=user_id)
    else:
        user_author = request.user
    user_reviews = Review.objects.filter(author=user_author)
    logged_user = request.user
    context = {
        'user_author': user_author,
        'user_reviews': user_reviews,
        'logged_user': logged_user
    }
    return render(request, 'my_profile.html', context)


class SearchResultsView(ListView):
    model = Review
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Review.objects.filter(
            Q(subject__contains=query) | Q(text__contains=query)
        )
        return object_list
