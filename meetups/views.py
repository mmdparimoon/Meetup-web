from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant
from .forms import RegistrationForm
# Create your views here.


def index(request):
    meetups=Meetup.objects.all()


    return render(request, 'meetups/index.html', context={'meetups': meetups,
                                                          'show_meetups': True})

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('registration-success'  , meetup_slug=meetup_slug)
                
        return render(request, 'meetups/meetup-details.html',
                              context={'meetup': selected_meetup,
                                       'meetup_found':True,
                                       'registration_form': registration_form})        
    except Exception as exc :
        return render(request, 'meetups/meetup-details.html',
                      context={'meetup_found':False})
        
        
def registration_success(request,meetup_slug):
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', context={'organizer_email': selected_meetup.organizer_email})       