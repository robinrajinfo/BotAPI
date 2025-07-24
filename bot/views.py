from django.shortcuts import render
from .models import Bot
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BotSerializer

# HTML View (for normal browser page)
def bot_list(request):
    bots = Bot.objects.all()
    return render(request, 'bot/bot_list.html', {'bots': bots})

# API View (for /api/bots/)
@api_view(['GET', 'POST'])
def bot_list_api(request):
    if request.method == 'GET':
        bots = Bot.objects.all()
        serializer = BotSerializer(bots, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
