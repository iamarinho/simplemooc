# Generated by Django 2.2.1 on 2019-06-17 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190617_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Número (Ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['number'],
            },
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-created_at'], 'verbose_name': 'Anúncio', 'verbose_name_plural': 'Anúncios'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Embedded')),
                ('file', models.FileField(blank=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='Aula')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
