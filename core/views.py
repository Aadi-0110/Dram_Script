import os
from time import sleep

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import re
from json import dumps

# Create your views here.
from Project.settings import BASE_DIR
from core.forms import SignUpForm, ContactUsForm, UploadScriptForm, CharacterForm
from core.models import UploadScript, Script, Character


@login_required
def home(request):
    # messages.add_message(request, constants.SUCCESS, message="Details Saved Welcome %s %s" % (request.user, request) )
    user1 = get_object_or_404(User, username=request.user)
    script = UploadScript.objects.all()
    return render(request, 'dashboard.html', {'user': user1, 'scripts': script})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user_type = form.cleaned_data['user_type']
            # referral_id = form.cleaned_data['referral_id']
            # UserProfile(user_type=user_type, referral_id=referral_id, user=user).save()
            # print(form.cleaned_data['user_type'], form.cleaned_data['referral_id'], form.cleaned_data['username'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request, constants.SUCCESS, message="Details Saved Welcome %s" % request.user, )
            return redirect('home')  # todo change it
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user_type = form.cleaned_data['user_type']
            # referral_id = form.cleaned_data['referral_id']
            # UserProfile(user_type=user_type, referral_id=referral_id, user=user).save()
            # print(form.cleaned_data['user_type'], form.cleaned_data['referral_id'], form.cleaned_data['username'])
            user.save()
            messages.add_message(request, constants.SUCCESS, message="Your request has been registered, We will get back to you soon", )
            return redirect('home')  # todo change it
    else:
        form = ContactUsForm()
    return render(request, 'contact-us.html', {'form': form})


@login_required
def upload_script(request):
    if request.method == 'POST':
        form = UploadScriptForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.script_file = form.cleaned_data['script_file']
            user.save()
            obj = get_object_or_404(UploadScript, script_file=user.script_file)
            pk = obj.pk
            messages.add_message(request, constants.SUCCESS, message="Script Uploaded", )
            return redirect('generate_script', pk)  # todo change it
    else:
        form = UploadScriptForm()
    return render(request, 'ScriptUpload.html', {'form': form})


@login_required
def generate_script(request, pk):
    l = []
    # if Script.objects.filter(script_id=pk):
    #     # render(request, 'loader.html')
    #     sleep(5)
    #     messages.add_message(request, constants.SUCCESS,
    #                          message="Scripts already generated!!", )
    #     return redirect('home')
    obj = get_object_or_404(UploadScript, pk=pk)
    datas = open(obj.script_file.path)
    # render(request, 'loader.html')
    for i in datas.readlines():
        try:
            index, character_name, dia = [re.sub(r'\"|\n|\\', '', j) for j in i.split('" ')]
            l.append(character_name)
            Script(index=index, character_name=character_name, dialogue=dia, script=obj).save()
        except:
            pass
    datas.close()
    l = list(set(l))
    for i in l:
        try:
            sleep(.1)
            Character(character_name=i, script=obj).save()
        except:
            pass
    return redirect('home')


@login_required
def view_all_scripts(request, pk):
    datas = Script.objects.filter(script_id=pk)
    return render(request, 'new_view_all_script.html', {'datas': datas})


def about_us(request):
    return render(request, 'about-us.html')


@login_required
def who_are_you(request, pk):
    if request.method == 'POST':
        form = CharacterForm(request.POST, pkm=pk)
        # messages.add_message(request, constants.SUCCESS, message="Bad things happening! {}".format(form.is_valid()), )
        if form.is_valid():
            character = form.cleaned_data['select_your_character']
            messages.add_message(request, constants.SUCCESS, message="Successfully Selected the Character!!", )
            return redirect('start_script', pk, character)  # todo change it
    else:
        form = CharacterForm(pkm=pk)
    return render(request, 'WhoAreYou.html', {'form': form})


@login_required
def start_script(request, pk, ch):
    datas = Script.objects.filter(script_id=pk)
    return render(request, 'start_script.html', {'datas': datas, 'ch': ch})


def send_script_data(request, pk, ch):
    datas = Script.objects.filter(script_id=pk).values()
    return JsonResponse(data={'datas': list(datas), 'ch': ch})
