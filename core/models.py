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
    title = models.CharField(max_length=512)
    created_by = models.ForeignKey(User, on_delete=None, related_name="scripts")
    created_at = models.DateTimeField(auto_now_add=True)
    script_file = models.FileField(upload_to='script_files/%Y/%m/%d/', null=False, blank=False)

    def __str__(self):
        return self.title


class Script(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    index = models.CharField(max_length=512)
    character_name = models.CharField(max_length=512, null=False, blank=False)
    dialogue = models.TextField(max_length=4096)
    script = models.ForeignKey(UploadScript, on_delete=models.CASCADE, related_name="scripts_name")
    audio = models.FileField(upload_to='audio/%y/%m/%d/', null=True, blank=True)
    character_gender = models.CharField(max_length=255, choices=GENDER, default=GENDER[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.script.title + "- index -" + str(self.index)

    class Meta:
        ordering = ['created_at']
