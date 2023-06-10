from django.contrib import messages
from .models import Question, Category, Answer
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render


def create_question_with_success_message(request, form):
    question = form.save(commit=False)
    question.author = request.user
    question.publish()
    messages.success(request, 'Your question has been successfully posted')


def create_answer_with_success_message(request, form):
    answer = form.save(commit=False)
    question_pk = request.POST.get('question_pk')
    question = Question.objects.get(pk=question_pk)
    answer.question = question
    answer.author = request.user
    answer.publish()
    messages.success(request, 'Your answer has been successfully posted')


def get_all_categories():
    return Category.objects.all()


def search_questions_by_query(query):
    return Question.objects.filter(Q(title__icontains=query) or Q(text__icontains=query))


def get_question_by_pk(pk):
    return get_object_or_404(Question, pk=pk)


def get_all_questions_by_category(category_id):
    if category_id:
        questions = Question.objects.all().filter(category=int(category_id)).prefetch_related('answer_set')
    else:
        questions = Question.objects.all().prefetch_related('answer_set')
    return questions


def get_questions_for_user(user):
    return Question.objects.filter(author=user)


def edit_record(request, model_class, form_class, record_id):
    record = get_object_or_404(model_class, pk=record_id)
    if request.method == 'POST':
        form = form_class(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_class(instance=record)
        return render(request, 'edit_record.html', {'form': form, 'model': model_class.__name__})


def delete_record(request, model_class, record_id):
    record = get_object_or_404(model_class, pk=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('/')
    else:
        return render(request, 'delete_record.html', {'model': model_class.__name__, 'record': record})


def upvote_controller(user, object_name, object_id):
    model = object_name.objects.get(pk=object_id)
    model.add_rating(user.pk)
    print(model.upvotes)


def downvote_controller(user, object_name, object_id):
    model = object_name.objects.get(pk=object_id)
    model.reduce_rating(user.pk)
    print(model.downvotes)

def get_answers_for_user(user):
    return Answer.objects.filter(author=user)

