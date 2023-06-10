from django.urls import path
from .views import render_main_page, create_question, \
    create_answer, categories_page, search, question_page, \
    render_ask_question_page, render_user_questions, \
    edit_question, edit_answer, delete_question, delete_answer,\
    upvote, downvote

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('categories_page', categories_page, name='categories_page'),
    path('search', search, name='search'),
    path('question_page', question_page, name='question_page'),
    path('ask_question', render_ask_question_page, name='ask_question'),
    path('my_questions', render_user_questions, name='render_user_questions'),
    path('Question/edit/<int:question_id>/', edit_question, name='edit_question'),
    path('Answer/edit/<int:answer_id>/', edit_answer, name='edit_answer'),
    path('Question/delete/<int:question_id>/', delete_question, name='delete_question'),
    path('Answer/delete/<int:answer_id>/', delete_answer, name='delete_answer'),
    path('<str:object_name>/upvote/<int:object_id>/', upvote, name='upvote'),
    path('<str:object_name>/downvote/<int:object_id>/', downvote, name='downvote'),
]
