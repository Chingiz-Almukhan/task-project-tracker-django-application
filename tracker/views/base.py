from django.shortcuts import render
from django.views.generic import View

from tracker.models.issue_tracker import IssueTracker


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = IssueTracker.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'main_page.html', context)
