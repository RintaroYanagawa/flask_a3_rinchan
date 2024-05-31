messages = [
    {"id": "I01", "message": "{}({})が登録されました"},
    {"id": "I02", "message": "{}は「{}」に変更されました"},
    {"id": "I03", "message": "{}({})が削除されました"},
    {"id": "W01", "message": "{}は、祝日マスタに登録されていません"},
]


def get_inform_message(id, *args):
    message = next(filter(lambda message: message["id"] == id, messages), None)
    print(args)
    if message is None:
        raise ValueError("invalid message id")

    return message["message"].format(*args)
