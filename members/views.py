from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

class RegisterView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', self.get_context_data(**kwargs))
