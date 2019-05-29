import graphene
import json

class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()
    is_wack = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"
    
    def resolve_is_admin(self, info):
        return True

    def resolve_is_wack(self, info):
        return False

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        isWack
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))