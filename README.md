# Jeu du snake
Le jeu du snake où il faut manger le plus de nourriture sans se manger la queue et rentrer dans les murs.

## Commant lancer le jeu ?
Vous avez deux moyen de jouer, 
  - un exécutable est disponible pour permettre un lancement plus rapide du jeu.
  - Et sinon directement dans une console en lancant le fichier Main.py avec tout les fichier dans le même dossier

## Comment jouer ?
Une fois l'exécutable ou le fichier de lancé, le jeu commence directement, pas le temps d'attendre😁.  
Vous êtes le carré vert et il faut manger le carré rouge pour gagner des points. Un score est disponible en haut à gauche de la fenêtre de jeu.

Vous pouvez ensuite vous déplacer avec les flèches(haut, bas, gauche, droite).  
Il y a une restriction, le serpent ne peut pas faire demi-tour. Si il va à gauche, vous ne pouvez pas aller à droite directement, la touche est bloqué pareil pour les autres sens.

Lorsque vous touchez votre propre corps ou un mur alors vous perdez et un message disant Game Over s'affiche.   
Mais ce n'est pas fini, vous pouvez rejouer en appuyant sur la touche R de votre clavier

Et enfin, la mise en pause de votre jeu est disponible en cliquant sur la touche P de votre clavier.  
Pour reprendre le jeu après la mise en pause, rien de plus simple, rappuyer sur P.

## Réponse aux Questions
  ### 1. Quels sont les rôles respectifs de Snake, Food, Game ?
  #### Snake 
   Responsable du serpent dans le jeu, la direction de celui-ci, la taille et la position, la gestion des collision, la croissance quand il mange un fruit, et enfin son propre affichage à l'écran.
      
  #### Food
   Responsable de la nourriture, sa position aléatoire dans la grille, ça génération dans la grille, et son affichage.

  #### Game
   C'est celui qui gère tout, de l'initialisation à la création des différents objets (food, snake), gère les évènements et les updates et draw des classes.
   
### 2. Donnez un exemple concret où l'accès direct à snake._body pourrait casser le jeu.
  Si l'accès à snake.__body n'était pas privé, alors n'importe qu'elle partie du code pourrait le modifié sans qu'il y est les vérifications faites pour ça modification. 
  Par exemple si dans le code il y a un snake.__body.clear() alors pour ce cas là il n'y aurait tout bonnement plus de corp pour le serpent et il serait donc inexistant.

### 3. Expliquez le polymorphisme ici : quelle interface implicite partagent Food/Snake ?
  Food et Snake partage tout les deux l'interface update(game) et draw(screen). Cela permet de manipuler les deux classes uniformément sans que celui qui utilise l'interface est à faire la différence entre les deux entitées.

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
  Pour que toute les entités ont les mêmes valeurs car si on les mets en attributs d'instance alors il pourrait il y avoir des incohérence (on oublie de changer une valeur dans une classe)

### 7. Donnez un exemple où set_cell_size() protège le programme (valeurs invalides).
  Car si une personne rentre une valeur invalide pour une taille de grille (négative ou null) alors le set_cell_size filtre et renvoi des erreurs si jamais, sans appliquer la valeur

### 8. Aurait-on pu éviter l'héritage ici ? avantages/inconvénients.
  Oui on aurait pu ne pas faire d'héritage dans ce code, mais il aurait fallut dupliquer des parties de code.
  Avec l'héritage, nous avons des liens entre les entités, et un polymorphisme. Avec un code plus lisible et maintenable
  Mais Nous avons de fortes dépendance entre les classes (une qui marche pas rien qui fonctionne) entrainant une hiérarchie plus rigide.
