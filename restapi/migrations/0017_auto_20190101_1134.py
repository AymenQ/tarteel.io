# Generated by Django 2.1.3 on 2019-01-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0016_remove_demographicinformation_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographicinformation',
            name='platform',
            field=models.CharField(default='web', max_length=256),
        ),
    ]
