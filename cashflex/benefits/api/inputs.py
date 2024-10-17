import graphene


class CreateOrUpdateBenefitInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    is_active = graphene.Boolean()


class CreateOrUpdateBenefitPriceInput(graphene.InputObjectType):
    id = graphene.ID()
    group_id = graphene.ID()
    benefit_id = graphene.ID()
    amount = graphene.Float()
    sub_total = graphene.Float()
    total_amount = graphene.Float()
