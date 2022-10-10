from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

from tracker.models.issue_tracker import IssueTracker


class MaxLengthValidator(BaseValidator):
    message = 'Заголовок должен быть менее 20 символов'
    code = 'too_long'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)


class MinLengthValidator(BaseValidator):
    message = 'Заголовок должен быть более 2 символов'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


class AddEditForm(forms.ModelForm):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок',
                              validators=(MinLengthValidator(2), MaxLengthValidator(20)))

    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].widget.attrs.update(
            {'placeholder': 'Введите название', 'type': 'text', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Введите описание', 'type': 'text', 'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if IssueTracker.objects.filter(summary=summary).exists():
            raise ValidationError('Запись с таким названием уже существует')
