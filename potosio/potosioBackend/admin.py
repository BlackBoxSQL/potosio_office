from django.contrib import admin

# Register your models here.
from . models import Skill, ClientProfile, GPSLocation, ProfilePhoto,ShowcasePhoto, PhotographerProfile, PhotographerType, PhotographyType, Camera, CameraBrand, CameraType, Address
admin.site.register(Skill)
admin.site.register(ClientProfile)
admin.site.register(GPSLocation)
admin.site.register(ProfilePhoto)
admin.site.register(ShowcasePhoto)
admin.site.register(Address)
admin.site.register(PhotographyType)
admin.site.register(PhotographerProfile)
admin.site.register(PhotographerType)
admin.site.register(CameraType)
admin.site.register(Camera)
admin.site.register(CameraBrand)