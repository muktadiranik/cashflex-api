import graphene
from graphene_django.filter import DjangoFilterConnectionField
from cashflex.benefits.api.schema import *
from cashflex.benefits.models import Benefit


class BenefitQuery(graphene.ObjectType):
    benefits = DjangoFilterConnectionField(BenefitObjectType)
    benefit_prices = DjangoFilterConnectionField(BenefitPriceObjectType)

    def resolve_benefits(self, info, **kwargs):
        return Benefit.objects.all()

    def resolve_benefit_prices(self, info, **kwargs):
        return BenefitPrice.objects.all()


benefit_schema_query = graphene.Schema(query=BenefitQuery)
