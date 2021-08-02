from django.db import models

# Create your models here.


class PhotographerType(models.Model):
    """Model definition for PhotographerType."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for PhotographerType."""

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

    class Meta:
        """Meta definition for PhotographyType."""

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


class CameraManufacturer(models.Model):
    """Model definition for CameraManufacturer."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for CameraManufacturer."""

        verbose_name = 'CameraManufacturer'
        verbose_name_plural = 'CameraManufacturers'

    def __str__(self):
        """Unicode representation of CameraManufacturer."""
        pass

    def save(self):
        """Save method for CameraManufacturer."""
        pass

    def get_absolute_url(self):
        """Return absolute url for CameraManufacturer."""
        return ('')

    # TODO: Define custom methods here


class Camera(models.Model):
    """Model definition for Camera."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Camera."""

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


class PhotographerProfile(models.Model):
    """Model definition for Photographer."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Photographer."""

        verbose_name = 'Photographer'
        verbose_name_plural = 'Photographers'

    def __str__(self):
        """Unicode representation of Photographer."""
        pass

    def save(self):
        """Save method for Photographer."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Photographer."""
        return ('')

    # TODO: Define custom methods here

    """Model definition for Client."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Client."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        pass

    def save(self):
        """Save method for Client."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Client."""
        return ('')

    # TODO: Define custom methods here


class ClientProfile(models.Model):
    """Model definition for ClientProfile."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for ClientProfile."""

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

    """Model definition for PhotographerProfile."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for PhotographerProfile."""

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


class Photo(models.Model):
    """Model definition for Photo."""

    # TODO: Define fields here
    class Meta:
        """Meta definition for Photo."""

        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        """Unicode representation of Photo."""
        pass

    def save(self):
        """Save method for Photo."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Photo."""
        return ('')

    # TODO: Define custom methods here


class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Address."""

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


class Location(models.Model):
    """Model definition for Location."""

    # TODO: Define fields here
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Location."""
        pass

    def save(self):
        """Save method for Location."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Location."""
        return ('')

    # TODO: Define custom methods here


class CommonInformation(models.Model):
    """Model definition for CommonInformation."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for CommonInformation."""

        verbose_name = 'CommonInformation'
        verbose_name_plural = 'CommonInformations'

    def __str__(self):
        """Unicode representation of CommonInformation."""
        pass

    def save(self):
        """Save method for CommonInformation."""
        pass

    def get_absolute_url(self):
        """Return absolute url for CommonInformation."""
        return ('')

    # TODO: Define custom methods here
