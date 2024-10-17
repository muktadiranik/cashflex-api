import graphene
from cashflex.api.schema import Query
from cashflex.api.schema import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
