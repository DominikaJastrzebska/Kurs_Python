## Generator linków

Program, który służy do obsługi programu partnerskego portalu helion.pl. Przekształca podane linki z portalu w linki dedykowane.
Program pobiera od użytkownika unikalny pięciocyfrowy numer partnera oraz link do przekształcenia. Zapisuje do pliku 
`csv` link podany przez użytkownika i link przekształcony.

#### - Strona główna:  
link podany przez użytkownika: https://helion.pl  
link przekształcony: https://helion.pl/view/12345

#### - Strona produktu - książki  
link podany przez uzytkownika: https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d  <br/>
link przeksztalcony: https://helion.pl/view/12345/algoip

#### - Strona kategorii  
link podany przez użytkownika: https://helion.pl/kategorie/ksiazki/programowanie lub https://helion.pl/kategorie/elektronika  
link przekształcony: https://helion.pl/12345/page/kategorie/programowanie

#### - Strona zakupów
link podany przez użytkownika: https://helion.pl/zakupy/edit.cgi
link przekształcony: https://helion.pl/add/12345
