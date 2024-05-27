# Generated by Django 4.2.8 on 2024-05-26 04:49

import apps.common.models_blog
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0003_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=apps.common.models_blog.get_thumbnail_filename)),
                ('url', models.URLField(blank=True)),
                ('type', models.CharField(choices=[('video', 'video'), ('pdf', 'pdf'), ('image', 'image'), ('other', 'other')], default='other', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.file'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.file'),
        ),
    ]