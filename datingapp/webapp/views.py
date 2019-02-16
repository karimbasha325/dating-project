from django.shortcuts import render, get_object_or_404
from webapp.models import Booktickets
from webapp.forms import FormModel,SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your views here.
def IndexView(request):
    return render(request,'webapp/base.html')

def resortview(request):
    return render(request,'webapp/resorts.html')

def aboutview(request):
    return render(request,'webapp/about.html')

def serviceview(request):
    return render(request,'webapp/service.html')

def successview(request):
    return render(request,'webapp/success.html')

def logout_view(request):
    return render(request,'registration/logout.html')

@login_required
def Bookticketview(request):
    form=FormModel()
    if request.method=='POST':
        form=FormModel(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    return render(request,'webapp/book.html',{'form':form})

def signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'webapp/signup.html',{'form':form})

class UserDetails(DetailView):
    model=User

class BookticketsDetail(DetailView):
    model=Booktickets

def Booktickets_list(request):
    booktickets_list=Booktickets.objects.all()
    return render(request,'webapp/booktickets_list.html',{'booktickets_list':booktickets_list})



#@login_required
#def BookingDate(request):
#    if request.method=='POST':
#        form=DateForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('webapp/book.html')
#    else:
#        form=DateForm(request.POST)
#    return render(request,'webapp.date.html',{'form':form})





#def Booktickets_list(request):
#    booktickets_list=super().get_queryset().filter(username)
#    return render(request,'webapp/bookticketslist.html',{'booktickets_list':booktickets_list})



#from webapp.forms import EmailForm
#from django.core.mail import send_mail
#sent=False
#def Email_send_view(request,id):
#    form=get_object_or_404().filter(status='booked')
#    if request.method=='POST':
#        cd=form.cleaned_data
#        form=EmailForm(request.POST)
#        subject="Booking Confirmation"
#        ticket=for.get_object_or_404().filter(status="booked")
#        meassage="Your tickets has booked and for your confirmation {}".format()
