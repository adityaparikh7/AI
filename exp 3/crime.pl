/*Problem Statement:
A Man is murdered on Sunday. His wife calls the police, who started questioning the wife and
household staff. Murder weapon found was flower vase. Sleeping pills were found in kitchen.
Gold chain was found at murder place.
Members:
1.wife (kiyara)
2.Maid (savita)
3.Sweeper (ramu)
4.Gardner (jay)
5.Cook (nick)
6. victim (rahul)
6.Police
Answers given by the members:
1 wife told that she was sleeping. (was on first floor)
2 Maid told that she had gone to take the post .(was on first floor)
3 Sweeper was cleaning the house.(was on first floor)
4 Gardner was cleaning the house
5 Cook was cooking the breakfast
Facts:
Gold chain was gifted to maid by victim .
Gold chain was also gifted to wife by victim .
Wife was sleeping because she had given sleeping pills.
Maid has gone to market
Gardner was cleaning seen by neighbours.
Cook was making breakfast
Murderer weapon was with both cook and maid.
Maid had an affair with victim
MURDERER – MAID(SAVITA)
Because no markets were open in early morning on Sunday. She was on first floor . She
had motive as she was betrayed by the victim. Suspect object found was gold chain which
was gifted to her by the victim.

*/


female(kiyra).
female(savita).
male(rahul).
male(jay).
male(nick).
suspobj(savita,goldchain).
suspobj(nick,knife).
working(kiyra,sleeping).
working(nick,cooking).
working(jay,watering).
working(savita,market).
working(ramu,cleaning).
victim(rahul).
weapon(savita,knife).
weapon(nick,knife).
location(savita,firstfloor).
location(kiyara,firstfloor).
location(jay,lawnarea).
location(nick,kitchen).
location(ramu,firstfloor).

couple(rahul,kiyara).
affair(rahul,savita).

gift(rahul,savita,goldchain).
gift(rahul,kiyara,goldchain).

canhaveweapon(X):-weapon(X,knife).
canbeonlocation(X):-location(X,firstfloor).
cankill(X):-working(X,market).
motive(X):-affair(rahul,X).
objectfound(X):-gift(rahul,X,goldchain).
clue(X):-suspobj(X,goldchain).
murderer(X):-
cankill(X),motive(X),canhaveweapon(X),objectfound(X),canbeonlocation(X),clue(X).