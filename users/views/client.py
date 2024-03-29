from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..models import User
from ..forms import ClientSignUpForm


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = 'client'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')    