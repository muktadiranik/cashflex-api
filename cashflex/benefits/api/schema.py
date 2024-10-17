import graphene
from graphene_django import DjangoObjectType
from cashflex.benefits.models import Benefit, BenefitPrice
from cashflex.benefits.api.filters import BenefitFilter, BenefitPriceFilter


class BenefitObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Benefit
        fields = "__all__"
        filterset_class = BenefitFilter
        interfaces = (graphene.relay.Node,)


class BenefitPriceObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = BenefitPrice
        fields = "__all__"
        filterset_class = BenefitPriceFilter
        interfaces = (graphene.relay.Node,)
