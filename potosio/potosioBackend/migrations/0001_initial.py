# Generated by Django 3.2.7 on 2021-09-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_model', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Camera',
                'verbose_name_plural': 'Cameras',
                'db_table': 'camera',
            },
        ),
        migrations.CreateModel(
            name='CameraBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'CameraBrand',
                'verbose_name_plural': 'CameraBrands',
                'db_table': 'camera_brand',
            },
        ),
        migrations.CreateModel(
            name='CameraType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_type', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'CameraType',
                'verbose_name_plural': 'CameraType',
                'db_table': 'camera_type',
            },
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'ClientProfile',
                'verbose_name_plural': 'ClientProfiles',
                'db_table': 'client_profile',
            },
        ),
        migrations.CreateModel(
            name='GPSLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'GPSLocation',
                'verbose_name_plural': 'GPSLocations',
                'db_table': 'gps_location',
            },
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=18)),
            ],
            options={
                'verbose_name': 'PersonalInformation',
                'verbose_name_plural': 'PersonalInformations',
                'db_table': 'personal_information',
            },
        ),
        migrations.CreateModel(
            name='PhotographerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer_type', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'PhotographerType',
                'verbose_name_plural': 'PhotographerTypes',
                'db_table': 'photographer_type',
            },
        ),
        migrations.CreateModel(
            name='PhotographyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photography_type', models.CharField(max_length=13)),
            ],
            options={
                'verbose_name': 'PhotographyType',
                'verbose_name_plural': 'PhotographyTypes',
                'db_table': 'photography_type',
            },
        ),
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_imgae', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'ProfilePhoto',
                'verbose_name_plural': 'ProfilePhotos',
                'db_table': 'profile_photo',
            },
        ),
        migrations.CreateModel(
            name='SecurityInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(max_length=17)),
                ('nid_side_1', models.ImageField(upload_to='')),
                ('nid_side_2', models.ImageField(upload_to='')),
                ('passport_number', models.CharField(max_length=18)),
                ('birth_certificate', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
            options={
                'verbose_name': 'SecurityInformation',
                'verbose_name_plural': 'SecurityInformations',
                'db_table': 'security_information',
            },
        ),
        migrations.CreateModel(
            name='ShowcasePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph1', models.ImageField(upload_to='')),
                ('ph2', models.ImageField(upload_to='')),
                ('ph3', models.ImageField(upload_to='')),
                ('ph4', models.ImageField(upload_to='')),
                ('ph5', models.ImageField(upload_to='')),
                ('ph6', models.ImageField(upload_to='')),
                ('ph7', models.ImageField(upload_to='')),
                ('ph8', models.ImageField(upload_to='')),
                ('ph9', models.ImageField(upload_to='')),
                ('ph10', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'ShowcasePhoto',
                'verbose_name_plural': 'ShowcasePhotos',
                'db_table': 'showcase_photo',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='PhotographerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(upload_to='')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potosioBackend.camera')),
                ('photographer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potosioBackend.photographertype')),
                ('photography_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potosioBackend.photographytype')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potosioBackend.skill')),
            ],
            options={
                'verbose_name': 'Photographer',
                'verbose_name_plural': 'Photographers',
                'db_table': 'photographer_profile',
            },
        ),
        migrations.AddField(
            model_name='camera',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potosioBackend.camerabrand'),
        ),
    ]
