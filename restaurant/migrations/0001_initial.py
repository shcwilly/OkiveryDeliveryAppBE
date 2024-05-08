# Generated by Django 5.0.4 on 2024-05-08 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hashtag', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('mandatory', models.BooleanField(default=False)),
                ('choice_mode', models.PositiveIntegerField(choices=[(1, 'Single'), (2, 'Multiple')], default=2)),
                ('maximum', models.PositiveIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.URLField(default=None, null=True)),
                ('representative_menu', models.PositiveIntegerField(default=None, null=True)),
                ('representative_menu_picture', models.URLField(default=None, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('notice', models.TextField(default=None, null=True)),
                ('delivery_fee', models.PositiveIntegerField(default=None, null=True)),
                ('minimum_order_amount', models.PositiveIntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('represent', models.CharField(default=None, max_length=20, null=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=None, null=True)),
                ('picture', models.URLField(default=None, null=True)),
                ('description', models.CharField(default=None, max_length=255, null=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Open'), (2, 'Sold Out'), (3, 'Hidden')])),
                ('menu_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu_group')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=None, null=True)),
                ('option_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.option_group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option_group_to_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
                ('option_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.option_group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='menu_group',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_groups', to='restaurant.restaurant'),
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.category')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='restaurant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantHashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.hashtag')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtags', to='restaurant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
