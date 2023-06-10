from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from .controllers import *
from .models import Answer



def render_main_page(request):
    category_id = request.GET.get('id')
    questions = get_all_questions_by_category(category_id)
    answer_form = AnswerForm()
    return render(request, 'main.html', {'questions': questions,
                                         'answer_form': answer_form})


@login_required()
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        selected_category_id = form.data.get('category')
        if form.is_valid():
            create_question_with_success_message(request, form)
        else:
            messages.error(request, 'There was an error while posting your question')
        return redirect(f'/?id={selected_category_id}')


@login_required()
def create_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            create_answer_with_success_message(request, form)
        else:
            messages.error(request, 'There was an error while posting your answer')
        return redirect('categories_page')


def categories_page(request):
    categories = get_all_categories()
    return render(request, 'categories.html', {'categories': categories})


def search(request):
    query = request.GET.get('q')
    questions = search_questions_by_query(query)
    return render(request, 'search_results.html', {'questions': questions,
                                                   'query': query})


def question_page(request):
    question_pk = request.GET.get('pk')
    question = get_question_by_pk(question_pk)
    answer_form = AnswerForm()
    return render(request, 'question.html', {'question': question,
                                             'answer_form': answer_form})


def render_ask_question_page(request):
    question_form = QuestionForm()
    return render(request, 'ask_question.html', {'question_form': question_form})


def render_user_questions(request):
    questions = get_questions_for_user(request.user)
    answers = get_answers_for_user(request.user)
    return render(request, 'user_questions.html', {'questions': questions, 'answers': answers})


def edit_question(request, question_id):
    return edit_record(request, Question, QuestionForm, question_id)


def edit_answer(request, answer_id):
    return edit_record(request, Answer, AnswerForm, answer_id)


def delete_question(request, question_id):
    return delete_record(request, Question, question_id)


def delete_answer(request, answer_id):
    return delete_record(request, Answer, answer_id)


@login_required
def upvote(request, object_name, object_id):
    model = Question if object_name == "Question" else Answer
    upvote_controller(request.user, model, int(object_id))
    return redirect('/')


@login_required
def downvote(request, object_name, object_id):
    model = Question if object_name == "Question" else Answer
    downvote_controller(request.user, model, int(object_id))
    return redirect('/')

