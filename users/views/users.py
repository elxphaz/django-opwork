from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from ..models import User

class SignUpView(TemplateView):
    template_name = "registration/register.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    
    
class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "users/auth/profile.html"
    login_url = '/accounts/login/'
    redirect_field_name = "redirect_to"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context["user"] = User.objects.get(pk=user_id)
        return context

def logout_view(request):
    logout(request)
    return redirect('home')