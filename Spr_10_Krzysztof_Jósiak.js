/*
Sprawozdanie 10 Krzysztof Jósiak 122349
Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać numer zadania
gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
polecenie zadania jest na początku każdej funkcji tak jak pan prosił
funkcje do zadania są odrazu we właściwej funkcji
*/


function zad_1(){
    /* Stwórz dwie zmienne zawierające jakieś liczby, trzeciej zmiennej nadaj wynik mnożenia tych
    zmiennych. Zmodyfikuj program “Hello World” tak, by wyświetlał zawartość trzeciej zmiennej. */
    var a = 5;
    var b =10;
    var c = b*a;
    console.log(c);

}

function zad_2(){
    /* Popraw nazwy zmiennych tak, by były zgodne z konwencją:
    var 1wszySamochod = ‘Polonez’;
    var ImieNazwisko = ‘Jan Kowalski’;
    var var = ‘Opel’;
    var samochod bonda = ‘Aston Martin’; */

    var pierwszySamochod = 'Polonez';
    var imieNazwisko = 'Jan Kowalski';
    var samochod = 'Opel';
    var samochodBonda = 'Aston Martin';
    
}

function zad_3(){
    /* Zainicjuj zmienną str, umieść w niej tekst ““Pan Wołodyjowski” przedstawia losy pana Michała –
    najlepszej szabli Rzeczpospolitej.”. Znajdź metody i przypisz do nowych zmiennych ich wartość:
    - długość tego stringu
    - index pierwszego wystąpienia słowa ‘szabli’
    - zwróć słowo ‘szabli’ przypisując je do nowej zmiennej
    - zwróć słowo ‘Rzeczypospolitej’ licząc od końca zdania.
    - zamień słowo ‘najlepszej’ na ‘pierwszej
    */
    var text = "\"Pan Wołodyjowski\" przedstawia losy pana Michała –najlepszej szabli Rzeczpospolitej.";
    
    var length = text.length;
    console.log(length);

    var firstSword = text.indexOf("szabli");
    console.log(firstSword);

    var sword = text.slice(firstSword, firstSword+6);
    console.log(sword);

    var rzeczpospolita = text.slice(-16, -1);
    console.log(rzeczpospolita);

    var newText = text.replace("najlepszej", "pierwszej");
    console.log(newText);


}


function zad_4(){
    /* Napisz program, który podzieli powyższy ciąg na słowa i zwróci zmienną z tymi słowami w
        odwrotnej kolejności. Na końcu niech alert(); wyświetli wynik. */
    var str = "Turków. przez Podolskiego Kamieńca przejęcie i Oblężenie";
    var tab = str.split(" ");
    var revTab = tab.reverse();
    var revStr = revTab.join(" ");
    console.log(revStr);

}

function zad_5(){
    /* Napisz program, który konwertuje temperaturę podaną w kelwinach na temperaturę
        w fahrenheitach. W tym celu:
        - zainicjuj zmienną = 301.
        - Temperatura w celsjuszach to kelwiny - 273.15.
        - Temperatura w fahrenheitach to 9/5tych + 32 temperatury w celsjuszach.
        - Wynik zaokrąglij w dół. Niech wynik końcowy pojawia się w alert(); */
    var tempK = 301;

    var tempC = tempK - 273.15;

    var tempF = Math.floor((9/5)*tempC + 32);

    console.log(Math.floor(tempC))
    console.log(tempF);


}


function zad_6(){
    /* - Stwórz obiekt ‘samochod’,
        - nadaj mu właściwości: marka (string), mocSilnika (int),
        - Poza deklaracją obiektu zmień wartość mocSilnika na 300.
        - Zwróć wartość mocSilnika z obektu samochod poprzez alert(); korzystając z notacji
        kropkowej. */
    var car = {
        marka: "BMW",
        mocSilnika : 200

    }
    console.log(car.mocSilnika);

    car.mocSilnika = 300;

    console.log(car.mocSilnika);
}

function zad_7(){
    /* - Stwórz funkcję konstruującą obiekt student(imie, nazwisko, stypendium).
        - Stwórz 3 obiekty student korzystając z tej funkcji.
        - Zmień nazwisko trzeciego obiektu na ‘Kowalski’.
        - Wyświetl imię i nazwisko trzeciego obiektu przy pomocy alert(); */
    function Student(imie,nazwisko,stypendium){
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.stypendium = stypendium;
    }

    var student1 = new Student("Jan", "Kowalski", 1000);
    var student2 = new Student("Adam, Nowak", 2000);
    var student3 = new Student("Piotr", "Kowal", 500);

    student3.nazwisko="Kowalski";
    console.log("Student 3: " + student3.imie + " " + student3.nazwisko);
}


function zad_9(day){
    /* Stwórz funkcję, która zwraca ile kalorii zostało zjedzone w dany dzień tygodnia (Np.
        2500 w Poniedziałek), określając 7 różnych warunków.
        - Dzień tygodnia podaj jako argument funkcji.
        - Zwróconą wartość podaj w alert(); */
    switch(day.toLowerCase()){
        case 'poniedziałek':
            console.log("2500");
            break;

        case 'wtorek':
            console.log("3000");
            break;
        
        case 'środa':
            console.log("2000");
            break;

        case 'czwartek':
            console.log("2100");
            break;

        case 'piątek':
            console.log("1800");
            break;
        
        case 'sobota':
            console.log("3500");
            break;

        case 'niedziela':
            console.log("3200");
            break;

        default:
            console.error("Nie ma takiego dnia tygodnia");
            break;
    }
}

function zad_10(){
    /* Napisz kod do gry w papier / nożyce / kamień.
        - Funkcja przyjmuje typ obu graczy, zwraca wygranego gracza lub ‘remis’, jeśli typ był taki
        sam.
        - Napisz osobną funkcję walidującą czy podane wartości to kamień, nożyce lub papier.
        Dane od użytkownika uzyskasz kodem:
        prompt("Podaj pierwszy typ - kamień, nożyce, papier?");
        - Wynik gry niech będzie podawany w alert(); */
    var player1 = prompt("Gracz 1: Podaj kamień, papier lub nożyce");
    var player2 = prompt("Gracz 2: Podaj kamień, papier lub nożyce");

    var result = determineWinner(player1, player2)
    
    if (result == undefined){
        console.error("Błąd");
    }
    if (result == "Remis"){
        console.log("Remis");
    }
    else{
        console.log("Wygrał: " + result);
    }
    // walidacja jest w tej samej fukcji co wybór zwycięzcy
    function determineWinner(player1, player2){

        
        if (player1 != "kamień" && player1 != "papier" && player1 != "nożyce"){
            console.error("Gracz 1 podał złą wartość");
            return;
        }
        if (player2 != "kamień" && player2 != "papier" && player2 != "nożyce"){
            console.error("Gracz 2 podał złą wartość");
            return;
        }
        
        
        if(player1 == player2){
            return "Remis";
        }
        else if(player1 == "kamień" && player2 == "nożyce" || player1 == "nożyce" && player2 == "papier" || player1 == "papier" && player2 == "kamień"){
            return "Gracz 1";
        }
        else{
            return "Gracz 2";
        }

    }
}
