# Generated by Django 4.1.7 on 2023-03-12 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitkaro', '0004_alter_linkexpansegroupuser_linkexpansegroupuser_group_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkexpansegroupuser',
            name='LinkExpanseGroupUser_group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LinkExpanseGroupUser_group_id', to='splitkaro.expansegroup'),
        ),
        migrations.AlterField(
            model_name='linkexpansegroupuser',
            name='LinkExpanseGroupUser_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LinkExpanseGroupUser_user_id', to='splitkaro.user'),
        ),
    ]
