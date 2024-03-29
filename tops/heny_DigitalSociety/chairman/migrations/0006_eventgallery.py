# Generated by Django 4.2.2 on 2023-06-06 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0005_alter_chairman_pic_alter_societymember_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=30)),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='')),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/images')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairman.user')),
            ],
        ),
    ]
