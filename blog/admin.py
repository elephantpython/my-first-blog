from django.contrib import admin

# Register your models here.
## the followng two lines were added following the girls tutorial
from .models import Post

admin.site.register(Post)