import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from potosioBackend.models import Camera, CameraBrand, CameraType, ProfilePhoto, ClientProfile, PersonalInformation, PhotographerProfile, PhotographerType, PhotographyType, Address, SecurityInformation, ShowcasePhoto, Skill


class CameraBrandType(DjangoObjectType):
    class Meta:
        model = CameraBrand


class CameraQuery(graphene.ObjectType):
    camerabrand = graphene.List(CameraBrandType)
    camerabrand_by_id = graphene.Field(CameraBrandType, id=graphene.String())

    def resolve_camerabrand(root, info, **kwargs):
        # Querying a list
        return CameraBrand.objects.all()

    def resolve_camerabrand_by_id(root, info, id):
        # Querying a single question
        return CameraBrand.objects.get(pk=id)
