import random

from django.http import HttpResponse
from dadjokes.settings import JOKES_FILE

def read_jokes():
    with open(JOKES_FILE, 'r') as file:
        return [line for line in file]

JOKES = read_jokes()

def index(request):
    joke = random.choice(JOKES)
    return HttpResponse(joke)
