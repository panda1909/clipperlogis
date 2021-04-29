from django.shortcuts import render
from core.models import Messages, Quote


# Create your views here.
def index(request):
    if request.method == 'POST':
        var = request.POST
        name = var['name']
        email = var['email']
        phone = var['phone']
        move = var['type']
        take = var['take']
        deliver = var['deliver']
        des = var['desc']

        quote = Quote.objects.create(Name=name, Email=email, Phone=phone, Type=move, Take=take, Deliver=deliver,
                                     Description=des)
    return render(request, 'core/index.html')


def contact(request):
    if request.method == 'POST':
        var = request.POST
        name = var['name']
        email = var['email']
        phone = var['phone']
        message = var['message']

        messages = Messages.objects.create(Name=name, Email=email, Phone=phone, Message=message)

    return render(request, 'core/contact.html')
