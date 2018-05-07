# import XRoadsServer.utils.database.users as db_users


# TODO: need to implement this
def email(email_str: str) -> bool:
    if email_str:
        return True
    return True


def new_user(request_data: dict) -> bool:
    # user_name = request_data["user_name"]
    # email = request_data["email"]
    for key in request_data.keys():
        if request_data[key] == "":
            return False
    # if db_users.is_user_unique(user_name) and \
    #    db_users.is_email_unique(email):
    #     return True
    # else:
    #     return False
    return True
