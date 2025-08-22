# posts/models.py
from django.conf import settings   # AUTH_USER_MODEL ni ishlatish uchun
from django.db import models       # Django ORM

class Post(models.Model):
    title = models.CharField(max_length=50)   # Post sarlavhasi (maks. 50 belgidan iborat)
    body = models.TextField()                 # Post matni
    author = models.ForeignKey(               # Muallif (CustomUser bilan bog‘lanadi)
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Avtomatik yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)      # Avtomatik yangilangan vaqt

    def __str__(self):
        return self.title   # Admin panelda post nomi sifatida ko‘rinadi
