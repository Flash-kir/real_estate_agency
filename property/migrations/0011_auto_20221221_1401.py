# Generated by Django 2.2.24 on 2022-12-21 11:01

from django.db import migrations


def owners_table_fill(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            phone=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
            )
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221221_1352'),
    ]

    operations = [
        migrations.RunPython(owners_table_fill),
    ]
