from cashflex.users.tasks import *
import string
import pandas as pd
import random
import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql import GraphQLError
import environ
from cashflex.users.api.inputs import *
from cashflex.users.api.schema import *
from cashflex.users.models import Role, Gender, Position, Department
from graphene_file_upload.scalars import Upload
User = get_user_model()
env = environ.Env()


# Collaborators File Upload Mutation
class CreateUserWithFile(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, file):
        file_extension = file.name.split(".")[-1].lower()
        if file_extension == "xlsx" or file_extension == "xls":
            df = pd.read_excel(file)
        elif file_extension == "csv":
            df = pd.read_csv(file)
        else:
            return CreateUserWithFile(success=False, message="Invalid file type. Only xlsx, xls, and csv files are supported.")
        user_list = [
            User(
                email=row["email"],
                cpf=row["cpf"],
                first_name=row["first_name"],
                last_name=row["last_name"],
            )
            for _, row in df.iterrows()
        ]
        User.objects.bulk_create(user_list)
        return CreateUserWithFile(success=True, message="Collaborators created successfully")


class CreateOrUpdateDepartment(graphene.Mutation):
    department = graphene.Field(DepartmentObjectType)

    class Arguments:
        input = DepartmentInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                department = Department.objects.get(id=input.id)
                if department:
                    if input.name:
                        department.name = input.name
                    if input.description:
                        department.description = input.description
                    department.save()
                    return CreateOrUpdateDepartment(department=department)
            except Department.DoesNotExist:
                return GraphQLError("Department does not exist")
        else:
            department = Department.objects.create(
                name=input.name,
                description=input.description
            )
            return CreateOrUpdateDepartment(department=department)


