import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()
    is_wack = graphene.Boolean()
    users = graphene.List(User, limit=graphene.Int())

    def resolve_hello(self, info):
        return "world"
    
    def resolve_is_admin(self, info):
        return True

    def resolve_is_wack(self, info):
        return False

    def resolve_users(self, info, limit=None):
        return [
            User(id="1", username="Mark", created_at=datetime.now()),
            User(id="2", username="Josh", created_at=datetime.now())

        ][:limit]
schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        users(limit: 1) {
            id,
            username
        }
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))