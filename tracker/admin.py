from django.contrib import admin

from tracker.models.issue_tracker import IssueTracker
from tracker.models.status import Status
from tracker.models.type import Type

admin.site.register(IssueTracker)
admin.site.register(Type)
admin.site.register(Status)
