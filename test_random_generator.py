from random_generator import generate_random_list


def test_generate_random_list():
  # Gerar uma lista com 20.000 números aleatórios
  random_list = generate_random_list()

  # Verificar se a lista tem o comprimento correto
  assert len(random_list) == 20000

  # Verificar se todos os números estão dentro do intervalo correto
  min_value = -999999
  max_value = 999999
  assert all(min_value <= num <= max_value for num in random_list)
