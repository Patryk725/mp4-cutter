import os
import re

folder_path = "."
text_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.txt')]

if len(text_files) == 1:
    answer = input(f"Edycja pliku: {text_files[0]}. Kontynuować? t/n: ")
    if answer.lower() == 't':
        print(f"Wybrałeś: {text_files[0]}")
        chosen_text_file = text_files[0]
    else:
        print("Zakończono.")
else:
    print("\nDostępne pliki tekstowe:")
    for index, file in enumerate(text_files, 1):
        print(f"{index}. {file}")
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            print(f.read())

    try:
        chosen_text_file_index = int(input(f"Wybierz numer pliku tekstowego (1-{len(text_files)}): ")) - 1
        if 0 <= chosen_text_file_index < len(text_files):
            chosen_text_file = text_files[chosen_text_file_index]
            print(f"\nWybrano: {chosen_text_file}")
        else:
            print("Nieprawidłowy numer pliku tekstowego.")
    except ValueError:
        print("Proszę podać poprawny numer.")

if 'chosen_text_file' in locals():
    print(f"Zawartość pliku {chosen_text_file} będzie teraz przetwarzana.")
else:
    print("Nie wybrano pliku")

# 
with open(chosen_text_file, "r", encoding="utf-8") as f:
    file_txt = f.read()

matches = re.findall(r'\b\d{1,2}:\d{2}(?::\d{2})?\b', file_txt)

formatted_times = [
    f"00:{t.zfill(5)}" if t.count(":") == 1 else t.zfill(8)
    for t in matches
]

print(formatted_times)

new_filename = f"{chosen_text_file.rsplit('.txt', 1)[0]}-formatted.txt"

if not os.path.exists(new_filename):
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(" ".join(formatted_times))

print(f"Zapisano do pliku: {new_filename}")
