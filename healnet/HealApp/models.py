from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[('general', 'General User'), ('patient', 'Patient')],
        default='general'
    )
    patient_name = models.CharField(max_length=150, blank=True)  # extra field
    disease = models.TextField(null=True, blank=True)  # optional field

    def __str__(self):
        return self.username
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="blogs")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title