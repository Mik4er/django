from django import forms
from .models import Question, Answer, Category


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'category']
        labels = {
            'title': 'Title',
            'text': 'Text',
            'category': 'category'
        }
        category = forms.ModelChoiceField(queryset=Category.objects.all())
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': 'Text'}
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})}