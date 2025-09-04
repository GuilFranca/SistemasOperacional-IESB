import threading  # Importa a biblioteca para trabalhar com threads
import time       # Importa para usar time.sleep() e simular atraso

# Função que a Thread-1 vai executar: imprimir números de 1 a 10
def print_numbers_1_to_10():
    for num in range(1, 11):  # Loop de 1 a 10 (inclusive)
        print(f"Thread-1: {num}")  # Imprime o número atual da Thread-1
        time.sleep(0.5)  # Pausa meio segundo para simular processamento

# Função que a Thread-2 vai executar: imprimir números de 50 a 60
def print_numbers_50_to_60():
    for num in range(50, 61):  # Loop de 50 a 60 (inclusive)
        print(f"Thread-2: {num}")  # Imprime o número atual da Thread-2
        time.sleep(0.5)  # Pausa meio segundo para simular processamento

# Ponto de entrada do programa
if __name__ == "__main__":
    # Cria a Thread-1, passando a função print_numbers_1_to_10 para ela executar
    thread1 = threading.Thread(target=print_numbers_1_to_10)

    # Cria a Thread-2, passando a função print_numbers_50_to_60 para ela executar
    thread2 = threading.Thread(target=print_numbers_50_to_60)

    # Inicia a execução das duas threads
    thread1.start()
    thread2.start()

    # Aguarda que a Thread-1 termine sua execução
    thread1.join()

    # Aguarda que a Thread-2 termine sua execução
    thread2.join()

    # Só chega aqui quando ambas as threads terminaram
    print("Programa finalizado: ambas as threads terminaram.")
