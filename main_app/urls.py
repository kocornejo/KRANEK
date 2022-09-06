

urlpatterns = [
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question')
    path('profile/<int:profile_id>/add_quiz/', views.add_quiz, name='add_quiz'),
    path('quiz/<int:pk>/update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),
]