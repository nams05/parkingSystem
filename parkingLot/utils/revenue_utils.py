from datetime import datetime, timedelta
from ..models import Revenue
from django.db.models import Sum
from django.utils import timezone

rate_card = {
    1: 20,
    2: 10,
    24: 200
}


def parking_fee(entry_time):
    tz_info = entry_time.tzinfo
    exit_time = datetime.now(tz_info)
    total_time = exit_time - entry_time
    total_time_in_sec = total_time.total_seconds()
    total_time_in_days = divmod(total_time_in_sec, 86400)
    total_time_in_hours = divmod(total_time_in_days[1], 3600)

    total_parking_fee = rate_card[24]*total_time_in_days[0]
    if total_time_in_hours[1] != 0:
        total_hours_charged = int(total_time_in_hours[0] + 1)

    if total_hours_charged == 1:
        total_parking_fee += rate_card[1]
    elif total_hours_charged < 13:
        total_parking_fee += (total_hours_charged-1)*rate_card[2] + rate_card[1]
    else:
        total_parking_fee += rate_card[24]

    return int(total_parking_fee)


def calculate_total_revenue():
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)
    total_revenue = Revenue.objects.filter(updated_at__lte=end_date, updated_at__gte=start_date)\
        .aggregate(fee=Sum('parking_fee'))['fee']
    return total_revenue

