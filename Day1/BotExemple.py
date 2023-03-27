import pyautogui
from time import sleep

quantidade = int(input("Digite a quantidade de mensagens que deseja enviar: "))
mensagem = input("Digite a mensagem que deseja enviar: ")

sleep(4)

for c in range(quantidade + 1):
    pyautogui.write(mensagem)
    pyautogui.press('enter')

    