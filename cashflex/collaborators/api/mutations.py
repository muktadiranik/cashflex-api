import graphene
import graphql_jwt
from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql import GraphQLError
from cashflex.users.api.inputs import *
from cashflex.users.api.schema import *
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateOrUpdateUser(graphene.Mutation):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        input = UserInput()

    def mutate(self, info, input):
        try:
            user = User.objects.get(uuid=input.uuid)
            if user:
                if input.email:
                    return GraphQLError("Email cannot be changed")
                if input.username:
                    if user.username:
                        return GraphQLError("Username cannot be changed")
                    user.username = input.username
                if input.first_name:
                    user.first_name = input.first_name
                if input.last_name:
                    user.last_name = input.last_name
                if input.password:
                    user.set_password(input.password)
                user.save()
                token = get_token(user)
                refresh_token = create_refresh_token(user)
                return CreateOrUpdateUser(user=user, token=token, refresh_token=refresh_token)
        except User.DoesNotExist:
            if User.objects.filter(email=input.email).exists():
                return GraphQLError("Email already exists")
            user = User.objects.create(email=input.email)
        user.set_password(input.password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateOrUpdateUser(user=user, token=token, refresh_token=refresh_token)


class AuthMutation(graphene.ObjectType):
    create_or_update_user = CreateOrUpdateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()


user_schema_mutation = graphene.Schema(mutation=AuthMutation)
