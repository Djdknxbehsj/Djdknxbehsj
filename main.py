import os
import subprocess
from colorama import init, Fore, Style
import pystyle
from pystyle import Box

print(Fore.RED + """
░█████╗░███╗░░██╗██╗░██████╗████████╗
██╔══██╗████╗░██║██║██╔════╝╚══██╔══╝
██║░░██║██╔██╗██║██║╚█████╗░░░░██║░░░
██║░░██║██║╚████║██║░╚═══██╗░░░██║░░░
╚█████╔╝██║░╚███║██║██████╔╝░░░██║░░░
░╚════╝░╚═╝░░╚══╝╚═╝╚═════╝░░░░╚═╝░░░""")
print(" ")
print(Fore.GREEN + "               Channel: @Softi_Termux")

def bd():
    init(autoreset=True)
    
    if not os.path.exists('Database'):
        print(f"{Fore.RED}Системе не удается найти папку 'Database'.{Style.RESET_ALL}")
        return
    
    count = len(os.listdir('Database'))
    print(f"{Fore.GREEN}Имеется {count} базы.{Style.RESET_ALL}")
    
    data = input(f"{Fore.CYAN}Введите запрос: {Style.RESET_ALL}")
    print('Поиск начат, может идти до 5 минут!')

    result = ''
    for label in os.listdir('Database'):
        file_path = os.path.join('Database', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        result += f"[{label}] - {line.strip()}"  
                        break  
        except Exception as e:
            print(f"{Fore.RED}Ошибка при чтении файла {label}: {e}{Style.RESET_ALL}")

    print(Fore.BLUE + 'Поиск окончен!')
    if result:
        print(Fore.BLUE + 'Вот что мы нашли:')
        pystyle.Write.Print(result, pystyle.Colors.blue_to_cyan, interval=0.000000001)
        print(" ")
    else:
        print(Fore.BLUE + "Ничего не найдено.")
        print(" ")

    input("Нажмите Enter" + Style.RESET_ALL)
    
    
    subprocess.run(["python", "main.py"])


bd()