class DeleteDepartment(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = DepartmentInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                department = Department.objects.get(id=input.id)
                if department:
                    department.delete()
                    return DeleteDepartment(success=True)
            except Department.DoesNotExist:
                return GraphQLError("Department does not exist")


class CreateOrUpdateRole(graphene.Mutation):
    role = graphene.Field(RoleObjectType)

    class Arguments:
        input = RoleInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                role = Role.objects.get(id=input.id)
                if role:
                    if input.name:
                        role.name = input.name
                    if input.description:
                        role.description = input.description
                    role.save()
                    return CreateOrUpdateRole(role=role)
            except Role.DoesNotExist:
                return GraphQLError("Role does not exist")
        else:
            role = Role.objects.create(
                name=input.name,
                description=input.description
            )
            return CreateOrUpdateRole(role=role)


class DeleteRole(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = RoleInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                role = Role.objects.get(id=input.id)
                if role:
                    role.delete()
                    return DeleteRole(success=True)
            except Role.DoesNotExist:
                return GraphQLError("Role does not exist")


class CreateOrUpdateGender(graphene.Mutation):
    gender = graphene.Field(GenderObjectype)

    class Arguments:
        input = GenderInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                gender = Gender.objects.get(id=input.id)
                if gender:
                    if input.name:
                        gender.name = input.name
                    gender.save()
                    return CreateOrUpdateGender(gender=gender)
            except Gender.DoesNotExist:
                return GraphQLError("Gender does not exist")
        else:
            gender = Gender.objects.create(
                name=input.name,
            )
            return CreateOrUpdateGender(gender=gender)


class DeleteGender(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = GenderInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                gender = Gender.objects.get(id=input.id)
                if gender:
                    gender.delete()
                    return DeleteGender(success=True)
            except Gender.DoesNotExist:
                return GraphQLError("Gender does not exist")


class CreateOrUpdateUser(graphene.Mutation):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        input = UserInput()

    def mutate(self, info, input):
        try:
            user = None
            if input.uuid:
                user = User.objects.get(uuid=input.uuid)
            if input.email:
                user = User.objects.get(email=input.email)
            if input.id:
                user = User.objects.get(username=input.id)
            if input.cpf:
                user = User.objects.get(cpf=input.cpf)
            if user:
                if input.first_name:
                    user.first_name = input.first_name
                if input.last_name:
                    user.last_name = input.last_name
                if input.password:
                    user.set_password(input.password)
                if input.cpf:
                    user.cpf = input.cpf
                if input.dob:
                    user.dob = input.dob
                if input.phone:
                    user.phone = input.phone
                if input.department:
                    user.department = Department.objects.get(id=input.department)
                if input.position:
                    user.position = Position.objects.get(id=input.position)
                if input.role:
                    user.role = Role.objects.get(id=input.role)
                if input.gender:
                    user.gender = Gender.objects.get(id=input.gender)
                user.save()
                token = get_token(user)
                refresh_token = create_refresh_token(user)
                return CreateOrUpdateUser(user=user, token=token, refresh_token=refresh_token)
        except User.DoesNotExist:
            if User.objects.filter(email=input.email).exists():
                return GraphQLError("Email already exists")
            user = User.objects.create(email=input.email)
        user.set_password(input.password)
        if input.first_name:
            user.first_name = input.first_name
        if input.last_name:
            user.last_name = input.last_name
        if input.password:
            user.set_password(input.password)
        if input.cpf:
            user.cpf = input.cpf
        if input.dob:
            user.dob = input.dob
        if input.phone:
            user.phone = input.phone
        if input.department:
            user.department = Department.objects.get(id=input.department)
        if input.position:
            user.position = Position.objects.get(id=input.position)
        if input.role:
            user.role = Role.objects.get(id=input.role)
        if input.gender:
            user.gender = Gender.objects.get(id=input.gender)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateOrUpdateUser(user=user, token=token, refresh_token=refresh_token)


class DeleteUser(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = UserInput()

    def mutate(self, info, input):
        if input.uuid is not None:
            try:
                user = User.objects.get(uuid=input.uuid)
                if user:
                    user.delete()
                    return DeleteUser(success=True)
            except User.DoesNotExist:
                return GraphQLError("User does not exist")
        if input.id is not None:
            try:
                user = User.objects.get(id=input.id)
                if user:
                    user.delete()
                    return DeleteUser(success=True)
            except User.DoesNotExist:
                return GraphQLError("User does not exist")


class ChangePasswordMutation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        user_id = graphene.ID(required=True)
        old_password = graphene.String(required=True)
        new_password1 = graphene.String(required=True)
        new_password2 = graphene.String(required=True)

    @staticmethod
    def mutate(self, info, user_id, old_password, new_password1, new_password2):
        user = User.objects.get(id=user_id)
        if user.check_password(old_password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                return ChangePasswordMutation(success=True)
            else:
                return GraphQLError("Passwords do not match")
        else:
            return GraphQLError("Old password is incorrect")


class SendPasswordResetEmailMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
            send_mail_for_password_reset.delay(email, token, user.first_name)
            user.reset_password_token = token
            user.save()
            return SendPasswordResetEmailMutation(success=True)
        except User.DoesNotExist:
            return GraphQLError("User does not exist")


class ResetPasswordMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        new_password = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, token, new_password):
        try:
            user = User.objects.get(reset_password_token=token)
            user.set_password(new_password)
            user.reset_password_token = None
            user.save()
            return ResetPasswordMutation(success=True)
        except User.DoesNotExist:
            return GraphQLError("User does not exist")


class CreateOrUpdateGroup(graphene.Mutation):
    group = graphene.Field(GroupObjectType)

    class Arguments:
        input = GroupInput()

    def mutate(self, info, input):
        if input.id:
            try:
                group = Group.objects.get(id=input.id)
                if group:
                    if input.name:
                        group.name = input.name
                    group.save()
                    return CreateOrUpdateGroup(group=group)
            except Group.DoesNotExist:
                return GraphQLError("Group does not exist")
        else:
            group = Group.objects.create(name=input.name)
            if input.permissions:
                for permission in input.permissions:
                    group.permissions.add(Permission.objects.get(id=permission))
            return CreateOrUpdateGroup(group=group)


class DeleteGroup(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = GroupInput()

    def mutate(self, info, input):
        if input.id is not None:
            try:
                group = Group.objects.get(id=input.id)
                if group:
                    group.delete()
                    return DeleteGroup(success=True)
            except Group.DoesNotExist:
                return GraphQLError("Group does not exist")


class AuthMutation(graphene.ObjectType):
    create_or_update_department = CreateOrUpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()
    create_or_update_role = CreateOrUpdateRole.Field()
    delete_role = DeleteRole.Field()
    create_or_update_gender = CreateOrUpdateGender.Field()
    delete_gender = DeleteGender.Field()
    create_or_update_user = CreateOrUpdateUser.Field()
    delete_user = DeleteUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()
    change_password = ChangePasswordMutation.Field()
    send_password_reset_email = SendPasswordResetEmailMutation.Field()
    reset_password = ResetPasswordMutation.Field()
    create_user_with_file = CreateUserWithFile.Field()
    create_or_update_group = CreateOrUpdateGroup.Field()
    delete_group = DeleteGroup.Field()


user_schema_mutation = graphene.Schema(mutation=AuthMutation)
