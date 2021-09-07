from django import forms
from stackoverflow.answer.models import Answer


class AnswerForm(forms.ModelForm):
    model = Answer
