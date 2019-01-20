""" Manually generated by Anas Abou Allaban(piraka9011).
    Taken from: https://bit.ly/2SnPJO1
"""
from __future__ import unicode_literals

from django.db import migrations


def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    site_model = apps.get_model('sites', 'Site')
    site_model.objects.all().delete()

    # Register SITE_ID = 1
    site_model.objects.create(pk=1, domain='tarteel.io', name='tarteel')
    # Register SITE_ID = 2
    site_model.objects.create(pk=2, domain='127.0.0.1', name='tarteel-test')


def revert_sites(apps, schema_editor):
    """Revert `insert_sites` changes"""
    site_model = apps.get_model('sites', 'Site')
    site_model.objects.all().delete()
    site_model.objects.create(pk=1, domain='example.com', name='example')


def create_groups(apps, schema_editor):
    """Creates the evaluator group"""
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name='evaluator')


def revert_groups(apps, schema_editor):
    """Reverts `create_groups` changes"""
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='evaluator').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sites, revert_sites),
        migrations.RunPython(create_groups, revert_groups)
    ]
