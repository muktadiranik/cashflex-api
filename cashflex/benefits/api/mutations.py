import graphene
from django.contrib.auth.models import Group
from cashflex.benefits.models import *
from cashflex.benefits.api.schema import *
from cashflex.benefits.api.inputs import *


class CreateOrUpdateBenefit(graphene.Mutation):
    benefit = graphene.Field(BenefitObjectType)

    class Arguments:
        input = CreateOrUpdateBenefitInput()

    def mutate(self, info, input):
        if input.id:
            benefit = Benefit.objects.get(id=input.id)
            if benefit:
                if input.name:
                    benefit.name = input.name
                if input.description:
                    benefit.description = input.description
                if input.is_active:
                    benefit.is_active = input.is_active
                benefit.save()
                return CreateOrUpdateBenefit(benefit=benefit)
        benefit = Benefit.objects.create(name=input.name, description=input.description, is_active=input.is_active)
        return CreateOrUpdateBenefit(benefit=benefit)


class DeleteBenefit(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        benefit = Benefit.objects.get(id=id)
        if benefit:
            benefit.delete()
        return DeleteBenefit(success=True)


class CreateOrUpdateBenefitPrice(graphene.Mutation):
    benefit_price = graphene.Field(BenefitPriceObjectType)

    class Arguments:
        input = CreateOrUpdateBenefitPriceInput()

    def mutate(self, info, input):
        if input.id:
            benefit_price = BenefitPrice.objects.get(id=input.id)
            if benefit_price:
                if input.group_id:
                    benefit_price.group = Group.objects.get(id=input.group_id)
                if input.benefit_id:
                    benefit_price.benefit = Benefit.objects.get(id=input.benefit_id)
                if input.amount:
                    benefit_price.amount = input.amount
                if input.sub_total:
                    benefit_price.sub_total = input.sub_total
                if input.total_amount:
                    benefit_price.total_amount = input.total_amount
                benefit_price.save()
                return CreateOrUpdateBenefitPrice(benefit_price=benefit_price)
        benefit_price = BenefitPrice.objects.create(group=Group.objects.get(id=input.group_id),
                                                    benefit=Benefit.objects.get(id=input.benefit_id),
                                                    amount=input.amount,
                                                    sub_total=input.sub_total,
                                                    total_amount=input.total_amount)
        return CreateOrUpdateBenefitPrice(benefit_price=benefit_price)


class DeleteBenefitPrice(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        benefit_price = BenefitPrice.objects.get(id=id)
        if benefit_price:
            benefit_price.delete()
        return DeleteBenefitPrice(success=True)


class BenefitMutation(graphene.ObjectType):
    create_or_update_benefit = CreateOrUpdateBenefit.Field()
    delete_benefit = DeleteBenefit.Field()
    create_or_update_benefit_price = CreateOrUpdateBenefitPrice.Field()
    delete_benefit_price = DeleteBenefitPrice.Field()
