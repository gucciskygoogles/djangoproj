import django.http
import django.shortcuts

def home(request):
    return django.shortcuts.render(request, 'homepage.html')