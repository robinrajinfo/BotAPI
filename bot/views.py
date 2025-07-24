from django.shortcuts import render
from .models import Bot

# Create your views here.
def bot_list(request):
    bots = Bot.objects.all()
    return render(request, 'bot/bot_list.html', {'bots': bots})
    