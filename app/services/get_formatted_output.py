def get_formatted_output(data) -> str:
    output = ""
    for group_name, group_data in data.items():
        quantity = group_data["quantity"]
        members = ", ".join(group_data["members"])
        output += f"Group: {group_name}, Quantity: {quantity}, Members: {members}\n"

    return output

