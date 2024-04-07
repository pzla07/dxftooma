# dxftooma

# Aplikacja do konwersji DXF do OMA dla optyków

## Opis

Niniejsza aplikacja została stworzona z myślą o optykach i specjalistach zajmujących się produkcją szkieł okularowych. Jej głównym celem jest ułatwienie procesu tworzenia szkieł poprzez automatyzację konwersji rysunków technicznych z formatu DXF (Drawing Exchange Format) do formatu OMA (Optical Manufacturing Association), który jest bezpośrednio gotowy do użycia na maszynach do szlifowania szkieł.

Dzięki temu narzędziu, optycy mogą szybko przekształcić rysunek techniczny w program gotowy do wykorzystania na maszynach produkcyjnych, co znacznie przyspiesza i upraszcza cały proces produkcji.

## Funkcjonalności

- Konwersja plików DXF do formatu OMA.
- Interfejs użytkownika umożliwiający łatwe korzystanie z programu.
- Możliwość modyfikacji i rozbudowy programu przez społeczność.

## Licencja

Program jest dostępny bezpłatnie i może być używany do dowolnych celów, zarówno komercyjnych, jak i niekomercyjnych. Zachęcamy do modyfikowania i rozbudowy aplikacji. Każdy wkład w rozwój projektu jest mile widziany.

## Wsparcie

Jeśli uznasz ten program za przydatny i chciałbyś wesprzeć społeczność, rozważ wsparcie dla biednych dzieci poprzez poniższy link:

https://www.paypal.com/donate?token=3CffS0zQejqONZsiNBDpvH5MhoLv_8V1XELBgpde7T-GaSO3n7qXTiTlu0-rMgB-4U6uix_FptS2yRRs

Twoje wsparcie może zrobić dużą różnicę!

## Jak korzystać

Nasza aplikacja do konwersji DXF do OMA jest prosta w użyciu i została zaprojektowana z myślą o maksymalnej wygodzie użytkownika. Oto krok po kroku, jak można z niej skorzystać:

Przygotuj plik DXF: Upewnij się, że masz gotowy plik DXF, który chcesz przekonwertować.

Wejdź na stronę aplikacji: Otwórz przeglądarkę i przejdź do strony głównej aplikacji. Strona jest responsywna, więc możesz z niej korzystać zarówno na urządzeniach mobilnych, jak i desktopowych.

Wybierz plik DXF: Kliknij na przycisk Select DXF File i wybierz plik DXF z dysku, który chcesz przekonwertować.

Wprowadź informacje o pacjencie: W formularzu wpisz Patient Name, Prescription Number, Date, a także inne wymagane informacje takie jak Lens Type, Lens Material, Surface Treatment i Lens Color.

Konwertuj do OMA: Po wypełnieniu wszystkich pól kliknij przycisk Convert to OMA. Nasza aplikacja przetworzy Twój plik i przygotuje wersję OMA, gotową do użycia na maszynie do szlifowania szkieł.

Pobierz plik OMA: Po zakończeniu konwersji zostaniesz poinformowany za pomocą komunikatu na stronie. Jeśli konwersja zakończy się sukcesem, pojawi się przycisk Download, za pomocą którego możesz pobrać przekonwertowany plik OMA.

Aplikacja została zaprojektowana tak, by była intuicyjna i łatwa w użyciu, nawet jeśli nie masz wcześniejszego doświadczenia z tego typu narzędziami.

## Wkład w projekt

Jeśli chcesz przyczynić się do rozwoju tego projektu, zapraszamy do współpracy! Możesz to zrobić poprzez zgłaszanie błędów, proponowanie nowych funkcji lub bezpośrednie wprowadzanie zmian w kodzie.


Krok 1: Przygotowanie serwera
Zaktualizuj pakiet serwera:
`sudo apt update && sudo apt upgrade -y`

Zainstaluj Pythona 3 i pip:
`sudo apt install python3 python3-pip -y`

Krok 2: Przygotowanie aplikacji
Skopiuj pliki aplikacji na serwer:
Użyj narzędzia do przesyłania plików, np. scp, aby skopiować pliki app.py i inne związane z aplikacją na serwer. Na przykład:

`scp /ścieżka/do/app.py użytkownik@adres_serwera:/ścieżka/na/serwerze`

Powtórz tę operację dla wszystkich niezbędnych plików, w tym szablonów HTML, plików konfiguracyjnych itp.

Zainstaluj wymagane biblioteki:
`flask
pandas
numpy`

# Dodaj inne potrzebne biblioteki
Zainstaluj wymagane biblioteki używając pip:
`pip3 install -r requirements.txt`

Krok 3: Uruchomienie aplikacji
Uruchom aplikację:

W terminalu przejdź do folderu, w którym znajdują się pliki aplikacji. Użyj poniższego polecenia, aby uruchomić aplikację:
`python3 app.py`

Polecenie to uruchomi serwer Flask

Dostęp do aplikacji:
Po uruchomieniu aplikacji powinna być dostępna pod adresem IP serwera na wybranym porcie (domyślnie Flask używa portu 5000). Aby uzyskać dostęp do aplikacji, wpisz w przeglądarce:

`http://adres_serwera:5000`

Dodatkowe uwagi
Jeśli planujesz udostępnić aplikację publicznie, rozważ użycie serwera proxy, np. Nginx, do obsługi ruchu HTTPS i przekierowywania ruchu do aplikacji.
Możesz również skonfigurować firewall (np. ufw) oraz zaktualizować ustawienia bezpieczeństwa serwera, aby zabezpieczyć dostęp do aplikacji.
Do zarządzania aplikacją produkcyjną rozważ użycie narzędzia jak Gunicorn (dla aplikacji Flask/Django) w połączeniu z Nginx jako serwerem proxy.


