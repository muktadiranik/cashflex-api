import graphene
from graphene_file_upload.scalars import Upload


class CreateOrUpdateUserInput(graphene.InputObjectType):
    id = graphene.ID()
    uuid = graphene.UUID()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()


class CreateOrUpdateCollaboratorAccountInput(graphene.InputObjectType):
    id = graphene.ID()
    collaborator_id = graphene.ID()
    budget_balance = graphene.Float()
    cost_balance = graphene.Float()
    cash_balance = graphene.Float()
    withdraw = graphene.Float()
    donation = graphene.Date()


class CreateOrUpdateCollaboratorPaymentInput(graphene.InputObjectType):
    id = graphene.ID()
    collaborator_id = graphene.ID()
    qr_code = Upload()


class CreateOrUpdateCollaboratorPaymentDetailsInput(graphene.InputObjectType):
    id = graphene.ID()
    collaborator_payment_id = graphene.ID()
