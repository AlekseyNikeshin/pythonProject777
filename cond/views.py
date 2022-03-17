from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Cond
from cond.forms import CondForm
# Create your views here.
def cond_list(request):
    conds=Cond.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return  render(request,"cond/cond_list.html",{'conds':conds})

def cond_detail(request, pk):
    cond=get_object_or_404(Cond, pk=pk)
    return render(request, 'cond/cond_detail.html',{'cond':cond})

def cond_new(request):
    if request.method =="POST":
        form = CondForm(request.POST)
        if form.is_valid():
            cond=form.save(commit=False)
            cond.author=request.user
            cond.published_date=timezone.now()
            cond.save()
            return redirect ('cond_detail', pk=cond.pk)
    else:
        form = CondForm()
    return render (request,'cond/cond_edit.html', {'form':form})

def cond_edit(request, pk):
    cond= get_object_or_404(Cond,pk=pk)
    if request.method=="POST":
        form=CondForm(request.POST,instance=cond)
        if form.is_valid():
            cond=form.save(commit =False)
            cond.author=request.user
            cond.published_date=timezone.now()
            cond.save()
            return redirect ('cond_detail',pk=cond.pk)
    else:
        form=CondForm(instance=cond)
    return render(request,'cond/cond_edit.html',{'form':form})


