from django_filters import *
from django.contrib.auth.models import Group, Permission
from cashflex.users.models import *


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['exact'],
            'email': ['exact'],
            'uuid': ['exact'],
            'cpf': ['exact'],
            'is_superuser': ['exact'],
        }


class DepartmentFilter(FilterSet):
    class Meta:
        model = Department
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class PositionFilter(FilterSet):
    class Meta:
        model = Position
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class GenderFilter(FilterSet):
    class Meta:
        model = Gender
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class RoleFilter(FilterSet):
    class Meta:
        model = Role
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class GroupFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class PermissionFilter(FilterSet):
    class Meta:
        model = Permission
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }
