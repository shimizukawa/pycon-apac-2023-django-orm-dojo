from django import template
from ..models import Staff

register = template.Library()


@register.filter
# @lru_cache  # キャッシュ検証用
def staff_status(obj: Staff):
    return f"最終ログイン:{obj.last_login:%Y-%m-%d}"


def staff_status2(obj: dict):
    return f"最終ログイン:{obj['last_login']:%Y-%m-%d}"


def staff_status3(obj: dict):
    return f"役割({obj['role__name']}) - " f"最終ログイン:{obj['last_login']:%Y-%m-%d}"


def staff_status4(obj: dict):
    return f"役割({obj['role_member__name']}) - " f"最終ログイン:{obj['last_login']:%Y-%m-%d}"
