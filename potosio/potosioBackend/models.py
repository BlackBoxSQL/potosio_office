from django import db
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Division(models.Model):
    """Model definition for Division."""

    # TODO: Define fields here
    division = models.CharField(max_length=35)

    class Meta:
        """Meta definition for Division."""
        db_table = 'division'
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        """Unicode representation of Division."""
        return f"{self.division}"

    # TODO: Define custom methods here


class District(models.Model):
    """Model definition for District."""

    # TODO: Define fields here
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.CharField(max_length=35)

    class Meta:
        """Meta definition for District."""
        db_table = 'district'
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        """Unicode representation of District."""
        return f"{self.district}"

    # TODO: Define custom methods here


class Upazila(models.Model):
    """Model definition for PoliceStation."""

    # TODO: Define fields here
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazila = models.CharField(max_length=35)

    class Meta:
        """Meta definition for PoliceStation."""
        db_table = 'upazila'
        verbose_name = 'Upazila'
        verbose_name_plural = 'Upazilas'

    def __str__(self):
        """Unicode representation of PoliceStation."""
        return f"{self.upazila}"

    # TODO: Define custom methods here


class Union(models.Model):
    """Model definition for Union."""

    # TODO: Define fields here
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    union = models.CharField(max_length=35)

    class Meta:
        """Meta definition for Union."""
        db_table = 'union'
        verbose_name = 'Union'
        verbose_name_plural = 'Unions'

    def __str__(self):
        """Unicode representation of Union."""
        return f"{self.union}"

    # TODO: Define custom methods here


