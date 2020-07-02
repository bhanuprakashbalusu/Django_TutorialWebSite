from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request, "main/series.html", context={"part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        matching_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutlist_series = Tutorial.objects.filter(tutorial_series__tutorial_series=matching_tutorial.tutorial_series).order_by("tutorial_published")
        this_tut_idx = list(tutlist_series).index(matching_tutorial)
        return render(request, "main/tutorial.html", context={"matching_tutorial": matching_tutorial, "side_bar":tutlist_series, "this_tut_idx": this_tut_idx})


    return HttpResponse(f"{single_slug} does not correspond to anything!!!")


def homepage(request):
    return render(
                  request=request,
                  template_name="main/categories.html",
                  context={"categories": TutorialCategory.objects.all}
                  )

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created: {username}')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "main/register.html", context={"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "main/login.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")