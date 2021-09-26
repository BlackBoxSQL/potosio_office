import graphene
from graphene_django import DjangoObjectType

from potosioBackend.models import Camera, CameraBrand, CameraType, ProfilePhoto, ClientProfile, PersonalInformation, PhotographerProfile, PhotographerType, PhotographyType, Address, SecurityInformation, ShowcasePhoto, GPSLocation, Skill

class Camera(DjangoObjectType):
    class Meta:
        model = Camera

class Query:
    attrs = graphene.List(Camera)
    attr = graphene.Field(Camera, attr_id=graphene.Int(required=True))

    def resolve_attrs(self, info, **kwargs):
    # Querying a list
        return Camera.objects.all()

    def resolve_attr(self, info, attr_id):
    # Querying a single question
        return Camera.objects.get(pk=attr_id)

schema = graphene.Schema(query=Query)