# Django初期化
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# views.py
from app.models import Staff
staffs = Staff.objects.order_by("last_login").only("pk", "name")

# index.html
from app.templatetags.status import staff_status
for staff in staffs:
    print({"pk": staff.pk, "name": staff.name, "status": staff_status(staff)})

