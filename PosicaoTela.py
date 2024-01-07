import pyautogui


# Mostrar as coordenadas do cursor do mouse
print("Posicione o cursor na posição desejada...")
print("Pressione Ctrl + C para sair.")

try:
    while True:
        # Obter e exibir a posição atual do cursor
        x, y = pyautogui.position()
        position_str = f'X: {x}, Y: {y}'
        print(position_str, end='\r')  # Mostra a posição atual sem criar novas linhas
except KeyboardInterrupt:
    print('\nPosição final obtida  .')