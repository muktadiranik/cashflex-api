import graphene
from graphene_django import DjangoObjectType
from cashflex.users.api.filters import UserFilter
from django.contrib.auth import get_user_model
User = get_user_model()


class UserObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = User
        fields = "__all__"
        filterset_class = UserFilter
        interfaces = (graphene.relay.Node,)
