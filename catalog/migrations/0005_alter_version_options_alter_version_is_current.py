# Generated by Django 4.2.5 on 2023-10-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_version_is_current'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('version_number',), 'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='is_current',
            field=models.BooleanField(choices=[(True, 'активная'), (False, 'не активная')], verbose_name='Признак текущей версии'),
        ),
    ]