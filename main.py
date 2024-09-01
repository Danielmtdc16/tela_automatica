from pynput import mouse, keyboard
import webbrowser
import time

tempo_padrao_inatividade = 5 # segundos
site_a_ser_aberto = "https://www.youtube.com/"
tempo_sem_mexer_em_nada = 0 # segundos

# Funções de MOUSE
def on_click(x, y, button, pressed):
    if pressed:
        global tempo_sem_mexer_em_nada
        tempo_sem_mexer_em_nada = 0

def on_move(x, y):
    global tempo_sem_mexer_em_nada
    tempo_sem_mexer_em_nada = 0

def on_scroll(x, y, dx, dy):
    global tempo_sem_mexer_em_nada
    tempo_sem_mexer_em_nada = 0

# Escuta do MOUSE
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
mouse_listener.start() # Iniciando a escuta

# Funções do TECLADO
def on_press(key):
    global tempo_sem_mexer_em_nada
    tempo_sem_mexer_em_nada = 0

# Escuta do TECLADO
teclado_listener = keyboard.Listener(on_press=on_press)
teclado_listener.start()

while True:
    if tempo_sem_mexer_em_nada >= tempo_padrao_inatividade:
        tempo_sem_mexer_em_nada = 0
        webbrowser.open(url=site_a_ser_aberto)

    tempo_sem_mexer_em_nada += 1
    time.sleep(1)
    print(f"tempo sem mexer: {tempo_sem_mexer_em_nada}")