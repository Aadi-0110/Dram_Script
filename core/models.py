from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" + str(self.created_at)


class UploadScript(models.Model):
    title = models.CharField(max_length=512, unique=True)
    created_by = models.ForeignKey(User, on_delete=None, related_name="scripts")
    created_at = models.DateTimeField(auto_now_add=True)
    script_file = models.FileField(upload_to='script_files/%Y/%m/%d/', null=False, blank=False)

    def __str__(self):
        return self.title


class Script(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )

    index = models.CharField(max_length=512, default=None, null=True, blank=True)
    character_name = models.CharField(max_length=512, null=False, blank=False)
    dialogue = models.TextField(max_length=4096)
    script = models.ForeignKey(UploadScript, on_delete=models.CASCADE, related_name="scripts_name")
    audio = models.FileField(upload_to='audio/%y/%m/%d/', null=True, blank=True)
    character_gender = models.CharField(max_length=255, choices=GENDER, default=GENDER[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=128)

    def __str__(self):
        return self.script.title + "- index -" + str(self.id)

    class Meta:
        ordering = ['created_at']


class Character(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )

    character_name = models.CharField(max_length=512)
    script = models.ForeignKey(UploadScript, on_delete=models.CASCADE, related_name="characters")
    created_at = models.DateTimeField(auto_now_add=True)
    character_gender = models.CharField(max_length=255, choices=GENDER, default=GENDER[0][0])

    def __str__(self):
        return self.character_name

    class Meta:
        ordering = ['script']


class TrainedModel(models.Model):
    model_name = models.CharField(max_length=128)
    word2id = models.FileField(upload_to='trained_model/')
    id2label = models.FileField(upload_to='trained_model/')
    label2id = models.FileField(upload_to='trained_model/')
    model_with_attentions = models.FileField(upload_to='trained_model/')

    def __str__(self):
        return self.model_name
