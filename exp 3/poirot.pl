% Suspects
suspect(hercule_poirot).
suspect(jackie_bellefort).
suspect(simon_doyle).
suspect(bouc).
suspect(linnet_ridgeway).
suspect(rosalie).
suspect(dr_linus_windelsham).
suspect(salome).
suspect(marie).
suspect(nurse_bowers).
suspect(andrew).

% Evidence
evidence(necklace, euphemia, bouc).
evidence(gun, nile_river, marie, bloody_handkerchief, scarf).
evidence(abandoned_gun, hercule_poirot).

% Relationships
married(linnet_ridgeway, simon_doyle).
introduced(jackie_bellefort, simon_doyle, linnet_ridgeway).

% Conclusions drawn by Hercule Poirot
killer(simon_doyle, linnet_ridgeway).
mastermind(jackie_bellefort).

% Rules
prime_suspect(X) :- suspect(X), killer(X, _), mastermind(_).

% Task 1: Finding all the suspects
% Use query: suspect(X).
% This will give you a list of all suspects.

% Task 2: Finding all the prime suspects
% Use query: prime_suspect(X).
% This will give you a list of prime suspects.

% Task 3: Finding the killer
% Use query: killer(X, Y).
% This will give you the killer and the victim.
