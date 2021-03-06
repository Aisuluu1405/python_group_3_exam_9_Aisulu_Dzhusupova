# Generated by Django 2.2 on 2019-12-14 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='user_photo', verbose_name='Фотография')),
                ('note', models.CharField(max_length=100, verbose_name='Подпись')),
                ('like', models.IntegerField(default=0, verbose_name='Лайк')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000, verbose_name='Комментарий')),
                ('author_comment', models.CharField(max_length=50, verbose_name='Автор комментария')),
                ('create_comment', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.Image', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
