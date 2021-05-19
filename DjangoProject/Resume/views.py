from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def resumeUpload(request):
    msg = ""
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        form.save()
        msg = "Resume Submited Successfully"
    form = ResumeForm()
    return render(request, 'home.html', {'forms': form, 'msg': msg})
