import random


def generate_random_list(length=20000, min_value=-999999, max_value=999999):
  return [random.randint(min_value, max_value) for _ in range(length)]
