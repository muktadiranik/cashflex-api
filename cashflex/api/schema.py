import graphene
from cashflex.users.api.mutations import AuthMutation
from cashflex.users.api.queries import AuthQuery
from cashflex.core.api.queries import CoreQuery
from cashflex.core.api.mutations import CoreMutation
from cashflex.benefits.api.queries import BenefitQuery
from cashflex.benefits.api.mutations import BenefitMutation


class Query(
        AuthQuery,
        CoreQuery,
        BenefitQuery,
        graphene.ObjectType
):
    pass


class Mutation(
    AuthMutation,
    CoreMutation,
    BenefitMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
