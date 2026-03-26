# Micro-kernel Architecture

Il faut créer plusiuers plugins qui permettrain d'ajouter différentes fonctionnalités.

Types de plugins :

- **DonjonPlugin** : Plugin qui permet de décrire un donjon. Un donjon est une zone qui contient une liste de monstre à tuer. Chaque monstre contient une liste d'objets que peut récupérer le joueur. Dans un Donjon, il y a au minimum 1 boss. Il peut y avoir plusieurs boss. Il y a obligatoirement un boss à la fin d'un donjon.

- **RaidPlugin** : Plugin qui premet de décrire un raid. Un raid est une très grande zone qui contient un grand nombre de monstres à tuer. Les monstres et les boss dans les raids sont beaucoup plus difficil à tuer que dans des donjons, et ils font beaucoup plus mal aux joueurs. En revanche, il permette au joueurs de récupérer de meilleurs équiepements.

- **StuffPlugin** : Plugin qui permet de mettre à disposition un ensemble d'équipement complet.
Un set d'équipement contient : 

  - Casque (facultatif)
  - Bijou pour Cou (facultatif)
  - Epaules (facultatif)
  - Bras (facultatif)
  - Coudes (facultatif)
  - Mains (facultatif)
  - Bague Droite (facultatif)
  - Bague Gauche (facultatif)
  - Plastron (facultatif)
  - Ceinture (facultatif)
  - Dos - Cape (facultatif)
  - Jambières (facultatif)
  - Chaussures (facultatif)

- **ContinentPlugin** : Plugin qui permet de décrire un continent (un pays). Un continent est composés de plusieurs régions. Une région est composés des plusieurs villes.