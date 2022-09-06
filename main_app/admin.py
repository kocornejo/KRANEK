from django.contrib import admin
from .models import Deck, Flashcard

# Registering the models
# from .models import #Flashcard, Photo, Quiz

# admin.site.register(Flashcard)
# admin.site.register(Quiz)
# admin.site.register(Photo)

admin.site.register(Deck)
admin.site.register(Flashcard)