from django.shortcuts import render, redirect
from .form import SampleForm
# Create your views here.
def home_view(request):
    form = SampleForm()
    return render(request, 'form_app/home.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.clean_email()
            return redirect('contact_success')
    else:
        form = SampleForm()
    return render(request, 'form_app/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')