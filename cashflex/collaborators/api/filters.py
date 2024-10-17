from django_filters import *
from django.contrib.auth import get_user_model
User = get_user_model()


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['exact'],
            'email': ['exact'],
            'uuid': ['exact'],
        }
