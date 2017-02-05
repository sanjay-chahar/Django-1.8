from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Host

from .models import Apps

from .models  import Musician

from .models import Album

admin.site.register(Host)
admin.site.register(Apps)
admin.site.register(Musician)
admin.site.register(Album)
