from time import sleep

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import re
import os
from urllib.parse import urlparse

# Create your views here.
from core.forms import SignUpForm, ContactUsForm, UploadScriptForm, CharacterForm, GenderForm, TrainedModelForm
from core.models import UploadScript, Script, Character
import pickle

from django.shortcuts import get_object_or_404
from keras_preprocessing.sequence import pad_sequences as enc
import keras
import re
import uuid

#loading pickle files
from core.models import TrainedModel

obj = get_object_or_404(TrainedModel, pk=1)
wid = open(obj.word2id.path, 'rb')
word2id = pickle.load(wid)
idl = open(obj.id2label.path, 'rb')
id2label = pickle.load(idl)
lid = open(obj.label2id.path, 'rb')
label2id = pickle.load(lid)
mwa = open(obj.model_with_attentions.path, 'rb')
model_with_attentions = pickle.load(mwa)
max_words = 178
wid.close()
idl.close()
lid.close()
mwa.close()


def new_predict(sample_text):
    # Encode samples
    tokenized_sample = sample_text.split()
    # if len(tokenized_sample) <= 6:
    #     return 'happy'

    # Make predictions
    try:
        encoded_samples = [[word2id[word] for word in tokenized_sample]]

        # Padding
        encoded_samples = enc(encoded_samples, maxlen=max_words)
        label_probs, attentions = model_with_attentions.predict(encoded_samples)
        label_probs_id = {id2label[_id]: prob for (label, _id), prob in zip(label2id.items(),label_probs[0])}
    except:
        return 'neutral'
    return max(label_probs_id, key=label_probs_id.get)


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
    l = {'male':[], 'female':[]}
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
            index, gender, character_name, dia = [re.sub(r'\"|\n|\\', '', j) for j in i.split('" ')]
            try:
                l[gender].append(character_name)
            except:
                pass
            je = re.sub('[^\w\s]', '', dia.lower())
            sentiment = new_predict(je)
            # sentiment = 'happy'
            Script(index=index, sentiment=sentiment, character_gender=gender, character_name=character_name, dialogue=dia, script=obj).save()
        except IndexError:
            pass
    datas.close()
    for z in l.keys():
        l[z] = list(set(l[z]))
    for i in l.keys():
        for j in l[i]:
            try:
                sleep(.1)
                Character(character_name=j, character_gender=i, script=obj).save()
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
    datas = Script.objects.filter(script_id=pk).order_by('created_at').values()
    return JsonResponse(data={'datas': list(datas), 'ch': ch})


@login_required
def set_gender(request, pk):
    if request.method == 'POST':
        form = GenderForm(request.POST)
        # messages.add_message(request, constants.SUCCESS, message="Bad things happening! {}".format(form.is_valid()), )
        if form.is_valid():
            character = form.save(commit=False)
            character.character_gender = form.cleaned_data['character_gender']
            messages.add_message(request, constants.SUCCESS, message="Successfully modified the Character Gender!!", )
            return redirect('start_script', pk, character)  # todo change it
    else:
        form = GenderForm()
    return render(request, 'WhoAreYou.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def set_trained_model(request):
    if request.method == 'POST':
        form = TrainedModelForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.model_name = form.cleaned_data['model_name']
            user.word2id = form.cleaned_data['word2id']
            user.label2id = form.cleaned_data['label2id']
            user.id2label = form.cleaned_data['id2label']
            user.model_with_attentions = form.cleaned_data['model_with_attentions']
            user.save()
            # obj = get_object_or_404(UploadScript, script_file=user.script_file)
            # pk = obj.pk
            messages.add_message(request, constants.SUCCESS, message="Model Uploaded", )
            return redirect('home')  # todo change it
    else:
        form = TrainedModelForm()
    return render(request, 'ScriptUpload.html', {'form': form})


def _sound_func(dia, sentiment, gender):
    pass


@login_required
def set_audio(request, pk):
    datas = Script.objects.filter(script_id=pk).order_by('created_at')

    for data in datas:
        try:
            url = ""
            filename = os.path.basename(urlparse(url).path)
            nm = data.character_name + str(uuid.uuid4())
            data.audio.save(nm, filename, save=True)
        except:
            pass

    messages.add_message(request, constants.SUCCESS, message="Audio Generated", )
    return redirect('home')