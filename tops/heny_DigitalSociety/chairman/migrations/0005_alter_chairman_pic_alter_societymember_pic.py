# Generated by Django 4.2.2 on 2023-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0004_alter_chairman_pic_alter_societymember_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/images/mypic.png', upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='societymember',
            name='pic',
            field=models.FileField(default='media/images/mypic.png', upload_to='media/images'),
        ),
    ]
