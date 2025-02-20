import os
import subprocess

# programming steps:
# 1. choose video
# 2. choose timestamps
# 3. create output folder
# 4. write outputs to output folder

# step 1

folder_path = "."

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.mp4')]
print(files)

if len(files) == 1:
    answer = input(f"Edycja pliku: {files[0]}. Kontynuować? t/n: ")
    if answer.lower() == 't':
        print(f"Wybrałeś: {files[0]}")
        chosen_file = files[0]
    else:
        print("Zakończono.")
else:
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    try:
        chosen_file_index = int(input("Wybierz numer pliku: ")) - 1
        if 0 <= chosen_file_index < len(files):
            chosen_file = files[chosen_file_index]
            print(f"Wybrałeś: {chosen_file}")
        else:
            print("Nieprawidłowy numer pliku.")
    except ValueError:
        print("Proszę podać poprawny numer.")

if 'chosen_file' in locals():
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "format=duration", "-of", "csv=p=0", os.path.join(folder_path, chosen_file)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    video_duration = round(float(result.stdout.strip())) + 1
    print(f"Długość filmu: {video_duration} sekund")
else:
    print("Nie wybrano pliku wideo.")

# step 2
text_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.txt')]

print("\nDostępne pliki tekstowe:")
for index, file in enumerate(text_files, 1):
    print(f"{index}. {file}")
    with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
        print(f.read())

try:
    chosen_text_file_index = int(input("Wybierz numer pliku tekstowego: ")) - 1
    if 0 <= chosen_text_file_index < len(text_files):
        chosen_text_file = text_files[chosen_text_file_index]
        print(f"\nWybrano: {chosen_text_file}")
    else:
        print("Nieprawidłowy numer pliku tekstowego.")
except ValueError:
    print("Proszę podać poprawny numer.")
    
# step 3
folder_name = os.path.splitext(chosen_file)[0]
new_folder_path = os.path.join(folder_path, folder_name)

if os.path.exists(new_folder_path):
    print("Folder już istnieje. Przerwanie działania.")
    exit()

os.mkdir(new_folder_path)
print(f"Utworzono folder: {new_folder_path}")

with open(os.path.join(folder_path, chosen_text_file), 'r', encoding='utf-8') as f:
    text_content = f.read().strip()

timestamps = text_content.split()
is_hour_format = any(':' in timestamp and len(timestamp.split(':')[0]) == 2 for timestamp in timestamps)

is_hour_format = False

if is_hour_format:
    timestamps.append(f"{video_duration // 3600:02}:{(video_duration % 3600) // 60:02}:{video_duration % 60:02}")
else:
    if video_duration >= 3600:
        timestamps.append(f"{video_duration // 3600:02}:{(video_duration % 3600) // 60:02}:{video_duration % 60:02}")
    else:
        timestamps.append(f"{video_duration // 60:02}:{video_duration % 60:02}")

# step 4
for i in range(len(timestamps) - 1):
    start = timestamps[i]
    end = timestamps[i + 1]

    output_name = f"{new_folder_path}/segment_{i + 1}-{start.replace(':', '-')}-{end.replace(':', '-')}.mp4"

    command = [
        "ffmpeg", 
        "-i", chosen_file, 
        "-ss", start, 
        "-to", end, 
        "-c", "copy", 
        output_name
    ]

    subprocess.run(command)
    print(f"Stworzono segment: {output_name}")
