from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Deck, Flashcard

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>༼ つ ◕_◕ ༽つ SUMMON THE KRAKEN ༼ つ ◕_◕ ༽つ</h1>')

def about(request):
    return render(request, 'about.html')

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
