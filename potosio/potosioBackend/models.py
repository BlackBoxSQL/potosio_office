from django.db import models

# Create your models here.


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
        pass

    def save(self):
        """Save method for CameraType."""
        pass

    def get_absolute_url(self):
        """Return absolute url for CameraType."""
        return ('')
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
        pass

    def save(self):
        """Save method for PhotographerType."""
        pass

    def get_absolute_url(self):
        """Return absolute url for PhotographerType."""
        return ('')
   # TODO: Define custom methods here


class PhotographyType(models.Model):

    """Model definition for PhotographyType."""

    # TODO: Define fields here
    photography_type = models.CharField(max_length=13)

    class Meta:
        """Meta definition for PhotographyType."""
        db_table = 'photography_type'
        verbose_name = 'PhotographyType'
        verbose_name_plural = 'PhotographyTypes'

    def __str__(self):
        """Unicode representation of PhotographyType."""
        pass

    def save(self):
        """Save method for PhotographyType."""
        pass

    def get_absolute_url(self):
        """Return absolute url for PhotographyType."""
        return ('')
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
        pass

    def save(self):
        """Save method for CameraBrand."""
        pass

    def get_absolute_url(self):
        """Return absolute url for CameraBrand."""
        return ('')

    # TODO: Define custom methods here


class Camera(models.Model):
    """Model definition for Camera."""

    # TODO: Define fields here
    brand = models.ForeignKey(CameraBrand, on_delete=models.CASCADE)
    camera_model = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Camera."""
        db_table = 'camera'
        verbose_name = 'Camera'
        verbose_name_plural = 'Cameras'

    def __str__(self):
        """Unicode representation of Camera."""
        pass

    def save(self):
        """Save method for Camera."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Camera."""
        return ('')

    # TODO: Define custom methods here

class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here
    skill = models.CharField(max_length=12)
    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        pass

    def save(self):
        """Save method for Skill."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Skill."""
        return ('')

    # TODO: Define custom methods here


class PhotographerProfile(models.Model):
    """Model definition for PhotographerProfile."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField()
    photographer_type = models.ForeignKey(
        PhotographerType, on_delete=models.CASCADE)
    photography_type = models.ForeignKey(
        PhotographyType, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for PhotographerProfile."""
        db_table = 'photographer_profile'
        verbose_name = 'PhotographerProfile'
        verbose_name_plural = 'PhotographerProfiles'

    def __str__(self):
        """Unicode representation of PhotographerProfile."""
        pass

    def save(self):
        """Save method for PhotographerProfile."""
        pass

    def get_absolute_url(self):
        """Return absolute url for PhotographerProfile."""
        return ('')

    # TODO: Define custom methods here



class ClientProfile(models.Model):
    """Model definition for ClientProfile."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField()
    class Meta:
        """Meta definition for ClientProfile."""
        db_table = 'client_profile'
        verbose_name = 'ClientProfile'
        verbose_name_plural = 'ClientProfiles'

    def __str__(self):
        """Unicode representation of ClientProfile."""
        pass

    def save(self):
        """Save method for ClientProfile."""
        pass

    def get_absolute_url(self):
        """Return absolute url for ClientProfile."""
        return ('')

    # TODO: Define custom methods here


class ProfilePhoto(models.Model):
    """Model definition for ProfilePhoto."""

    # TODO: Define fields here
    profile_imgae = models.ImageField()

    class Meta:
        """Meta definition for ProfilePhoto."""

        db_table = 'profile_photo'
        verbose_name = 'ProfilePhoto'
        verbose_name_plural = 'ProfilePhotos'

    def __str__(self):
        """Unicode representation of ProfilePhoto."""
        pass

    def save(self):
        """Save method for ProfilePhoto."""
        pass

    def get_absolute_url(self):
        """Return absolute url for ProfilePhoto."""
        return ('')

    # TODO: Define custom methods here


class ShowcasePhoto(models.Model):
    """Model definition for ShowcasePhoto."""

    # TODO: Define fields here
    ph1 = models.ImageField()
    ph2 = models.ImageField()
    ph3 = models.ImageField()
    ph4 = models.ImageField()
    ph5 = models.ImageField()
    ph6 = models.ImageField()
    ph7 = models.ImageField()
    ph8 = models.ImageField()
    ph9 = models.ImageField()
    ph10 = models.ImageField()

    class Meta:
        """Meta definition for ShowcasePhoto."""
        db_table = 'showcase_photo'
        verbose_name = 'ShowcasePhoto'
        verbose_name_plural = 'ShowcasePhotos'

    def __str__(self):
        """Unicode representation of ShowcasePhoto."""
        pass

    def save(self):
        """Save method for ShowcasePhoto."""
        pass

    def get_absolute_url(self):
        """Return absolute url for ShowcasePhoto."""
        return ('')

    # TODO: Define custom methods here


class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here
    division = models.CharField(max_length=50)
    district = models.CharField(max_length=50)


    class Meta:
        """Meta definition for Address."""
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Unicode representation of Address."""
        pass

    def save(self):
        """Save method for Address."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Address."""
        return ('')

    # TODO: Define custom methods here


class GPSLocation(models.Model):
    """Model definition for Location."""

    # TODO: Define fields here
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for GPSLocation."""
        db_table = 'gps_location'
        verbose_name = 'GPSLocation'
        verbose_name_plural = 'GPSLocations'

    def __str__(self):
        """Unicode representation of GPSLocation."""
        pass

    def save(self):
        """Save method for GPSLocation."""
        pass

    def get_absolute_url(self):
        """Return absolute url for GPSLocation."""
        return ('')

    # TODO: Define custom methods here


class SecurityInformation(models.Model):
    """Model definition for SecurityInformation."""

    # TODO: Define fields here
    nid = models.CharField(max_length=17)
    nid_side_1 = models.ImageField()
    nid_side_2 = models.ImageField()
    passport_number = models.CharField(max_length=18)
    birth_certificate = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for SecurityInformation."""
        db_table = 'security_information'
        verbose_name = 'SecurityInformation'
        verbose_name_plural = 'SecurityInformations'

    def __str__(self):
        """Unicode representation of SecurityInformation."""
        pass

    def save(self):
        """Save method for SecurityInformation."""
        pass

    def get_absolute_url(self):
        """Return absolute url for SecurityInformation."""
        return ('')

    # TODO: Define custom methods here


class PersonalInformation(models.Model):
    """Model definition for PersonalInformation."""

    # TODO: Define fields here
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=18)

    class Meta:
        """Meta definition for PersonalInformation."""
        db_table = 'personal_information'
        verbose_name = 'PersonalInformation'
        verbose_name_plural = 'PersonalInformations'

    def __str__(self):
        """Unicode representation of PersonalInformation."""
        pass

    def save(self):
        """Save method for PersonalInformation."""
        pass

    def get_absolute_url(self):
        """Return absolute url for PersonalInformation."""
        return ('')

    # TODO: Define custom methods here

