from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    DO_NOTHING,
)


class Staff(Model):
    name = CharField("名前", max_length=32)
    last_login = DateTimeField("最終ログイン")

    class Meta:
        db_table = "staff"


class Role(Model):
    name = CharField("ロール", unique=True, max_length=16)
    staffs = ManyToManyField("Staff", related_name="roles")

    class Meta:
        db_table = "role"


class Delivery(Model):
    date = DateField("配達日")
    receiver = ForeignKey("Person", null=True, on_delete=DO_NOTHING)
    mailman = ForeignKey("Staff", on_delete=DO_NOTHING)

    class Meta:
        db_table = "delivery"


class Person(Model):
    name = CharField("利用者", max_length=32)
    # 住所等は省略

    class Meta:
        db_table = "person"
