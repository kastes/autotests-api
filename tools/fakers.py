import time


def get_random_email() -> str:
    return f"test{time.time()}@example.com"


if __name__ == "__main__":
    print(get_random_email())
