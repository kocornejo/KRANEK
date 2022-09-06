

from .models import Quiz, Question

class QuizForm(ModelForm):
  class Meta:
    model = Quiz
    fields = ['title']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer']