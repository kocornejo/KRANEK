from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from .views import Profile

# Need to import Profile

#================================================================================================#

# Create our models here


class Flashcard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flashcards_detail', kwargs={'pk': self.id})


class Deck(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    flashcards = models.ManyToManyField(Flashcard)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'deck_id': self.id})

# class Card(models.Model):
class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.id})

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)


    def _str_(self):
        return self.name

    def get_absolute_url(self):

        return reverse('quiz_detail', kwargs={'quiz_id': self.id})




   
# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     flashcard = models.ForeignKey(Card, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Question, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"photo for card_id: {self.flashcard_id} @{self.url}"
#         return f"photo for question_id: {self.flashcard_id} @{self.url}"
