messages = [
    {"id": "I01", "message": "{}({})が登録されました"},
    {"id": "I02", "message": "{}は「{}」に変更されました"},
    {"id": "I03", "message": "{}({})が登録されました"},
    {"id": "I04", "message": "祝日マスタが登録されていません"},
]


def get_inform_message(id, *args):
    message = next(filter(lambda message: message["id"] == id, messages), None)
    if message is None:
        raise ValueError("invalid message id")

    return message["message"].format(*args)
