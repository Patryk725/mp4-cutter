# mp4-cutter

POLSKI README WYGENEROWAŁEM CHATEMGPT!!!

👉 mp4-cutter to bardzo proste narzędzie do przycinania wideo na podstawie ✨specjalnego✨ pliku tekstowego.

<h2>Być może masz kilka pytań. Na przykład:</h2>
<details>
  <summary><h2>Dlaczego to zrobiłeś i kiedy powinienem tego używać?</h2></summary>
  <strong>Zrobiłem to, ponieważ wolę nagrywać długie filmy i dodawać kody czasowe później</strong>. Jeśli pracujesz nad długim wideo, możesz automatycznie przyciąć wszystkie fragmenty na osobne, małe filmy, a następnie <strong>możesz chcieć zrobić krótkie filmy z długich fragmentów wideo</strong>, to narzędzie jest dla Ciebie! To narzędzie pomoże Ci podzielić długi film na mniejsze części.
</details>
<details>
  <summary><h2>Jak to używać?</h2></summary>
  Przede wszystkim <strong>musisz mieć zainstalowane i skonfigurowane <img src="https://img.icons8.com/?size=100&id=32418&format=png&color=000000" width="24" alt="ffmpeg icon"/><u>ffmpeg</u> oraz <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="24" alt="python icon"/><u>python</u> na swoim urządzeniu.</strong>. Następnie potrzebujesz specjalnego pliku tekstowego z kodami czasowymi wideo, który wskaże programowi, jak przycinać wideo. Przykładowa zawartość pliku <code>segments.txt</code>: <code>00:00 02:20 04:24 06:25 08:00</code>.  
  Oto kilka ważnych uwag dotyczących tego, aby Twój plik działał:
  <ul>
    <li>Segmenty muszą być w formacie <code>MM:SS</code> lub <code>HH:MM:SS</code> i oddzielone <b>spacjami</b>.</li>
    <li>Proszę napisać zero przed minutami i sekundami. Nie wiem, czy to ma znaczenie, ale lepiej dmuchać na zimne 😇</li>
    <li>Wszystkie segmenty muszą być w porządku rosnącym, więc nie możesz zapisać czegoś takiego jak: 00:20 04:20 3:20, ponieważ wideo nie może kończyć się przed rozpoczęciem.</li>
  </ul>
  🧐 Nie musisz ustalać końca wideo, ja się tym zająłem, więc jeśli film trwa 5 minut, a Twój ostatni segment jest na 4 minutach - zostanie on przycięty od 04:00 do 05:00
</details>
<details>
  <summary><h2>Co jeśli mam kody czasowe w innym formacie?</h2></summary>
  Załóżmy, że przygotowałeś kody czasowe do 6-minutowego wideo na youtube: <br>
  <pre>
00:00 intro
02:20 czym jest rekurencja
04:40 dlaczego powinienem tego używać
05:50 zakończenie</pre>
  Możesz wykonać następujące kroki, aby je przekonwertować:
  <ol>
    <li>Utwórz i otwórz pusty plik .txt</li>
    <li>Wklej swoje surowe kody czasowe</li>
    <li>Otwórz <code>format.py</code> z mojego repozytorium w tym samym folderze co plik .txt</li>
    <li>Pliki zostaną wyświetlone. Wybierz swój plik z kodami czasowymi używając numerów na klawiaturze.</li>
    <li>Gotowe! Powinno to dać Ci plik w formacie: "{ORIGINAL_FILE_NAME}-timecodesf.txt"</li>
  </ol>
</details>
<details>
  <summary><h2>Mam ✨specjalny✨ plik tekstowy, co teraz?</h2></summary>
  Teraz to najłatwiejsza część. Po prostu otwórz segment.py i znajdź swoje pliki na liście! FFMPEG powinien otworzyć się po wybraniu Twojego ✨specjalnego✨ pliku z kodami czasowymi.
</details>
