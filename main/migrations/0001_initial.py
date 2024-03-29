# Generated by Django 4.2.10 on 2024-03-05 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poems', to='main.difficulty')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('choices', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.poem')),
            ],
        ),
    ]
