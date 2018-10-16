from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CommentForm
from .models import Comment
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='/account/login')
@csrf_exempt
@require_POST
def upload_comment(request):
    new_comment = Comment.objects.create(user_id=request.user.id,body=request.POST['body'],video_id=request.POST['video_id'])
    return HttpResponse("1")



