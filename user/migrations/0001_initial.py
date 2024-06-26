# Generated by Django 4.2 on 2024-04-08 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BASE', '0010_grade_schooltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('student', 'student'), ('provider', 'provider'), ('admin', 'admin')], default='student', max_length=10)),
                ('verified', models.BooleanField(default=False)),
                ('credit', models.FloatField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('lat', models.FloatField(blank=True, default=None, null=True)),
                ('lng', models.FloatField(blank=True, default=None, null=True)),
                ('picture', models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BASE.grade')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BASE.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
