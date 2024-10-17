import graphene


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    uuid = graphene.UUID()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    cpf = graphene.String()
    dob = graphene.Date()
    phone = graphene.String()
    department = graphene.ID()
    position = graphene.ID()
    gender = graphene.ID()
    role = graphene.ID()


class DepartmentInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class PositionInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class GenderInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class RoleInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class GroupInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    permissions = graphene.List(graphene.ID)
