# Django初期化
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


# datamodels.py
import dataclasses
from datetime import date
@dataclasses.dataclass
class DeliveryDesc:
    pk: int  # 配達者pk
    name: str  # 配達者名
    date: date  # 配達日
    delivery_num: int | None = None  # 配達数
    unknown_num: int | None = None  # 宛先不明数


# views.py
from django.db.models import Count, Q
from app.models import Staff
from datetime import date
today = date(2023, 2, 14)  # 動作検証用
qs = (
    Staff.objects
    .annotate(
        delivery_num=Count(
            "delivery",
            filter=Q(
                delivery__date=today,
                delivery__receiver__isnull=False,
            ),
        ),
        unknown_num=Count(
            "delivery",
            filter=Q(
                delivery__date=today,
                delivery__receiver__isnull=True,
            ),
        ),
    )
)

# テンプレートへ渡すデータの詰め替え
desc_list = []
for staff in qs:
    desc = DeliveryDesc(
        pk=staff.pk,
        name=staff.name,
        date=today,
        delivery_num=staff.delivery_num,
        unknown_num=staff.unknown_num,
    )
    desc_list.append(desc)


# index.html
for desc in desc_list:
    print(desc)


# SQL確認
print("### printsqlによるSQL出力")
def printsql(query):
    from sqlparse import format as sfmt
    print(sfmt(str(query), reindent_aligned=True))

printsql(qs.query)
