import graphene
from graphene_file_upload.scalars import Upload




class PartnerInput(graphene.InputObjectType):
    name = graphene.String()
    slug = graphene.String()
    discription = graphene.String()
    website = graphene.String()
    image = Upload()
    is_active = graphene.Boolean()


class UpdatePartnerInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    slug = graphene.String()
    discription = graphene.String()
    website = graphene.String()
    image= Upload()
    is_active = graphene.Boolean()


class FAQCategoryInput(graphene.InputObjectType):
    name = graphene.String()
    slug = graphene.String()


class UpdateFAQCategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    slug = graphene.String()


class FAQInput(graphene.InputObjectType):
    category = graphene.ID()
    question = graphene.String()
    slug = graphene.String()
    answer = graphene.String()
    is_active = graphene.Boolean()


class UpdateFAQInput(graphene.InputObjectType):
    id = graphene.ID()
    category = graphene.ID()
    question = graphene.String()
    slug = graphene.String()
    answer = graphene.String()
    is_active = graphene.Boolean()


class TrainingTypeInput(graphene.InputObjectType):
    name = graphene.String()
    slug = graphene.String()


class UpdateTrainingTypeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    slug = graphene.String()


class TrainingInput(graphene.InputObjectType):
    type = graphene.ID()
    title = graphene.String()
    slug = graphene.String()
    description = graphene.String()
    video = graphene.String()
    is_active = graphene.Boolean()


class UpdateTrainingInput(graphene.InputObjectType):
    id = graphene.ID()
    type = graphene.ID()
    title = graphene.String()
    slug = graphene.String()
    description = graphene.String()
    video = graphene.String()
    is_active = graphene.Boolean()


class ContactInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    message = graphene.String()

class SocialMediaInput(graphene.InputObjectType):
    platform = graphene.String()
    url = graphene.String()
    icon = graphene.String()


class UpdateSocialMediaInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    platform = graphene.String()
    url = graphene.String()
    icon = graphene.String()

