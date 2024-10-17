import graphene
from graphene_django.filter import DjangoFilterConnectionField
from cashflex.collaborators.api.schema import UserObjectType
from cashflex.users.api.schema import *
from django.contrib.auth import get_user_model
User = get_user_model()


class AuthQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserObjectType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


user_schema_query = graphene.Schema(query=AuthQuery)
