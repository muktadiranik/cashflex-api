import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from cashflex.core.api.schema import *
User = get_user_model()


class CoreQuery(graphene.ObjectType):

    partners = DjangoFilterConnectionField(PartnerObjectType)
    faq_categories = DjangoFilterConnectionField(FAQCategoryObjectType)
    faqs = DjangoFilterConnectionField(FAQObjectType)
    training_types = DjangoFilterConnectionField(TrainingTypeObjectType)
    trainings = DjangoFilterConnectionField(TrainingObjectType)
    contacts = graphene.List(ContactObjectType)
    social_medias = DjangoFilterConnectionField(SocialMediaObjectType)

    def resolve_partners(self, info, **kwargs):
        return Partner.objects.all()

    def resolve_faq_categories(self, info, **kwargs):
        return FAQCategory.objects.prefetch_related('faq_set').all()

    def resolve_faqs(self, info, **kwargs):
        return FAQ.objects.all()

    def resolve_training_types(self, info, **kwargs):
        return TrainingType.objects.prefetch_related('training_set').all()

    def resolve_trainings(self, info, **kwargs):
        return Training.objects.all()

    def resolve_contacts(self, info, **kwargs):
        return Contact.objects.all()

    def resolve_social_medias(self, info, **kwargs):
        return SocialMedia.objects.all()


core_schema_query = graphene.Schema(query=CoreQuery)
