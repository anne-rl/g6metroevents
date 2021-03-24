# Generated by Django 3.1.1 on 2021-03-23 18:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metroevents', '0004_auto_20210324_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Administrators',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifType', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('sentDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('isViewed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('requestDateTime', models.DateTimeField()),
                ('responseDateTime', models.DateTimeField(null=True)),
                ('responseStatus', models.CharField(default='Pending', max_length=100)),
            ],
            options={
                'db_table': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('createdDateTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Upvotes',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventStatus',
            field=models.CharField(default='Upcoming', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='startdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(),
        ),
        migrations.AlterModelTable(
            name='event',
            table='Events',
        ),
        migrations.AddField(
            model_name='upvote',
            name='event',
            field=models.ManyToManyField(to='metroevents.Event'),
        ),
        migrations.AddField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='metroevents.event'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='request',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='metroevents.event'),
        ),
        migrations.AddField(
            model_name='request',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metroevents.organizer'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='metroevents.event'),
        ),
        migrations.AddField(
            model_name='notification',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='metroevents.request'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='metroevents.organizer'),
        ),
    ]