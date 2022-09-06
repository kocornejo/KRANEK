from django.contrib import admin
# import your models here
from .models import Deck, Flashcard

# Register your models here
admin.site.register(Deck)
admin.site.register(Flashcard)