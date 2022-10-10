from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from tracker.forms import AddEditForm
from tracker.models.issue_tracker import IssueTracker


class EditView(TemplateView):
    template_name = "edit_task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = AddEditForm(instance=context['article'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = AddEditForm(request.POST, instance=article)
        if form.is_valid():
            type = form.cleaned_data.pop('type')
            article = form.save()
            article.type.set(type)
            article.save()
            return redirect('main')
        return render(request, 'edit_task.html', context={'form': form})
