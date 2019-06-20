import graphene
from .models import Track
from graphene_django import DjangoObjectType

class TrackType(DjangoObjectType):
    class Meta:
        model = Track
    
class Query(graphene.ObjectType):
    tracks = graphene.List(Track)

    def resolve_tracks(self, info):
        return Track.objects.all()

