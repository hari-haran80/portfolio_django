from .models import UserProfile
from django.contrib.auth import get_user


def custom_context(request):
    user = get_user(request)
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(pro=user)
            image_url = profile.profile.url
        except UserProfile.DoesNotExist:
            image_url = None  
    else:
        image_url = None

    return {'image_url': image_url}

