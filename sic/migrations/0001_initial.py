# Generated by Django 3.1.3 on 2021-07-01 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('avatar', models.CharField(editable=False, max_length=8196, null=True)),
                ('email_notifications', models.BooleanField(default=False)),
                ('email_replies', models.BooleanField(default=False)),
                ('email_messages', models.BooleanField(default=False)),
                ('email_mentions', models.BooleanField(default=False)),
                ('show_avatars', models.BooleanField(default=True)),
                ('show_story_previews', models.BooleanField(default=False)),
                ('show_submitted_story_threads', models.BooleanField(default=False)),
                ('github_username', models.CharField(max_length=500, null=True)),
                ('homepage', models.URLField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_moderator', models.BooleanField(default=False)),
                ('banned_by_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banned_by', to=settings.AUTH_USER_MODEL)),
                ('disabled_invite_by_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Moderation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sic.domain')),
                ('merged_into', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sic.story')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TagFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(to='sic.Tag'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_by_recipient', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
                ('hat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sic.hat')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField()),
                ('inviter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sic.comment')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.story')),
            ],
        ),
    ]
