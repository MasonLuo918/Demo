from django.shortcuts import render
from .models import LectureVideo,Classify
from comment.models import Comment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

def AllVideo(request,column_id):
    VideoAll = LectureVideo.objects.filter(column_id=column_id)
    column = Classify.objects.get(id=column_id)
    return render(request,"video/video.html",{"Videos":VideoAll,"column":column})

def VideoDetail(request,video_id):
    Comments = Comment.objects.filter(video_id=video_id,display=True).order_by("-publish_time")
    request_video = LectureVideo.objects.get(id=video_id)
    return render(request,"video/detail.html",{"video":request_video,"Comments":Comments})

@login_required(login_url='/account/login')
@csrf_exempt
@require_POST
def like_video(request):
    video_id = request.POST.get("id")
    action = request.POST.get("action")
    if video_id and action:
        try:
            video = LectureVideo.objects.get(id=video_id)
            if action == "like":
                video.user_like.add(request.user)
                return HttpResponse("1")
            else:
                video.user_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")
