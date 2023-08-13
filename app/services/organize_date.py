from collections import defaultdict
from app.services.generate_users import T_HUMANS


def organize_data(humans: T_HUMANS):
    groups = defaultdict(lambda: {"quantity": 0, "members": []})
    for human in humans:
        group_name = human["group"]
        groups[group_name]["quantity"] += 1
        groups[group_name]["members"].append(human["name"])

    return groups
