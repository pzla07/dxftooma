# dxftooma

# Aplikacja do konwersji DXF do OMA dla optyków

![DXF to OMA](https://github.com/pzla07/dxftooma/blob/main/picture.jpg?raw=true)

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


_________________________________________________________________________________________________________________________________________________

dxftooma

DXF to OMA Conversion Application for Opticians

![DXF to OMA](https://github.com/pzla07/dxftooma/blob/main/picture.jpg?raw=true)

Description

This application was created with opticians and eyeglass lens manufacturing specialists in mind. Its main goal is to simplify the lens creation process by automating the conversion of technical drawings from DXF (Drawing Exchange Format) to the OMA (Optical Manufacturing Association) format, which is directly usable on lens grinding machines.

Thanks to this tool, opticians can quickly transform a technical drawing into a program ready for use on production machines, significantly speeding up and simplifying the entire production process.

Features

Conversion of DXF files to the OMA format.
User interface that allows for easy use of the program.
Ability to modify and expand the program by the community.
License

The program is available for free and can be used for any purpose, both commercial and non-commercial. We encourage modifying and expanding the application. Every contribution to the project development is welcome.

Support

If you find this program useful and would like to support the community, consider supporting poor children through the following link:

https://www.paypal.com/donate?token=3CffS0zQejqONZsiNBDpvH5MhoLv_8V1XELBgpde7T-GaSO3n7qXTiTlu0-rMgB-4U6uix_FptS2yRRs

Your support can make a big difference!

How to Use

Our DXF to OMA conversion application is easy to use and designed for maximum user convenience. Here is a step-by-step on how to use it:

Prepare the DXF file: Make sure you have a DXF file ready that you want to convert.

Enter the application page: Open your browser and go to the application's main page. The page is responsive, so you can use it on both mobile and desktop devices.

Select the DXF file: Click the Select DXF File button and choose the DXF file from your disk that you want to convert.

Enter patient information: In the form, enter Patient Name, Prescription Number, Date, and other required information such as Lens Type, Lens Material, Surface Treatment, and Lens Color.

Convert to OMA: After filling all the fields, click the Convert to OMA button. Our application will process your file and prepare the OMA version, ready for use on a lens grinding machine.

Download the OMA file: After the conversion is complete, you will be informed via a message on the page. If the conversion is successful, a Download button will appear, which you can use to download the converted OMA file.

The application has been designed to be intuitive and easy to use, even if you have no previous experience with such tools.

Contributing to the Project

If you want to contribute to the development of this project, we welcome collaboration! You can do so by reporting bugs, suggesting new features, or directly making changes to the code.

Step 1: Server Preparation
Update server packages:
`sudo apt update && sudo apt upgrade -y`

Install Python 3 and pip:
`sudo apt install python3 python3-pip -y`

Step 2: Application Preparation
Copy application files to the server:
Use a file transfer tool, e.g., scp, to copy app.py and other related files to the server. For example:

`scp /path/to/app.py user@server_address:/path/on/server`

Repeat this operation for all necessary files, including HTML templates, configuration files, etc.

Install required libraries:
`flask
pandas
numpy`

Install the required libraries using pip:
`pip3 install -r requirements.txt`

Step 3: Launching the Application
Run the application:

In the terminal, go to the folder where the application files are located. Use the following command to run the application:
`python3 app.py`

This command will launch the Flask server.

Access the application:
Once the application is running, it should be accessible at the server's IP address on the chosen port (by default, Flask uses port 5000). To access the application, type in the browser:

`(http://server_address:5000)`

Additional Notes
If you plan to make the application publicly available, consider using a proxy server, e.g., Nginx, to handle HTTPS traffic and redirect traffic to the application.
You may also want to configure a firewall (e.g., ufw) and update server security settings to secure access to the application.
For managing a production application, consider using a tool like Gunicorn (for Flask/Django applications) in conjunction with Nginx as a proxy server.
