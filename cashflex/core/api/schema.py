import graphene
from graphene_django import DjangoObjectType
from cashflex.core.api.filters import *
from cashflex.core.models import *


class PartnerObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Partner
        fields = "__all__"
        filterset_class = PartnerFilter
        interfaces = (graphene.relay.Node,)

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class FAQCategoryObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = FAQCategory
        fields = "__all__"
        filterset_class = FAQCategoryFilter
        interfaces = (graphene.relay.Node,)


class FAQObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = FAQ
        fields = "__all__"
        filterset_class = FAQFilter
        interfaces = (graphene.relay.Node,)


class TrainingTypeObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = TrainingType
        fields = "__all__"
        filterset_class = TrainingTypeFilter
        interfaces = (graphene.relay.Node,)


class TrainingObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Training
        fields = "__all__"
        filterset_class = TrainingFilter
        interfaces = (graphene.relay.Node,)


class ContactObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Contact
        fields = "__all__"

class SocialMediaObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = SocialMedia
        fields = "__all__"
        filterset_class = SocialMediaFilter
        interfaces = (graphene.relay.Node,)