from django.shortcuts import render, redirect
from .models import Board, Comment 

# Create your views here.

def index(request):
    boards = Board.objects.all() 
    return render(request, "board/index.html", {'boards':boards})
    
def new(request):
    return render(request, "board/new.html")
    
def create(request):
    title = request.POST.get("title")
    content1 = request.POST.get("content1")
    content2 = request.POST.get("content2")
    
    Board.objects.create(title=title, content1=content1, content2=content2)
    
    return redirect("/board/")
    
def read(request, id):
    board = Board.objects.get(pk=id)
    comments = board.comment_set.all()
    comment1,comment2 = (0,0)
    for comment in comments:
        if comment.checkValue == 1:
            comment1 += 1
        else:
            comment2 += 1
    return render(request, "board/read.html", {'board':board, "comment1":comment1, "comment2":comment2})
    
def delete(request, id):
    Board.objects.get(pk=id).delete()
    return redirect("/board/")
    
def edit(request, id):
    board = Board.objects.get(pk=id)
    return render(request, "board/edit.html", {'board': board})
    
    
def update(request, id):
    title = request.POST.get("title")
    content1 = request.POST.get("content1")
    content2 = request.POST.get("content2")
    Board.objects.filter(pk=id).update(title=title, content1=content1, content2=content2)
    return redirect(f"/board/{id}/")
    
def comment_create(request, id):
    board = Board.objects.get(pk=id)
    checkValue = request.POST.get("checkValue")
    content = request.POST.get("content")
    Comment.objects.create(board=board, checkValue=checkValue, content=content)
    
    return redirect(f"/board/{id}/")

def comment_delete(request, id, cid):
    Comment.objects.get(pk=cid).delete()
    return redirect(f"/board/{id}/")