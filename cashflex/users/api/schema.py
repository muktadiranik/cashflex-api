import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from cashflex.users.api.filters import UserFilter, DepartmentFilter, PositionFilter, RoleFilter, GenderFilter, GroupFilter, PermissionFilter
from cashflex.users.models import Department, Position, Gender, Role
User = get_user_model()


class UserObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = User
        fields = "__all__"
        filterset_class = UserFilter
        interfaces = (graphene.relay.Node,)


class DepartmentObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Department
        fields = "__all__"
        filterset_class = DepartmentFilter
        interfaces = (graphene.relay.Node,)


class PositionObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Position
        fields = "__all__"
        filterset_class = PositionFilter
        interfaces = (graphene.relay.Node,)


class GenderObjectype(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Gender
        fields = "__all__"
        filterset_class = GenderFilter
        interfaces = (graphene.relay.Node,)


class RoleObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Role
        fields = "__all__"
        filterset_class = RoleFilter
        interfaces = (graphene.relay.Node,)


class GroupObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Group
        fields = "__all__"
        filterset_class = GroupFilter
        interfaces = (graphene.relay.Node,)


class PermissionObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Permission
        fields = "__all__"
        filterset_class = PermissionFilter
        interfaces = (graphene.relay.Node,)