class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazila = models.ForeignKey(
        Upazila, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Address."""
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Unicode representation of Address."""
        return f"{self.id}"

    # TODO: Define custom methods here


class SecurityInformation(models.Model):
    """Model definition for SecurityInformation."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    nid = models.CharField(max_length=17)
    nid_side_1 = models.ImageField(upload_to='images/')
    nid_side_2 = models.ImageField(upload_to='images/')
    passport_number = models.CharField(max_length=18)
    birth_certificate = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for SecurityInformation."""
        db_table = 'security_information'
        verbose_name = 'SecurityInformation'
        verbose_name_plural = 'SecurityInformations'
        abstract = True

    def __str__(self):
        """Unicode representation of SecurityInformation."""
        return f"{self.id}"

    # TODO: Define custom methods here


class PersonalInformation(models.Model):
    """Model definition for PersonalInformation."""
    T_SHIRT_SIZE_CHOICES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    # TODO: Define fields here
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    t_shirt_size = models.CharField(
        max_length=5, choices=T_SHIRT_SIZE_CHOICES)
    contact_number = models.CharField(max_length=18)

    class Meta:
        """Meta definition for PersonalInformation."""
        db_table = 'personal_information'
        verbose_name = 'PersonalInformation'
        verbose_name_plural = 'PersonalInformations'
        abstract = True

    def __str__(self):
        """Unicode representation of PersonalInformation."""
        return f"{self.id}"

    # TODO: Define custom methods here


class CameraType(models.Model):
    """Model definition for CameraType."""

    # TODO: Define fields here
    camera_type = models.CharField(max_length=16)

    class Meta:
        """Meta definition for CameraType."""
        db_table = 'camera_type'
        verbose_name = 'CameraType'
        verbose_name_plural = 'CameraType'

    def __str__(self):
        """Unicode representation of CameraType."""
        return f"{self.camera_type}"

   # TODO: Define custom methods here


class PhotographerType(models.Model):
    """Model definition for PhotographerType."""

    # TODO: Define fields here
    photographer_type = models.CharField(max_length=10)

    class Meta:
        """Meta definition for PhotographerType."""
        db_table = 'photographer_type'
        verbose_name = 'PhotographerType'
        verbose_name_plural = 'PhotographerTypes'

    def __str__(self):
        """Unicode representation of PhotographerType."""
        return f"{self.photographer_type}"

   # TODO: Define custom methods here


class PhotographyType(models.Model):

    """Model definition for PhotographyType."""

    # TODO: Define fields here
    photography_type = models.CharField(max_length=15)

    class Meta:
        """Meta definition for PhotographyType."""
        db_table = 'photography_type'
        verbose_name = 'PhotographyType'
        verbose_name_plural = 'PhotographyTypes'

    def __str__(self):
        """Unicode representation of PhotographyType."""
        return f"{self.photography_type}"
    # TODO: Define custom methods here


class CameraBrand(models.Model):
    """Model definition for CameraBrand."""

    # TODO: Define fields here
    brand = models.CharField(max_length=10)

    class Meta:
        """Meta definition for CameraBrand."""
        db_table = 'camera_brand'
        verbose_name = 'CameraBrand'
        verbose_name_plural = 'CameraBrands'

    def __str__(self):
        """Unicode representation of CameraBrand."""
        return f"{self.brand}"

    # TODO: Define custom methods here


class Camera(models.Model):
    """Model definition for Camera."""

    # TODO: Define fields here
    model_name = models.CharField(max_length=50)
    brand = models.ForeignKey(CameraBrand, on_delete=models.CASCADE)
    camera_type = models.ForeignKey(CameraType, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Camera."""
        db_table = 'camera'
        verbose_name = 'Camera'
        verbose_name_plural = 'Cameras'

    def __str__(self):
        """Unicode representation of Camera."""
        return f"{self.camera_name}"

    # TODO: Define custom methods here


class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here

    skill = models.CharField(max_length=12)

    class Meta:
        """Meta definition for Skill."""
        db_table = 'skill'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return f"{self.skill}"

    # TODO: Define custom methods here


class PhotographerProfile(SecurityInformation, PersonalInformation):
    """Model definition for PhotographerProfile."""

    # TODO: Define fields here
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/profilephoto/')
    photographer_type = models.ForeignKey(
        PhotographerType, on_delete=models.CASCADE)
    photography_type = models.ForeignKey(
        PhotographyType, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    charges_per_day = models.IntegerField()
    ph1 = models.ImageField(upload_to='images/')
    ph2 = models.ImageField(upload_to='images/')
    ph3 = models.ImageField(upload_to='images/')
    ph4 = models.ImageField(upload_to='images/')
    ph5 = models.ImageField(upload_to='images/')
    ph6 = models.ImageField(upload_to='images/')
    ph7 = models.ImageField(upload_to='images/')
    ph8 = models.ImageField(upload_to='images/')
    ph9 = models.ImageField(upload_to='images/')
    ph10 = models.ImageField(upload_to='images/')

    class Meta:
        """Meta definition for PhotographerProfile."""
        db_table = 'photographer_profile'
        verbose_name = 'PhotographerProfile'
        verbose_name_plural = 'PhotographerProfiles'

    def __str__(self):
        """Unicode representation of PhotographerProfile."""
        return f"{self.name}"

    # TODO: Define custom methods here


class ClientType(models.Model):
    """Model definition for ClientType."""

    # TODO: Define fields here
    client_type = models.CharField(max_length=20)

    class Meta:
        """Meta definition for ClientType."""
        db_table = 'client_type'
        verbose_name = 'ClientType'
        verbose_name_plural = 'ClientTypes'

    def __str__(self):
        """Unicode representation of ClientType."""
        return f"{self.client_type}"

    # TODO: Define custom methods here


class ClientProfile(SecurityInformation, PersonalInformation):
    """Model definition for ClientProfile."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/')
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for ClientProfile."""
        db_table = 'client_profile'
        verbose_name = 'ClientProfile'
        verbose_name_plural = 'ClientProfiles'

    def __str__(self):
        """Unicode representation of ClientProfile."""
        return f"{self.name}"

    # TODO: Define custom methods here
