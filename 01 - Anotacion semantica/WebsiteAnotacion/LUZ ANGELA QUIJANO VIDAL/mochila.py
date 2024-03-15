def master_problem(values, weights, volume, capacity):
    # Paso 1: Inicializar la tabla dp
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    print (dp);

    # Paso 2: Llenar la tabla dp
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # Paso 2.1: Comprobar si el peso del elemento actual es menor o igual al volumen actual
            if weights[i - 1] <= j:
                # Paso 2.2: Calcular el máximo valor que se puede obtener al incluir o excluir el elemento actual
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                # Paso 2.3: El elemento actual no cabe en el volumen, por lo que el máximo valor es el mismo que el valor anterior
                dp[i][j] = dp[i - 1][j]


    # Paso 3: Imprimir la tabla dp
    print("Item weights: ", weights)
    print("Item values: ", values)
    print("Volume: ", volume)
    print("Capacity: ", capacity)
    print("Table:")
    for row in dp:
        print(row)


    # Paso 4: Devolver el máximo valor que se puede obtener sin exceder la capacidad
    return dp[n][capacity]



# Paso 5: Llamar a la función master_problem con los valores y pesos de los elementos, el volumen y la capacidad deseados
values = [3, 9, 15]
weights = [2, 5, 14]
volume = 5
capacity = 10
print("Maximum value that can be obtained without exceeding the capacity is:")
print(master_problem(values, weights, volume, capacity))

