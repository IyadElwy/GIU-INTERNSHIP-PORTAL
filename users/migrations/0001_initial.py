# Generated by Django 4.0 on 2022-01-05 21:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_faculty_representative', models.BooleanField(default=False)),
                ('is_academic_advisor', models.BooleanField(default=False)),
                ('is_career_office_coordinator', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='AcademicAdvisor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('faculty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CareerOfficeCoordinator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('company_name', models.CharField(max_length=20)),
                ('employer_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(max_length=50)),
                ('type_of_business', models.CharField(max_length=50)),
                ('establishment_year', models.DateField()),
                ('country_of_origin', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=20)),
                ('number_of_current_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('products_or_services', models.CharField(max_length=30)),
                ('company_logo', models.ImageField(blank=True, default='company_images/default.png', max_length=1000, null=True, upload_to='C:\\Users\\iyade\\PycharmProjects\\Python-Personal-Projects\\GIU_Internship_Portal\\media/company_images/')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyRepresentative',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('faculty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GIUAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('middle_name', models.CharField(max_length=20)),
                ('student_university_id', models.PositiveIntegerField()),
                ('birthdate', models.DateField()),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('faculty', models.CharField(choices=[('Engineering', 'Engineering'), ('Computer Science', 'Computer Science'), ('Business', 'Business'), ('Design', 'Design'), ('Architecture', 'Architecture'), ('Biotechnology', 'Biotechnology'), ('Pharmaceutical', 'Pharmaceutical')], max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('student_address', models.CharField(max_length=10)),
                ('has_cv', models.BooleanField(blank=True, default=False)),
                ('cover_letter', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('employer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('contact_person_name', models.CharField(blank=True, default='None', max_length=20, null=True)),
                ('job_title', models.CharField(blank=True, default='None', max_length=30, null=True)),
                ('email', models.CharField(blank=True, default='None', max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, default='None', max_length=20, null=True)),
                ('fax', models.CharField(blank=True, default='None', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HRDirector',
            fields=[
                ('employer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('hr_name', models.CharField(blank=True, default='None', max_length=20, null=True)),
                ('hr_email', models.CharField(blank=True, default='None', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPhoneNumbers',
            fields=[
                ('phone_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
            options={
                'unique_together': {('student_id', 'phone_number')},
            },
        ),
    ]
