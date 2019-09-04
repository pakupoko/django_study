from django.shortcuts import render, redirect
from .models import *
from .forms import FeedbackForm

#피드백 목록 체크
def list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedbacklist.html', {'feedbacks':feedbacks})

#피드백 생성
def create(request):
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})

#피드백 수정
def edit(request, id):
    fb = Feedback.objects.get(pk=id)
    if request.method=='POST':
        form = FeedbackForm(request.POST, instance=fb)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm(instance=fb)

    return render(request, 'feedback/feedback.html', {'form':form})