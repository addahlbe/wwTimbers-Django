from django.shortcuts import render
# from django.http import (
#     HttpResponse,
#     Http404
# )
from models import Image
# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def history(request):
    return render(request, 'history.html')


def decking(request):
    return render(request, 'decking.html')


def timbers(request):
    return render(request, 'timbers.html')


def outdoor(request):
    return render(request, 'outdoor.html')


def crane(request):
    return render(request, 'crane.html')


def repair(request):
    return render(request, 'repair.html')


# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject please. . .')
#         if not request.POST.get('messasage', ''):
#             errors.append('Enter a message please. . .')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid formatted e-mail address. . .')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POSt['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request, 'contact_form.html', {'errors': errors})
