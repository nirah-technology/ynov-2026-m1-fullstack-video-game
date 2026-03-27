# TP Microservices : Architecture RPG Distribuée (WoW-Like)

## Contexte
L'objectif de ce TP est de migrer les fonctionnalités de votre moteur RPG (basé sur l'architecture Micro-kernel) vers une architecture Microservices. Nous allons simuler les interactions entre le monde, les instances (Donjons/Raids) et le système d'équipement.

## Objectifs Pédagogiques
1.  **Modularisation** : Chaque microservice doit être un projet Python indépendant géré par **Poetry**.
2.  **Service Registry** : Utiliser **Netflix Eureka** pour permettre aux services de se découvrir dynamiquement.
3.  **Communication Synchrone** : Requêtes REST entre services pour la validation de données.
4.  **Communication Asynchrone** : Design **Event-Driven** pour déclencher des mécaniques de jeu (ex: Loot après un Boss).

## Infrastructure (Docker)
Lancez les services d'infrastructure via Docker :
```bash
# Service Registry (Eureka)
# docker run -d -p 8761:8761 --name eureka-server springcloud/eureka

# Message Broker (RabbitMQ)
docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:3-management-alpine
```

## Travail à réaliser

### Étape 1 : Initialisation des projets Poetry
Vous devez créer 1 projet par service, chacun étant une application Poetry autonome :
- `profile-service` : Responsable de la gestion des profils joueurs.
- `guilde-service` : Responsable de la gestion des guildes.
- `stuff-service` : Responsable de la gestion des équipements.
- `donjons-service` : Responsable de la gestion des donjons.
- `raids-service` : Responsable de la gestion des raids

*Chaque service doit avoir son propre fichier `pyproject.toml` avec les dépendances appropriées (`fastapi`, `uvicorn`, `py-eureka-client`, `pika`).*

### Étape 2 : Service Discovery avec Eureka
1.  Configurez `profile-service` et `guilde-service` pour qu'ils s'enregistrent automatiquement auprès d'Eureka au démarrage.
2.  Dans le `guilde-service`, implémentez la récupération des membres d'une guilde. 
3.  **Contrainte** : Le `guilde-service` ne doit jamais connaître l'adresse IP ou le port du `profile-service` en dur. Il doit utiliser le client Eureka pour appeler l'ID du service (`PROFILE-SERVICE`).

### Étape 3 : Design Événementiel (Event-Driven)
1.  **Producteur** : Modifiez le `profile-service` pour qu'il publie un message dans une queue RabbitMQ nommée `profile.events` à chaque fois qu'un profil est consulté ou modifié.

### Étape 4 : Robustesse et Patterns
1.  **Retry Strategy** : Gérez le cas où le Message Broker n'est pas encore prêt lors du lancement d'un microservice (exception de connexion).
2.  **DTOs Partagés** : Réfléchissez à la manière de partager les schémas de données (DataClasses) entre les services sans créer de couplage fort (copie de code vs package commun).
