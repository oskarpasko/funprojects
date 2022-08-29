# Concepts

File to create some concepts for new games or just for new projects.

<br /><br />

# Table of Concepts
1. [Try To Get Up](#Try-To-Get-Up)
2. [Taern: Broken Cards](#Taern-Broken-Cards)

<br /><br />

# Try To Get Up

## Description


Głowna postać leci w kierunku prawo/dół pod kątem około 45 stopni cały czas i nie można jej zatrzymać.<br />
Co jakiś czas napotykamy na przeszkody lub na inne dziwactwa które można wykreować.<br />
Gra podobna do Geometry Dash. Można podglądnąć trochę mechanik.<br />

## Mechanics

Główna postać powinna być w kształcie koła i toczyć się w dół.<br />
Pierwszy level niech zawiera tylko momenty w których trzeba coś przeskoczyć.<br />
Gra powinna zawierać przynajmniej na początek 2 poziomy.<br />
W dalesz częście można dodawać nowe poziomy oraz ewentualnie nowe mechaniki.<br /><br />

Genres: Runner, platformer<br />
Language: C#<br />
Engine: Unity2D

<br /><br />

# Taern: Broken Cards

## Description

Karcianka osadzona w świecie gry Taern / Broken Ranks.<br />
Postacie na kartach powinny być takie jak w Taernie (podobne).<br />

## Mechanics

Plansza, na którą każdy gracz może dać Max 5 stronników.<br />
Gracze rzucają kostką na początku gry, kto wyrzuci wyższą liczbę oczek zaczyna.<br />
Jeśli będzie remis rzucamy dopóki ktoś nie wyrzuci więszkej ilości oczek.<br />

### Characters
- Rycerz
  - Ochrona (chroni sojuszniczą kartę przed pierwszym uderzeniem)
  - Rozkaz (+1 do ataku stronnikom)
- Druid 
  - Leczenie (leczy siebie lub karte o 3hp)
  - Leczeie grupowe (leczy wszystkich sojusznikow o 1hp)
- Mag Ognia 
  - Meteor (Zadaje 2dmg obrazenia karcie oraz 1dmg kartom obok wybranej)
  - Ognista tarcza (Zadaje obrazenia bohaterowi lub kartom które zaatakują Maga Ognia)
- Barbarzyńca 
  - AoE (zadaje WSZYSTKIM kartom 1dmg)
  - Furia (daje karcie +2 do ataku na jedna ture)
- Łucznik 
  - Grad (zadaje wszystkim wrogim kartom 1dmg)
  - Trująca (zadaje 1dmg od razu i 1dmg co ture (mozna rzucic tylko na karty))
- VooDoo 
  - Aura Ciebia (zmniejsza obrazenia przeciwnym kartom o 1)
  - Ukaz (usuwa wybraną kartę w następnej turze)
- Sheed 
  - Unik (Bohater jest niewrazliwy na pierwszy atak)
  - Kontrola Oddechu (Zmniejsza koszt kart w ręce)


Genres: Card Game<br />
Language: C#<br />
Engine: Unity2D

<br /><br />
