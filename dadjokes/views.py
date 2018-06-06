import random
import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render

from dadjokes.settings import JOKES_FILE

def read_jokes():
    with open(JOKES_FILE, 'r') as file:
        return [line for line in file]

JOKES = read_jokes()

def index(request):
    return render(request, 'dadjokes/index.html')

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'dadjokes/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

@login_required
def joke(request):
    joke = random.choice(JOKES)
    template = loader.get_template('dadjokes/joke.html')
    context = {'joke': joke}
    return HttpResponse(template.render(context, request))
