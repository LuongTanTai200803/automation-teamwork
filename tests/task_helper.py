from datetime import datetime, timezone
from dateutil import parser

def filter_overdue_tasks(cards, now=None):
    now = now or  datetime.now(timezone.utc)
    # print(type(now), now.tzinfo)
    overdue = []
    for card in cards:
        due = card.get("due")
        if due:
            due_date = parser.isoparse(due)
            if due_date < now:
                overdue.append(card["name"])
                # print(type(due_date), due_date.tzinfo)
    return overdue


