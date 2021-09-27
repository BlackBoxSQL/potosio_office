import graphene
from graphene_django import DjangoObjectType

from potosioBackend.models import Camera, CameraBrand, CameraType, ProfilePhoto, ClientProfile, PersonalInformation, PhotographerProfile, PhotographerType, PhotographyType, Address, SecurityInformation, ShowcasePhoto, GPSLocation, Skill

class Camera(DjangoObjectType):
    class Meta:
        model = Camera

class Query(graphene.ObjectType):
    cameras = graphene.List(Camera)
    camera = graphene.Field(Camera, camera_id=graphene.Int(required=True))

    def resolve_cameras(self, info, **kwargs):
    # Querying a list
        return Camera.objects.all()

    def resolve_camera(self, info, camera_id):
    # Querying a single question
        return Camera.objects.get(pk=camera_id)

schema = graphene.Schema(query=Query)