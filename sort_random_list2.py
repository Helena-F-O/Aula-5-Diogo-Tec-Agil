def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
  from random_list_generator2 import generate_random_list

  # Gerar a lista aleatória
  random_list = generate_random_list()

  # Ordenar a lista usando o quicksort
  sorted_list = quicksort(random_list)

  # Imprimir a lista ordenada
  print(sorted_list)
