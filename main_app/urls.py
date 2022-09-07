from django.urls import path
from . import views 
# from . views import UserEditView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='edit_profile'),

    # Add the path for the signup 
    path('accounts/signup/', views.signup, name='signup'), # Signup url
    # path('edit_profile/', UserEditView.as_view()),

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

    path('quiz/create/', views.QuizCreate.as_view(), name='quiz_create'),
    path('quizzes/', views.quiz_index, name='quiz_index'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:pk>/update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    
    path('quiz/<int:quiz_id>/assoc_question/<int:question_id>/', views.assoc_question, name='assoc_question'),
    path('quiz/<int:quiz_id>/unassoc_question/<int:question_id>/', views.unassoc_question, name='unassoc_question'),

    path('questions/create/', views.QuestionCreate.as_view(), name='question_create'),
    path('questions/', views.QuestionList.as_view(), name='question_index'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('questions/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),
    path('questions/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),
]