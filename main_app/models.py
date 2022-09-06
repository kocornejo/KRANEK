from django.db import models
from django.urls import reverse



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
