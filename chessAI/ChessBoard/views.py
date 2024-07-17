from django.shortcuts import render

# Create your views here.


def ChessPlay(request):
    return render(request, 'chess.html')