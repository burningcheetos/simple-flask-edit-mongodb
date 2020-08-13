def identifier():
    count = 0
    while True:
        yield count
        count += 1

user_id = identifier()

db = [
    {
        "user": "a",
        "id": next(user_id),
        "access": "low",
        "profile": "blue eyes"
    },
    {
        "user": "b",
        "id": next(user_id),
        "access": "high",
        "profile": "green eyes"
    },
    {
        "user": "c",
        "id": next(user_id),
        "access": "high",
        "profile": "brown eyes"
    },
    {
        "user": "d",
        "id": next(user_id),
        "access": "mid",
        "profile": "grey eyes"
    },
]