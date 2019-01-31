from django.shortcuts import render, redirect
from .models import Board, Comment
import requests
from bs4 import BeautifulSoup

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
    url = "https://search.naver.com/search.naver?where=image&query="
    board = Board.objects.get(pk=id)
    res1 = requests.get(url+board.content1).text
    res2 = requests.get(url+board.content2).text
    soup1 = BeautifulSoup(res1,"html.parser")
    soup2 = BeautifulSoup(res2,"html.parser")
    jpg1 = soup1.select_one("#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img").get("data-source")
    jpg2 = soup2.select_one("#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img").get("data-source")
    comment1 = board.comment_set.all().filter(checkValue=1).count()
    comment2 = board.comment_set.all().filter(checkValue=2).count()
    return render(request, "board/read.html", {'board':board, "comment1":comment1, "comment2":comment2, "jpg1":jpg1, "jpg2":jpg2})
    
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