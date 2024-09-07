import pyperclip

def paste():
    clip = pyperclip.paste()
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(clip)
        print("Raw Data pasted")
