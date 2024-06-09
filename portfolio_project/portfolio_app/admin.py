from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

class SessionAdmin(admin.ModelAdmin):
    list_display = ['get_username','expire_date']
    
    def get_username(self, obj):
        
        session_data = obj.get_decoded()
        user_id = session_data.get('_auth_user_id')
        
        if user_id:
        
            try:
                user = User.objects.get(pk=user_id)
                return user.username
        
            except User.DoesNotExist:
                return 'Unknown User'
        
        return 'Anonymous User'

    get_username.short_description = 'Username'

admin.site.register(Session, SessionAdmin)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(UserReview)
admin.site.register(GalleryCategory)
admin.site.register(Category)