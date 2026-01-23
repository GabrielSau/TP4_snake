# Jeu du snake
Le jeu du snake où il faut manger le plus de nourriture sans se manger la queue et entrer dans les murs.

## Comment lancer le jeu ?
Vous avez deux moyens de jouer,
  - un exécutable est disponible pour permettre un lancement plus rapide du jeu.
  - et sinon directement dans une console en lançant le fichier Main.py avec tous les fichiers dans le même dossier.

## Comment jouer ?
Une fois l’exécutable ou le fichier lancé, le jeu commence directement, pas le temps d’attendre 😁.
Vous êtes le carré vert et il faut manger le carré rouge pour gagner des points. Un score est disponible en haut à gauche de la fenêtre de jeu.

Vous pouvez ensuite vous déplacer avec les flèches (haut, bas, gauche, droite).
Il y a une restriction, le serpent ne peut pas faire demi-tour. S’il va à gauche, vous ne pouvez pas aller à droite directement, la touche est bloquée, pareil pour les autres sens.

Lorsque vous touchez votre propre corps ou un mur, alors vous perdez et un message indiquant « Game Over » s’affiche.
Mais ce n’est pas fini, vous pouvez rejouer en appuyant sur la touche R de votre clavier.

Et enfin, la mise en pause de votre jeu est disponible en appuyant sur la touche P de votre clavier.
Pour reprendre le jeu après la mise en pause, rien de plus simple, rappuyez sur P.

## Réponse aux Questions
  ### 1. Quels sont les rôles respectifs de Snake, Food, Game ?
  #### Snake 
   Responsable du serpent dans le jeu, de sa direction, de sa taille et de sa position, de la gestion des collisions, de la croissance lorsqu’il mange un fruit, et enfin de son propre affichage à l’écran.
      
  #### Food
   Responsable de la nourriture, de sa position aléatoire dans la grille, de sa génération dans la grille, et de son affichage.

  #### Game
   C’est celui qui gère tout, de l’initialisation à la création des différents objets (food, snake), gère les événements ainsi que les update et draw des classes.
   
### 2. Donnez un exemple concret où l'accès direct à snake._body pourrait casser le jeu.
  Si l’accès à snake._body n’était pas protégé, alors n’importe quelle partie du code pourrait le modifier sans qu’il y ait les vérifications prévues pour cette modification.
  Par exemple, si dans le code il y a un snake._body.clear(), alors dans ce cas-là il n’y aurait tout simplement plus de corps pour le serpent et il deviendrait inexistant.

### 3. Expliquez le polymorphisme ici : quelle interface implicite partagent Food/Snake ?
  Food et Snake partagent tous les deux les interfaces update(game) et draw(screen). Cela permet de manipuler les deux classes uniformément sans que celui qui utilise l’interface ait à faire la différence entre les deux entités.

### 4. Pourquoi Food.update() existe alors qu'il ne fait rien ?
  Il a cette méthode pour respecter la même interface que les autres entités.

### 5. Quels éléments de logique sont factorisés grâce à MovingEntity ?
  les éléments de logique factorisés sont : 
    - la gestion de la direction (_dx et _dy)
    - les paramètres de déplacement
    - les méthodes de mouvement
    - la taille de la grille
    - et la vitesse
  Cela évite une duplication de ces logique dans les différentes entités

### 6. Pourquoi CELL_SIZE et DEFAULT_SPEED sont des attributs de classe et pas d'instance ?
  Pour que toutes les entités aient les mêmes valeurs, car si on les met en attributs d’instance, il pourrait y avoir des incohérences (on oublierait de changer une valeur dans une classe).

### 7. Donnez un exemple où set_cell_size() protège le programme (valeurs invalides).
  Car si une personne saisit une valeur invalide pour la taille d’une grille (négative ou nulle), alors set_cell_size filtre et renvoie des erreurs le cas échéant, sans appliquer la valeur.

### 8. Aurait-on pu éviter l'héritage ici ? avantages/inconvénients.
  Oui, on aurait pu ne pas utiliser l’héritage dans ce code, mais il aurait fallu dupliquer certaines parties du code.
  Avec l’héritage, nous avons des liens entre les entités et du polymorphisme, ce qui rend le code plus lisible et maintenable.
  Mais nous avons de fortes dépendances entre les classes (si l’une ne fonctionne pas, rien ne fonctionne), ce qui entraîne une hiérarchie plus rigide.
