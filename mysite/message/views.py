from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView

# class MessageView(TemplateView):
#     template_name = 'message/message.html'

from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def send_message(request):

    if request.method == 'POST':
        content = request.POST.get('content')
        recipient_id = request.POST.get('recipient')
        if content and recipient_id:
            recipient = User.objects.get(id=recipient_id)
            message = Message(user=request.user, content=content, recipient=recipient)
            message.save()

    users = User.objects.all()
    messages = Message.objects.filter(user=request.user) | Message.objects.filter(recipient=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'message/message.html', {'users': users,'messages': messages})

def chat_detail(request, recipient_username):
    recipient = User.objects.get(username=recipient_username)

    if request.method == 'POST':
        content = request.POST.get('content')
        
        if content:
            
            message = Message(user=request.user, content=content, recipient=recipient)
            message.save()
    
    
    users = User.objects.all()
    messages = Message.objects.filter(user=request.user, recipient=recipient) | Message.objects.filter(user=recipient, recipient=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'message/chat_detail.html', {'recipient': recipient, 'messages': messages, 'users': users})




# @login_required
# def send_message_Ivan(request):

#     if request.method == 'POST':
#         content = request.POST.get('content')
#         recipient_id = request.POST.get('recipient')
#         if content and recipient_id:
#             recipient = User.objects.get(id=recipient_id)
#             message = Message(user=request.user, content=content, recipient=recipient)
#             message.save()
    
#     messages = Message.objects.filter(user=request.user)
#     messages_Ivan = Message.objects.filter(user='Ivan')
#     messages= messages + messages_Ivan
#     return render(request, 'message/message.html', {'messages': messages})

# def message_view(request):
#     return HttpResponse("Hello, this is the message app!")
#     print(request)