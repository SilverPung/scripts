import  re
import sqlite3

# Sprawozdanie 9 Krzysztof Jósiak 122349
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# funkcje do zadania są odrazu pod właściwym zadaniem


class Scripts:
    def __init__(self):
        self.mail  ='''Cześć,
        Mam nadzieję, że u Was wszystko w porządku. W związku z nadchodzącym spotkaniem
        projektowym chciałem przypomnieć o kilku ważnych kwestiach i uzupełnić dane
        kontaktowe osób, które będą kluczowe w realizacji tego zadania. Poniżej znajdziecie listę:
        Anna Kowalska (Manager): anna.kowalska.manager@googlemail.com
        Tomasz Nowakowski (HR): tomasz.nowakowski.hr@outlook.co.uk
        Piotr Adamski (Sales): piotr.adamski.sales@o2.pl
        Magdalena Wróblewska (IT): magdalena_wroblewska_91@protonmail.com
        Karolina Zielińska (IT): karolina.zielinska.it@icloud.com
        Janusz Trzeciak (Legal): janusz_trzeciak_legal@outlook.com
        Ewa Michalska (Admin): ewa.michalska.admin@wp.pl
        Każdy z wymienionych będzie odpowiadać za swoje obszary, więc w razie potrzeby
        możecie się z nimi kontaktować bezpośrednio.
        Pozdrawiam,
        Mail 2:
        Temat: Aktualizacja kontaktów - nowi członkowie zespołu
        Dzień dobry,
        Z radością informuję, że do naszego zespołu dołączają nowe osoby! Proszę,
        zapoznajcie się z ich danymi kontaktowymi:
        Paweł Kaczmarek (Developer): pawel.kaczmarek.developer@gmail.com
        Monika Majchrzak (Support): monika.majchrzak_support@interia.eu
        Adam Kamiński (CEO): adam.kaminski.ceo@zoho.com
        Barbara Kalinowska (Finance): barbara.kalinowska_finance@o2.co.uk
        Krzysztof Lewandowski (Projects): krzysztof.lewandowski.projects@icloud.com
        Agnieszka Janowska (Marketing): agnieszka.janowska.marketing@google.com
        Mateusz Szpakowski (Lead): mateusz.szpakowski_lead@outlook.com
        Joanna Kowalik (HR): joanna.kowalik.hr@poczta.onet.pl
        Wojciech Nowicki (Ops): wojciech.nowicki_ops@yahoo.com
        Katarzyna Wieczorek (Consultant): katarzyna.wieczorek_consultant@protonmail.ch
        Łukasz Ostrowski (Dev): lukasz.ostrowski.dev@wp.pl
        Marzena Górska (Admin): marzena.gorska.admin@interia.co.uk
        Piotr Krakowski (Analyst): piotr_krakowski_analyst@poczta.pl
        Nowe osoby są już przypisane do projektów i będą wdrażane w najbliższych dniach.
        Proszę, dajcie im czas na zapoznanie się z bieżącymi zadaniami.
        Pozdrawiam,'''
        self.nutrition = nutrition = '''Meat, poultry, & eggs
        Food Portion size Protein amount (g) Calories (kcal)
        Chicken breast 75 g 25 119
        Turkey, roasted 75 g 21 116
        Beef, steak 75 g 20 230
        Beef, lean ground 75 g 22 194
        Hamburger 90 g patty 12 275
        Beef jerky 20 g 7 81
        Pork tenderloin 75 g 21 108
        Pork, lean ground 75 g 19 175
        Ham, cured 75 g 17 124
        Lamb, shank 75 g 21 182
        Egg 1 egg, large 6 78
        Egg whites From 1 egg, large 3 16
        Seafood
        Food Portion size Protein amount (g) Calories (kcal)
        Salmon, baked 75 g 17 155
        Salmon, pink canned 75 g 17 102
        Rainbow trout 75 g 18 127
        Tuna, light canned 75 g 19 87
        Sardines, canned in oil and drained 106 g can 26 220
        Shrimp 30 g, 6 medium 6 30
        Lobster 77 g 16 75
        Scallops 78 g, 6 medium 18 87
        Imitation crab meat 67 g 8 68
        Dairy
        Food Portion size Protein amount (g) Calories (kcal)
        Milk, skim 250 mL 9 88
        Milk, 1% 250 mL 9 108
        Milk, 2% 250 mL 9 129
        Milk, whole 250 mL 8 155
        Nonfat yogurt 175 mL 8 79
        Greek yogurt, plain, 8-12% 175 mL 12 314
        Kefir 175 mL 6 104
        Sour cream, 5% 15 mL 1 21
        Cottage cheese, 1% 125 mL 15 86
        Cream cheese, regular 30 mL 2 103
        Ricotta cheese 125 mL 15 181
        Cheddar cheese 50 g 12 202
        Feta 50 g 7 132
        Parmesan, grated 15 mL 2 27'''

    def zad_1(self):
        """Używając re.sub(), zamień zwrot “sto milionów kelwinów” na “99999727℃”"""
        txt = "Temperatura w trakcie eksplozji osiąga sto milionów kelwinów"
        refactored_txt = re.sub("sto milionów kelwinów", "99999727 ℃", txt)
        print(refactored_txt)

    def zad_2(self):
        """ Dokończ uzupełnianie wzoru wyłapującego adresy email z tekstu. Użyj findall() do
            wydrukowania wszystkich. """

        emails = self.find_emails()
        for email in emails:
            print(email)

    def find_emails(self):
        return re.findall(r'[\w\.-]+@[\w\.-]+', self.mail)

    def zad_3(self):
        """ Dokończ uzupełnianie wzoru wyłapującego adresy email z tekstu. Użyj findall() do
            wydrukowania wszystkich. """
        #załozyłem że dla każdego maila jest przypisana osoba bo dla takich danych było wygodniej bo można to zrobić osobno
        names = re.findall(r'[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+ [A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+', self.mail)
        mails = self.find_emails()
        matches = zip(names, mails)
        
        for match in matches:
            print(f"Osoba: {match[0]}, Email: {match[1]}")

    def zad_4(self):
        """ Korzystając z funkcji re.sub, przekonwertuj daty z formatu '14 lutego 2023' na format '2023-02-
            14'. Użyj słownika do mapowania polskich słów zawierających miesiąc na liczbę. Wydrukuj
            zamieniony tekst na ekran. """
        
        txt = '''Spotkanie odbędzie się 5 stycznia 2021. Kolejne spotkanie zaplanowano na 22 lutego
        2022.
        Projekt ma zostać zakończony 15 marca 2025. Przegląd dokumentacji 9 kwietnia 2024.
        Uroczystość odbędzie się 12 maja 2022, a kolejna 30 czerwca 2024. Wizyta kontrolna
        planowana jest na 21 lipca 2023.
        Start nowego projektu 17 sierpnia 2025. Spotkanie podsumowujące 29 września 2025.
        Rocznica firmy 6 października 2025.'''

        months = {
            "stycznia": "01",
            "lutego": "02",
            "marca": "03",
            "kwietnia": "04",
            "maja": "05",
            "czerwca": "06",
            "lipca": "07",
            "sierpnia": "08",
            "września": "09",
            "października": "10",
            "listopada": "11",
            "grudnia": "12"
        }
        refactored_txt = re.sub(r'(\d{1,2})\s*([a-ząćęłńóśźż]+)\s*(\d{4})', lambda x: f"{x.group(3)}-{months[x.group(2)]}-{x.group(1)}", txt)
        print(refactored_txt)

    def zad_5(self):
        """Przy użyciu funkcji re.sub, przekształć kwoty z formatu '$1,234.56 USD' na '1234.56'. Usuń
            wszystkie znaki oprócz cyfr i kropki."""
        bucks = '''$1,234.56 USD, $987,654.32 USD, $10,000.00 USD, $5,678.90 USD, $123.45 USD,
            $1,000,000.00 USD, $250.00 USD, $3,141.59 USD, $75,000.25 USD, $8.99 USD'''
        refactored_bucks = re.sub(r'[$,A-Z]', '', bucks)
        print(refactored_bucks)

    def zad_6(self):
        """Zanonimizuj ten email: emmet.brown@outatime.com do formatu e***n@outatime.com,
            korzystając z regexu. Weź pod uwagę, że anonimizacja musi działać z innymi mailami w tym
            formacie. Wydrukuj zanonimizowny mail na ekran, a także wzór regex, który został użyty.
        """ 
        email="emmet.brown@outatime.com"
        anonimized_email = re.sub(r'([\w\.-])[\w\.-]+([\w\.-])@', r'\1***\2@', email)
        print(anonimized_email)

    def zad_7(self):
        """Stwórz regex który z poniższego tekstu wyłapuje 4 krupy: nazwę dania, rozmiar porcji, ilość
            białka, kcal. Zauważ, że wielkość porcji zawsze zaczyna się od liczby. Ilość białka to tylko
            liczby, tak samo kcal.
        """
        
        print(self.get_nutrition())

    def get_nutrition(self):
        lines = self.nutrition.split("\n")
        result=[]
        for line in lines:
            line = line.strip().split(" ")
            line.reverse()
            line = " ".join(line)
            output = re.findall(r'([\d]+) ([\d]+) ([\w, ]+ [\d]+) (.+)', line) 
            
            if output:
                kcal, protein, size, name = output[0]
                
                name = name.strip()
                #print(name, sep=" ")
                try: 
                    name = name.split(" ")
                    name.reverse()
                    name = " ".join(name)
                except:
                    print("---"*3+name+"---"*3)
                size = size.split(" ")
                size.reverse()
                size = " ".join(size)
                #print(f"Name: {name}; Size: {size}; Protein: {protein}; Kcal: {kcal}")
                result.append((name, size, protein, kcal))

        return result   

        #naokoło tak , ale działa ;)
        # i nwm czemu jest parmezam w danych jest w mL a nie w g
        # w białkach z jajka nazwa bedzie wychodzić jako egg whites From  ale bierze warunke że wielkośc zaczyna sie liczbą tak jak w poleceniu
                      

    def zad_8(self):
        """ Korzystając z SQLite:
            - Utwórz bazę produktów spożywczych zawierającą: nazwę, rozmiar porcji, ilość białka,
            kcal.
            - dodaj do niej produkty z zadania 7 (jeśli nie masz zrobionego zad6, dodaj kilka ręcznie)
            - Popraw wpis Pork tenderloin tak, by porcja miała 100g (odpowiednio zaktualizuj też
            białko i kcal)
            - Usuń wpis Feta
            - Wyświetl wpisy posortowane po ilości białka
            - Wyświetl najbardziej kaloryczny produkt (w porcji)
            - Wyświetl wszystkie wpisy w bazie """
        self.insert_data()
        self.change_Pork()
        self.delete_feta()
        for row in self.sort_protein():
            print(row)

        print("---"*10)
        print(self.max_calorie())
        print("---"*10)

        for row in self.get_all():
            print(row)
        
    def insert_data(self):
        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE nutrition
            (id int,name text, size text, protein int, kcal int)''')
            #dodałem id z przyzwyczajenia ale nie jest potrzebne w tym przypadku
            i=0
            nutrition = self.get_nutrition()
            for row in nutrition:
                i+=1
                c.execute("INSERT INTO nutrition VALUES (?,?, ?, ?, ?)", (i,row[0],row[1],row[2],row[3]))
                conn.commit()
        except Exception as e:
            print(e)
        conn.close()

    def change_Pork(self):
        #zrobiłem data hardcode specjalnie dla uproszczenia
        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        c.execute("SELECT * FROM nutrition WHERE name='Pork tenderloin'")
        data = list(c.fetchone())     
        data[2]='100 g'
        data[3]='28'
        data[4]='144'
        c.execute("UPDATE nutrition SET size=?, protein=?, kcal=? WHERE name='Pork tenderloin'", (data[2],data[3],data[4]))
        conn.commit()
        conn.close()

    def delete_feta(self):

        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        try:
            c.execute("DELETE FROM nutrition WHERE name='Feta'")
        except Exception as e:
            print(e)
        conn.commit()
        conn.close()

    def sort_protein(self):
        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        c.execute("SELECT * FROM nutrition ORDER BY protein")
        data = c.fetchall()
        conn.close()
        return data

    def max_calorie(self):
        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        c.execute("SELECT * FROM nutrition ORDER BY kcal DESC LIMIT 1")
        data = c.fetchone()
        conn.close()
        return data

    def get_all(self):
        conn = sqlite3.connect('nutrition.db')
        c = conn.cursor()
        c.execute("SELECT * FROM nutrition")
        data = c.fetchall()
        conn.close()
        return data

if __name__ == '__main__':
    s = Scripts()
    s.zad_8()