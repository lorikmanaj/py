from django.shortcuts import render

# Create your views here.
def index(request):
    meetups = [
        { 
            'title' : 'A First Meetup',
            'location': 'NY', 
            'slug': 'first' 
        },
        { 
            'title' : 'A Second Meetup', 
            'location': 'XK', 
            'slug': 'second' 
        },
        { 
            'title' : 'A Third Meetup',
            'location': 'AL',
            'slug': 'third' 
        },
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request):
    selected_meetup = { 
        'title': 'test', 
        'description': 'desc', 
        'location': '' 
        }
    return render(request, 'meetups/meetup-details.html', {
        'meetup-title': selected_meetup['title'],
        'meetup-description': selected_meetup['description']
    })