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


% persons involved
person(kiyra, female).
person(savita, female).
person(rahul, male).
person(jay, male).
person(nick, male).

% objects found
suspicious_object(savita, gold_chain).
suspicious_object(nick, knife).

% alibis
activity(kiyra, sleeping).
activity(nick, cooking).
activity(jay, watering).
activity(savita, market).
activity(ramu, cleaning).

location(savita, first_floor).
location(kiyra, first_floor).
location(jay, lawn_area).
location(nick, kitchen).
location(ramu, first_floor).

victim(rahul).

% possession of weapon
weapon(savita, knife).
weapon(nick, knife).

% relationships
couple(rahul, kiyra).
affair(rahul, savita).

gift(rahul, savita, gold_chain).
gift(rahul, kiyra, gold_chain).

% Rules
can_have_weapon(X) :- weapon(X, knife).
can_be_on_location(X) :- location(X, first_floor).
can_kill(X) :- activity(X, market).
motive(X) :- affair(rahul, X).
object_found(X) :- gift(rahul, X, gold_chain).
clue(X) :- suspicious_object(X, gold_chain).

% Predicate to identify potential murderers
murderer(X) :-
    can_kill(X),
    motive(X),
    can_have_weapon(X),
    object_found(X),
    can_be_on_location(X),
    clue(X).
