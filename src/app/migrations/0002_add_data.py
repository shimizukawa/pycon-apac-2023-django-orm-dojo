# Generated by Django 4.1.4 on 2022-12-20 08:49

from django.db import migrations
from django.utils import timezone


def add_data(apps, schema_editor):
    # setup staffs
    Staff = apps.get_model("app", "Staff")
    dt = timezone.make_aware(timezone.datetime(2023, 10, 27, 1, 23, 45))
    s1 = Staff.objects.create(name="staff1", last_login=dt)
    s2 = Staff.objects.create(name="staff2", last_login=dt)
    s3 = Staff.objects.create(name="staff3", last_login=dt)
    s4 = Staff.objects.create(name="staff4", last_login=dt)

    # setup roles
    Role = apps.get_model("app", "Role")
    role_officer = Role.objects.create(name="officer")
    role_mailman = Role.objects.create(name="mailman")
    role_officer.staffs.set([s1, s2])
    role_mailman.staffs.set([s2, s3, s4])

    # setup people
    Person = apps.get_model("app", "Person")
    p1 = Person.objects.create(name="p1")
    p2 = Person.objects.create(name="p2")
    p3 = Person.objects.create(name="p3")
    p4 = Person.objects.create(name="p4")
    p5 = Person.objects.create(name="p5")
    p6 = Person.objects.create(name="p6")
    p7 = Person.objects.create(name="p7")

    # setup deliveries
    Delivery = apps.get_model("app", "Delivery")
    Delivery.objects.create(date="2023-10-27", receiver=p1, mailman=s2)
    Delivery.objects.create(date="2023-10-27", receiver=p2, mailman=s2)
    Delivery.objects.create(date="2023-10-28", receiver=p1, mailman=s2)
    Delivery.objects.create(date="2023-10-28", receiver=p2, mailman=s2)
    Delivery.objects.create(date="2023-10-28", receiver=p3, mailman=s2)
    Delivery.objects.create(date="2023-10-28", receiver=None, mailman=s2)
    Delivery.objects.create(date="2023-10-28", receiver=p4, mailman=s3)
    Delivery.objects.create(date="2023-10-28", receiver=p5, mailman=s3)
    Delivery.objects.create(date="2023-10-28", receiver=p6, mailman=s3)
    Delivery.objects.create(date="2023-10-28", receiver=p7, mailman=s3)
    Delivery.objects.create(date="2023-10-28", receiver=None, mailman=s3)
    Delivery.objects.create(date="2023-10-28", receiver=None, mailman=s3)


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            code=add_data,
            reverse_code=migrations.RunPython.noop,
        )
    ]
