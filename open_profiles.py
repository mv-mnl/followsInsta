import os
import webbrowser
import sys

RESULTS_DIR = 'resultados'

def list_txt_files():
    if not os.path.isdir(RESULTS_DIR):
        return []
    files = [os.path.join(RESULTS_DIR, f) for f in os.listdir(RESULTS_DIR) if f.endswith('.txt')]
    return sorted(files)

def parse_usernames(filepath):
    usernames = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # Lines are format: "1. username"
            parts = line.strip().split('. ')
            if len(parts) >= 2:
                # Handle cases where username might contain dots, though split('. ', 1) is safer
                # But strict format "Number. username" is expected
                usernames.append(parts[1])
    return usernames

def main():
    print("Archivos disponibles:")
    files = list_txt_files()
    
    if not files:
        print("No se encontraron archivos .txt.")
        return

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    try:
        selection = int(input("\nSelecciona el número del archivo que quieres abrir: "))
        if selection < 1 or selection > len(files):
            print("Selección inválida.")
            return
        
        selected_file = files[selection - 1]
    except ValueError:
        print("Entrada inválida.")
        return

    users = parse_usernames(selected_file)
    total_users = len(users)
    print(f"\nSe encontraron {total_users} usuarios en {selected_file}.")
    print("Modos:")
    print("1. Abrir uno por uno (Presionar Enter)")
    print("2. Abrir todos (¡Cuidado con muchos usuarios!)")
    
    mode = input("Selecciona modo (1 o 2): ").strip()

    if mode == '2':
        for user in users:
            url = f"https://www.instagram.com/{user}/"
            print(f"Abriendo: {user}")
            webbrowser.open(url)
    
    else:
        print("\nPresiona Enter para abrir el siguiente perfil, o escribe 'q' y Enter para salir.")
        for i, user in enumerate(users, 1):
            url = f"https://www.instagram.com/{user}/"
            user_input = input(f"[{i}/{total_users}] Abrir {user}? ")
            if user_input.lower() == 'q':
                print("Saliendo...")
                break
            
            webbrowser.open(url)
            print(f"Abriendo {url} ...")

if __name__ == "__main__":
    main()
