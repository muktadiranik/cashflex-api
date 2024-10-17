import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .schema import UserObjectType
from cashflex.users.api.schema import *
User = get_user_model()


class AuthQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserObjectType)
    departments = DjangoFilterConnectionField(DepartmentObjectType)
    positions = DjangoFilterConnectionField(PositionObjectType)
    roles = DjangoFilterConnectionField(RoleObjectType)
    genders = DjangoFilterConnectionField(GenderObjectype)
    groups = DjangoFilterConnectionField(GroupObjectType)
    permissions = DjangoFilterConnectionField(PermissionObjectType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()

    def resolve_positions(self, info, **kwargs):
        return Position.objects.all()

    def resolve_roles(self, info, **kwargs):
        return Role.objects.all()

    def resolve_genders(self, info, **kwargs):
        return Gender.objects.all()

    def resolve_groups(self, info, **kwargs):
        return Group.objects.prefetch_related("permissions").all()

    def resolve_permissions(self, info, **kwargs):
        return Permission.objects.all()


user_schema_query = graphene.Schema(query=AuthQuery)
