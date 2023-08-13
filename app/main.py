from app.services.generate_users import DataProvider
from app.services.get_formatted_output import get_formatted_output
from app.services.organize_date import organize_data


def main():
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)
