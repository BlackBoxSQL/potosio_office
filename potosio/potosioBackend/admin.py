from django.contrib import admin

# Register your models here.
from users.models import CustomUser
from . models import Skill, ClientProfile, ProfilePhoto, ShowcasePhoto, PhotographerProfile, PhotographerType, PhotographyType, Camera, CameraBrand, CameraType, Address
admin.site.register(Skill)
admin.site.register(ClientProfile)
admin.site.register(ProfilePhoto)
admin.site.register(ShowcasePhoto)
admin.site.register(Address)
admin.site.register(PhotographyType)
admin.site.register(PhotographerProfile)
admin.site.register(PhotographerType)
admin.site.register(CameraType)
admin.site.register(Camera)
admin.site.register(CameraBrand)
admin.site.register(CustomUser)
