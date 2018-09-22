# DEPRECATED

Te repozytorium zostało porzucone ze wględu na złożoność modelu do zaimplementowania.
Nowy serwis Back-End'owy znajduje się [tutaj](https://github.com/inzadrianbury/back-end).

Schemat bazy danych jaki został utworzony przed porzuceniem projektu:
![Schemat bazy danych](https://raw.githubusercontent.com/inzadrianbury/back-end-deprecated/master/schemat.png "Utworzony schemat bazy danych")

## Wymagania
* Python 2.7
* MySQL 7.0.0 

## Łączenie się z bazą MySQL
Aby aplikacja mogła połączyć z bazą danych musi zostać odpowiednio skonfigurowana.
W tym celu należy utworzyć plik o nazwie `db.conf` w katalogu głównym aplikacji.
Przykładowa konfiguracja została zapisana w pliku `db.example.conf`.

## Uruchomienie aplikacji
```bash
$ pip install -r req.txt
$ cd ./src
$ python manager.py migrate
$ python manager.py runserver
```
Aplikacja domyślnie uruchamia się na [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Tworzenie konta administratora
```bash
$ python manager.py createsuperuser
```
Aby zalogować się do aplikacji przejdź na stronę: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
