import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType

from potosioBackend.models import Camera, CameraBrand, CameraType, ProfilePhoto, ClientProfile, PersonalInformation, PhotographerProfile, PhotographerType, PhotographyType, Address, SecurityInformation, ShowcasePhoto, GPSLocation, Skill

class CameraBrandType(DjangoObjectType):
    class Meta:
        model = CameraBrand

class Query(graphene.ObjectType):
    all_camera_brands = graphene.List(CameraBrandType)
    camera_brand = graphene.Field(CameraBrandType, id=graphene.Int(required=True))

    def resolve_all_camera_brands(self, info, **kwargs):
    # Querying a list
        return CameraBrand.objects.all()

    def resolve_camera_brand(self, info, id):
    # Querying a single question
        return CameraBrand.objects.get(pk=id)
        
schema = graphene.Schema(query=Query)