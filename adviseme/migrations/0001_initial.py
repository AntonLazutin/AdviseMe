# Generated by Django 3.2.9 on 2021-12-06 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(choices=[('MOV', 'Movie'), ('BK', 'Book'), ('GM', 'Game')], default=None, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('genre', models.TextField(choices=[('MOV', 'Movie'), ('BK', 'Book'), ('GM', 'Game')])),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Date published')),
                ('subject', models.TextField(max_length=20)),
                ('text', models.TextField(default='', max_length=100)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='adviseme.review')),
            ],
        ),
    ]
