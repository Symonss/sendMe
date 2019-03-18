# Generated by Django 2.0.9 on 2019-03-11 11:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_employer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_regional_admin', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(default='Peterson', max_length=50)),
                ('last_name', models.CharField(default='Peterson', max_length=50)),
                ('phone', models.IntegerField(default='0792799958')),
                ('email', models.CharField(default='yourmail@gmail.com', max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('is_seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_topic', models.CharField(blank=True, max_length=200)),
                ('order_description', models.TextField(blank=True)),
                ('track_number', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(default='50')),
                ('words', models.IntegerField(default='50')),
                ('order_files', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_editing', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(default='Peterson', max_length=50)),
                ('last_name', models.CharField(default='Peterson', max_length=50)),
                ('phone', models.IntegerField(default='0792799958')),
                ('email', models.CharField(default='yourmail@gmail.com', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(default='Peterson', max_length=50)),
                ('last_name', models.CharField(default='Peterson', max_length=50)),
                ('phone', models.IntegerField(default='0792799958')),
                ('email', models.CharField(default='yourmail@gmail.com', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegionalAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(default='Peterson', max_length=50)),
                ('last_name', models.CharField(default='Peterson', max_length=50)),
                ('phone', models.IntegerField(default='0792799958')),
                ('email', models.CharField(default='yourmail@gmail.com', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='coreapp.Status'),
        ),
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='coreapp.Order'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='coreapp.Order'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='order',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='coreapp.Employer'),
        ),
    ]
