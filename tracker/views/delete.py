from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tracker.models.issue_tracker import IssueTracker


class Delete(DeleteView):
    model = IssueTracker

    def get_success_url(self):
        return reverse_lazy('main')
