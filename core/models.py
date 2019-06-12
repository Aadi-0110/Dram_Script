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
