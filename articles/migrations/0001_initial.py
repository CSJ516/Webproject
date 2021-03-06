# Generated by Django 3.0.8 on 2020-07-15 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleCategory', models.CharField(choices=[('book', '도서'), ('event', '행사'), ('author', '저자')], max_length=255, verbose_name='기사카테고리')),
                ('articleTitle', models.CharField(max_length=255, verbose_name='기사제목')),
                ('articleExp', models.TextField(verbose_name='기사내용')),
                ('articleDate', models.DateField(auto_now_add=True, verbose_name='기사등록날짜')),
                ('eventName', models.CharField(max_length=255, null=True, verbose_name='행사이름')),
                ('bookArticlePic', models.ImageField(blank=True, null=True, upload_to='articles/book/', verbose_name='도서기사사진')),
                ('eventArticlePic', models.ImageField(blank=True, null=True, upload_to='articles/event/', verbose_name='행사기사사진')),
                ('authorArticlePic', models.ImageField(blank=True, null=True, upload_to='articles/author/', verbose_name='저자기사사진')),
                ('authorID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='저자ID')),
                ('bookID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='도서ID')),
            ],
        ),
    ]
