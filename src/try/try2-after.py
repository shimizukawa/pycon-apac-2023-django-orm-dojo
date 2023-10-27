# Django初期化
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


# views.py
from datetime import date
from django.db.models import Count, Q
from app.models import Staff
today = date(2023, 2, 14)  # 動作検証用
qs = (
    Staff.objects
    .values("pk", "name")  # group byのキー
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
).values("pk", "name", "delivery_num", "unknown_num")

## クエリーセットを辞書のリストに展開。データの詰め替えは不要
values = list(qs)

# index.html
## todayは各行に持たせず別で渡せばよい
print(today)
for staff in values:
    print(staff)

# ----------------------------

# SQL確認
print("### valuesに変更したSQL")
def printsql(query):
    from sqlparse import format as sfmt
    print(sfmt(str(query), reindent_aligned=True))

printsql(qs.query)


# ----------------------------

print("### SQLを観察してORMを組みなおした改善版")
from django.db.models import FilteredRelation, F

# ORMクエリの実装
qs = (
    Staff.objects
    .values("pk", "name")  # group byのキー
    .annotate(
        dlist=FilteredRelation("delivery", condition=Q(delivery__date=today)),
        delivery_num=Count("dlist__receiver"),
        unknown_num=Count(
            "dlist",
            filter=Q(dlist__receiver__isnull=True),
        ),
    ).values("pk", "name", "delivery_num", "unknown_num")
)

printsql(qs.query)
