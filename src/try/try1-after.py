# Django初期化
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# views.py
from app.models import Staff
staffs = Staff.objects.order_by("last_login").values("pk", "name", "last_login")

# index.html
from app.templatetags.status import staff_status_dict
for staff in staffs:
    print(
        {"pk": staff["pk"], "name": staff["name"], "status": staff_status_dict(staff)}
    )

