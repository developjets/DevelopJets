from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Team, Contact, Client, Project
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    teamData = Team.objects.all()
    clientData = Client.objects.all()
    index = loader.get_template('index.html')
    context = {
        'teamData' : teamData ,
        'clientData' : clientData
    }
    return HttpResponse(index.render(context, request))

def projects(request):
    projectData = Project.objects.all().order_by('-id')
    projects = loader.get_template('projects.html')
    context = {
        'projectData' : projectData ,
        }
    return HttpResponse(projects.render(context, request))

def projectDetail(request, id):
    projectDetailData = Project.objects.get(id=id)
    projectDetail = loader.get_template('projectDetail.html')
    context = {
        'projectDetailData' : projectDetailData,
    }
    return HttpResponse(projectDetail.render(context, request))
    
def addContactQuerry(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    addContact = Contact(name = name, email = email, subject = subject, message = message)
    addContact.save()
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
    send_mail(subject, message, email, ['help.developjets@gmail.com'])
    return HttpResponseRedirect(reverse('index'))
