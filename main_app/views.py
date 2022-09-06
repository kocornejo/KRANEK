from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
# Importing or model here
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Login and create a user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

import uuid
import boto3
# This makes it so we need to be logged in, in order to see all the other pages
from django.contrib.auth.mixins import LoginRequiredMixin    # This is to authorize our class based views
from django.contrib.auth.decorators import login_required

# from .models import Quiz, Question, Flashcard, Card, Photo

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'kranek' # Make a kranek bucket so we can import photos (not set up yet)

#============================================= Adding the Signup form ===================================================#

def signup(request):
   # this will handle the POST Request to /accounts/signup
  # Will process the form submission, add the form data to the database
  # login the user
  error_message = ''

  if request.method == 'POST':
    # create the user from the form object
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # save the form, this adds the user to database
      user = form.save()
      # login the user using the login function that we import above 
      login(request, user) # this assings to every request the user object, so in function based views we have request.user, cbv self.request.user (inside a method)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again!'

  # this will handle the GET request /accounts/signup 
  # We want to render a template with a form that has inputs pertaining to creating a user
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

#========================================== Create a user profile after sign-up ======================================================#

class CreateProfilePageView(CreateView):

class EditProfilePageView(generic.UpdateView):

class ShowProfilePageView(DetailView):

class DeleteProfilePageView(DeleteView):

#========================================== Main home page ======================================================#

# Define the home view
def home(request):
  return HttpResponse('<h1>༼ つ ◕_◕ ༽つ SUMMON THE KRAKEN ༼ つ ◕_◕ ༽つ</h1>')

def about(request):
    return render(request, 'about.html')

#============================================ My flashcard view ====================================================#
@login_required 
def flashcard_index(request):

def flashcard_detail(request, flashcard_id):

class FlashcardCreate(LoginRequiredMixin, CreateView):


class FlashcardUpdate(UpdateView):


class FlashcardDelete(DeleteView):

def add_card(request, flashcard_id):

#========================================== My quizzes view ======================================================#

def quiz_index(request):

def quiz_detail(request, quiz_id):

class QuizCreate(LoginRequiredMixin, CreateView):

# change name and put in correct spot
def add_quiz(request, profile_id):
    form = QuizForm(request.POST)
    if form.is_valid():
        new_quiz = form.save(commit=False)
        new_quiz.profile_id = profile_id
        new_quiz.save()
    return redirect('detail', profile_id=profile_id)


class QuizUpdate(UpdateView):


class QuizDelete(DeleteView):

def add_question(request, quiz_id):

#============================================= Inserting a photo ===================================================#

def add_photo(request,cat_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, flashcar_id=flashcard_id)
        except:
            print('An error accoured uploading file to S3')
    return redirect('detail', flashcard_id=flashcard_id)

#===================================================================================================================#