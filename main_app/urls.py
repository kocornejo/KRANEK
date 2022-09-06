from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('decks/', views.decks_index, name='index'),
    path('decks/<int:deck_id>/', views.decks_detail, name='detail'),
    path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
    path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
    path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),
    path('decks/<int:deck_id>/assoc_flashcard/<int:flashcard_id>/', views.assoc_flashcard, name='assoc_flashcard'),
    path('flashcards/', views.FlashcardList.as_view(), name='flashcards_index'),
    path('flashcards/<int:pk>/', views.FlashcardDetail.as_view(), name='flashcards_detail'),
    path('flashcards/create/', views.FlashcardCreate.as_view(), name='flashcards_create'),
    path('flashcards/<int:pk>/update/', views.FlashcardUpdate.as_view(), name='flashcards_update'),
    path('flashcards/<int:pk>/delete/', views.FlashcardDelete.as_view(), name='flashcards_delete'),
]