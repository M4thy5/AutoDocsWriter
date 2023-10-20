import pyautogui
from time import sleep


def linha():
    print("\033[30m==\033[m" * 11)


def main():
    pyautogui.hotkey("alt", "tab")
    sleep(1)
    pyautogui.hotkey("f2")


contador_docs = int(input("\033[34mQual a quantidade de docs: \033[m").strip())

while True:
    contador = 0
    pergunta_docs = str(input("""\033[32mEscreva a especificação em minúsculo!
Digite: """)).strip().upper()
    linha()
    main()

    while contador != contador_docs:
        sleep(0.89)
        pyautogui.hotkey("right")
        pyautogui.write((f" - {pergunta_docs}"))
        pyautogui.hotkey("tab")
        contador += 1
