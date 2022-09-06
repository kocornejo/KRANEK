from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
# Importing or model here
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Login and create a user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Deck, Flashcard, Quiz, Question
from .forms import QuizForm, QuestionForm



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

# Add new view
def decks_index(request):
  decks = Deck.objects.all()
  return render(request, 'decks/index.html', { 'decks': decks })

def decks_detail(request, deck_id):
  deck = Deck.objects.get(id=deck_id)
  flashcards_deck_doesnt_have = Flashcard.objects.exclude(id__in = deck.flashcards.all().values_list('id'))
  return render(request, 'decks/detail.html', { 'deck': deck, 'flashcards': flashcards_deck_doesnt_have })

def assoc_flashcard(request, deck_id, flashcard_id):
  Deck.objects.get(id=deck_id).flashcards.add(flashcard_id)
  return redirect('detail', deck_id=deck_id)


class DeckCreate(CreateView):
  model = Deck
  fields = ['name', 'subject']
  success_url = ['/decks/']

class DeckUpdate(UpdateView):
  model = Deck
  fields = '__all__'

class DeckDelete(DeleteView):
  model = Deck
  success_url = '/decks/'

class FlashcardList(ListView):
  model = Flashcard

class FlashcardDetail(DetailView):
  model = Flashcard

class FlashcardCreate(CreateView):
  model = Flashcard
  fields = '__all__'

class FlashcardUpdate(UpdateView):
  model = Flashcard
  fields = ['name']

class FlashcardDelete(DeleteView):
  model = Flashcard
  success_url = '/flashcards/'

#========================================== My quizzes view ======================================================#

@login_required
def add_quiz(request, profile_id):
    form = QuizForm(request.POST)
    if form.is_valid():
        new_quiz = form.save(commit=False)
        new_quiz.profile_id = profile_id
        new_quiz.save()
    return redirect('detail', profile_id=profile_id)

@login_required
def quiz_detail(request, quiz_id):
  quiz = Quiz.objects.get(id=quiz_id)
  quiz_form = QuizForm()
  questions = Question.objects.filter(quiz=quiz)
  return render(request, 'quiz/detail.html',{
    'quiz': quiz, 
    'quiz_form':quiz_form,
    'questions': questions,
  })

@login_required
def quizUpdate(request, UpdateView):
    model = Quiz
    fields = ['title']
#Use this if above doesnt work
def quiz_update(request, profile_id):
    form = QuizForm(request.POST)
    if form.is_valid():
        new_quiz = form.save(commit=False)
        new_quiz.profile_id = profile_id
        new_quiz.save()
    return redirect('detail', profile_id=profile_id)

@login_required
def quizDelete(request, DeleteView):
    model = Quiz
    success_url = '/quiz/'

@login_required
def add_question(request, quiz_id,):
  form = QuestionForm(request.Post)
  if form.is_valid():
    new_question = form.save(commit=False)
    new_question.quiz_id = quiz_id
    new_question.save()
  return redirect('details', quiz_id=quiz_id)
#Use this if above doesnt work
def add_question(request, quiz_id, question_id):
  Quiz.objects.get(id=quiz_id).question.add(question_id)
  return redirect('detail', quiz_id=quiz_id)

@login_required
def remove_question(request, quiz_id, question_id):
  Quiz.objects.get(id+quiz_id).question.remove(question_id)
  return redirect('detail', quiz_id=quiz_id)

@login_required
def question_update(request, UpdateView, quiz_id):
    form = QuestionForm(request.POST)
    if form.is_valid():
        new_question = form.save(commit=False)
        new_question.quiz_id = quiz_id
        new_question.save()
    return redirect('detail', quiz_id=quiz_id)



@login_required
def question_delete(request, DeleteView, quiz_id):
    form = QuestionForm(request.Delete)
    if form.is_valid():
        new_question = form.save(commit=False)
        new_question.quiz_id = quiz_id
        new_question.remove()
    return redirect('detail', quiz_id=quiz_id)


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

#=======================oooo=======================================================================#