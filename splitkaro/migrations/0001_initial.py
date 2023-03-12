# Generated by Django 4.1.7 on 2023-03-09 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpanseGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ExpanseGroup_name', models.CharField(max_length=255)),
                ('ExpanseGroup_description', models.TextField(blank=True, null=True)),
                ('ExpanseGroup_created_at', models.DateTimeField(auto_now_add=True)),
                ('ExpanseGroup_updated_at', models.DateTimeField(auto_now=True)),
                ('ExpanseGroup_image', models.TextField(blank=True, null=True)),
                ('ExpanseGroup_amount', models.TextField(blank=True, default='0', null=True)),
                ('ExpanseGroup_is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('User_name', models.CharField(max_length=255)),
                ('User_email', models.CharField(max_length=255)),
                ('User_created_at', models.DateTimeField(auto_now_add=True)),
                ('User_updated_at', models.DateTimeField(auto_now=True)),
                ('User_is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpanseGroupUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ExpanseGroupUser_created_at', models.DateTimeField(auto_now_add=True)),
                ('ExpanseGroupUser_updated_at', models.DateTimeField(auto_now=True)),
                ('ExpanseGroupUser_is_active', models.BooleanField(default=True)),
                ('ExpanseGroupUser_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExpanseGroupUser_group_id', to='splitkaro.expansegroup')),
                ('ExpanseGroupUser_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitkaro.user')),
            ],
        ),
        migrations.CreateModel(
            name='Expanse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Expanse_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_created_at', models.DateTimeField(auto_now_add=True)),
                ('Expanse_updated_at', models.DateTimeField(auto_now=True)),
                ('Expanseamount', models.TextField(blank=True, default='0', null=True)),
                ('Expanse_is_active', models.BooleanField(default=True)),
                ('Expanse_description', models.TextField(blank=True, null=True)),
                ('Expanse_Note', models.TextField(blank=True, null=True)),
                ('Expanse_Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_locationName', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_locationAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_locationCity', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_locationState', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_locationCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('Expanse_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expanse_group_id', to='splitkaro.expansegroupuser')),
                ('Expanse_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expanse_user_id', to='splitkaro.user')),
            ],
        ),
    ]