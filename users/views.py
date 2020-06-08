from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from users.forms import RegisterForm

from users.models import Post,Pricing,About

# Create your views here.

# Create signup views for registration
# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/accounts/login/")
		else:
			return redirect("/accounts/signup/")

	else:
		form = RegisterForm()

	return render(response, "signup.html", {"form":form})


def logout(request):
	auth.logout(request)
	return redirect("")


def home(request):
	post_list = list(Post.objects.all())
	
	return render(request, 'home.html', {'post_list':post_list})

def pricing(request):
	pricing_list = list(Pricing.objects.all())

	return render(request, 'pricing.html', {'pricing_list': pricing_list})


def about(request):
	about_list = list(About.objects.all())

	return render(request, 'about.html', {'about_list': about_list})

