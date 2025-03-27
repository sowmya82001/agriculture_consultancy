from django.shortcuts import render, redirect
from .models import Consultant, Booking, CropRecommendation
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .forms import ContactForm
from .models import ContactMessage



def home(request):
    return render(request, 'consultancy/home.html')

@login_required
def book_consultant(request):
    consultants = Consultant.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'consultancy/book.html', {'form': form, 'consultants': consultants})

def crop_recommendation(request):
    crops = CropRecommendation.objects.all()
    return render(request, 'consultancy/crops.html', {'crops': crops})

def booking_success(request):
    return render(request, 'consultancy/booking_success.html')
    return redirect('home')  # Change 'home' to an existing URL name

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can save the data to the database or send an email
            return redirect('contact_success')  # Redirect to success page
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('contact_success')  # Redirect to success page
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})