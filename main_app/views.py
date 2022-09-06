from .models import Profile, Quiz, Question
from .forms import QuizForm, QuestionForm



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

