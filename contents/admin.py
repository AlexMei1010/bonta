from django.contrib import admin
from django.db import models

# Register your models here.
from photos.models import Post

admin.site.register(Post)
