import graphene
import json
import uuid
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value = datetime.now())
    avatar_url = graphene.String()

    def resolve_avatar_url(self, info):
        return f'http://cloudinary.com/{self.username}/{self.id}'

class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()

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

class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()
    
    def mutate(self, info, username):
        user = User(username = username)
        return CreateUser(user = user)

class CreatePost(graphene.Mutation):
    post = graphene.Field(Post)

    class Arguments:
        title = graphene.String()
        content = graphene.String()
    
    def mutate(self, info, title, content):
        is_anonymous = info.context.get('is_anonymous')
        if (is_anonymous):
            raise Exception('User is not logged in!')

        post = Post(title = title, content = content)
        return CreatePost(post = post)

class Mutation(graphene.ObjectType):
    # This will do the work for creating our class for us, and will have the notation 'Class.Field()'. The class must exist, so we create a CreateUser class above
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)

result = schema.execute(
    '''
    query getAllUsers {
        users {
            id
            username
            avatarUrl
        }
    }
    ''',
    # context = { 'is_anonymous': True }
    # variable_values = { 'limit': 1 }
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))