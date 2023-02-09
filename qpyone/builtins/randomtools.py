import random

from faker import Faker


__all__ = ["faker", "random_str", "random_unicode", "random_GBK2312"]

faker = Faker(["en_US", "zh_CN"])


def random_unicode():
    val = random.randint(0x4E00, 0x9FBF)
    return chr(val)


def random_GBK2312():
    head = random.randint(0xB0, 0xF7)
    body = random.randint(0xA1, 0xFE)
    val = f"{head:x} {body:x}"
    return bytes.fromhex(val).decode("gb2312")


def random_str(length=4):
    result = []
    for i in range(length):
        result.append(random.choice([random_unicode])())
    return "".join(result)
