from django.contrib import admin
from .models import Post  #post model defined in the previous chapter is imported

admin.site.register(Post) #make model visible on the admin page
#Register the Model