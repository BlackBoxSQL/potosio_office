import graphene
from graphene_django import DjangoObjectType
from graphene_django.types import DjangoObjectType

from potosioBackend.models import (Address, Camera, CameraBrand, CameraType,
                                   ClientProfile, PersonalInformation,
                                   PhotographerProfile, PhotographerType,
                                   PhotographyType,
                                   SecurityInformation, Skill)


class CameraBrandType(DjangoObjectType):
    class Meta:
        model = CameraBrand


class CameraTypeType(DjangoObjectType):
    class Meta:
        model = Camera


class CameraTypeQuery(graphene.ObjectType):
    cameras = graphene.List(CameraTypeType)
    camera_by_brand_name = graphene.List(
        CameraBrandType, name=graphene.String())

    def resolve_cameras(self, info, **kwargs):
        return Camera.objects.all()

    def resolve_camera_by_brand_name(root, info, name):
        # Querying a single question
        return Camera.objects.all().filter(brand=name)


class CameraBrandQuery(graphene.ObjectType):
    camerabrand = graphene.List(CameraBrandType)
    camerabrand_by_id = graphene.Field(CameraBrandType, id=graphene.String())
    camerabrand_by_name = graphene.List(
        CameraBrandType, name=graphene.String())
    total_brand = graphene.Int()

    def resolve_camerabrand(root, info, **kwargs):
        # Querying a list
        return CameraBrand.objects.all()

    def resolve_camerabrand_by_id(root, info, id):
        # Querying a single question
        return CameraBrand.objects.get(pk=id)

    def resolve_camerabrand_by_name(root, info, name):
        # Querying a single question
        return CameraBrand.objects.all().filter(brand=name)

    def resolve_total_brand(root, info):
        return CameraBrand.objects.count()
