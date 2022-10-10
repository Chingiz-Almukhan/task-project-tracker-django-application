from django import forms

from tracker.models.issue_tracker import IssueTracker


class AddEditForm(forms.ModelForm):
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
