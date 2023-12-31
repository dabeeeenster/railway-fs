from rest_framework.exceptions import APIException


class InviteExpiredError(APIException):
    status_code = 400
    default_detail = "Invite has expired"


class InviteLinksDisabledError(APIException):
    status_code = 400
    default_detail = "Invite links are disabled."
