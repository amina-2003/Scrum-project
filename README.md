# Scrum-Project 
# 🏠 SOS Darek — Plateforme de Recherche de Professionnels

> Plateforme centralisée facilitant la recherche de professionnels liés à l'entretien et à la remise en état d'un logement, avec filtres avancés par métier, disponibilité et proximité géographique.

---

## 📋 Table des matières

- [Contexte & Problématique](#contexte--problématique)
- [Objectifs du projet](#objectifs-du-projet)
- [Équipe Scrum](#équipe-scrum)
- [Organisation Scrum](#organisation-scrum)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Stack technique](#stack-technique)
- [Installation & lancement](#installation--lancement)
- [Structure du projet](#structure-du-projet)
- [Conventions de travail](#conventions-de-travail)
- [Backlog & Suivi](#backlog--suivi)

---

## 🎯 Contexte & Problématique

Le déménagement est une période stressante où l'on a besoin de **services multiples et urgents** sans perdre de temps. Or, il est difficile de trouver rapidement des professionnels fiables réunis au même endroit.

**SOS Darek** répond à ce besoin en proposant une plateforme centralisée permettant de trouver, comparer et contacter rapidement des prestataires qualifiés pour l'entretien et la remise en état d'un logement.

---

## ✅ Objectifs du projet

| # | Objectif |
|---|----------|
| 01 | Mettre à disposition une plateforme intuitive permettant aux utilisateurs de trouver rapidement les contacts de prestataires selon leur besoin |
| 02 | Aider les utilisateurs à comparer facilement les services et choisir l'offre la plus adaptée à leur budget, réduisant ainsi les dépenses inutiles |
| 03 | Intégrer des filtres pour aider l'utilisateur à cibler les professionnels selon leur métier, leur disponibilité et leur proximité géographique |
| 04 | Fournir des fiches claires avec les informations utiles : spécialité, zone d'intervention, téléphone, horaires, avis ou notes si disponibles |

---

## 👥 Équipe Scrum

| Rôle | Nom | Responsabilités |
|------|-----|-----------------|
| 🧭 **Product Owner** | — | Définition du backlog, priorisation des user stories, validation des livrables |
| 🏃 **Scrum Master** | — | Animation des cérémonies Scrum, levée des impediments, garant du processus |
| 💻 **Développeur 1** | — | Frontend — Templates Django, HTML/CSS, filtres de recherche |
| 💻 **Développeur 2** | — | Frontend — Pages profil, responsive design, JavaScript |
| 💻 **Développeur 3** | — | Backend — Modèles, vues, URLs, logique métier |
| 💻 **Développeur 4** | — | Backend — Base de données, authentification, déploiement |

> ℹ️ Remplacez les tirets `—` par les noms réels des membres de l'équipe.

---

## 🔄 Organisation Scrum

### Cadence des sprints

- **Durée d'un sprint :** 2 semaines
- **Sprint actuel :** Sprint 1
- **Nombre total de sprints prévus :** 4

### Cérémonies

| Cérémonie | Fréquence | Durée | Responsable |
|-----------|-----------|-------|-------------|
| **Sprint Planning** | Début de chaque sprint | 2h max | Scrum Master |
| **Daily Standup** | Chaque jour ouvré | 15 min | Scrum Master |
| **Sprint Review** | Fin de chaque sprint | 1h | Product Owner |
| **Sprint Retrospective** | Fin de chaque sprint | 1h | Scrum Master |
| **Backlog Refinement** | Mi-sprint | 1h | Product Owner + équipe |

### Definition of Done (DoD)

Une user story est considérée comme **terminée** lorsque :

- [ ] Le code est écrit et respecte les conventions du projet
- [ ] Les tests unitaires sont rédigés et passent (`python manage.py test`)
- [ ] Une revue de code (pull request) a été effectuée et validée par au moins un autre développeur
- [ ] La fonctionnalité est déployée sur l'environnement de staging
- [ ] La user story est validée par le Product Owner

---

## ✨ Fonctionnalités principales

### MVP (Sprint 1 & 2)

- **Recherche par mots-clés** — recherche full-text sur les noms, spécialités et services
- **Filtres avancés** — métier/spécialité, zone géographique, disponibilité, budget
- **Liste de résultats** — affichage paginé avec tri (pertinence, note, proximité)
- **Fiche professionnel** — spécialité, zone d'intervention, téléphone, horaires, avis
- **Inscription / Connexion** — authentification via `django.contrib.auth`

### Extensions (Sprint 3 & 4)

- **Comparaison de prestataires** — comparer les offres et tarifs côte à côte
- **Favoris** — sauvegarder des profils de prestataires
- **Système de notation et avis** — évaluation post-prestation
- **Tableau de bord professionnel** — gestion de son propre profil et disponibilités
- **Interface d'administration** — gestion des comptes via Django Admin

---

## 🛠 Stack technique

### Backend

- **Langage :** Python 3.11+
- **Framework :** Django 4.x
- **Base de données :** PostgreSQL (ou SQLite en développement)
- **ORM :** Django ORM (intégré)
- **Authentification :** Django Auth + django-allauth
- **Formulaires & validation :** Django Forms / django-crispy-forms

### Frontend

- **Templates :** Django Templates (Jinja2-compatible)
- **Style :** Bootstrap 5 / Tailwind CSS
- **JavaScript :** Vanilla JS (AJAX pour les filtres dynamiques)

### DevOps & Outils

- **Versioning :** Git / GitHub
- **Environnement virtuel :** `venv` / `pipenv`
- **Variables d'environnement :** `python-decouple` / `django-environ`
- **Serveur de développement :** `python manage.py runserver`
- **Hébergement :** (à définir — Railway / Render / PythonAnywhere)
- **Gestion de projet :** Jira / Trello
- **Communication :** Discord / Slack

---

## 🚀 Installation & lancement

### Prérequis

- Python >= 3.11
- pip
- PostgreSQL >= 14 (optionnel en dev, SQLite par défaut)

### Cloner le dépôt

```bash
git clone https://github.com/votre-org/sos-darek.git
cd sos-darek
```

### Créer et activer l'environnement virtuel

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Configuration des variables d'environnement

```bash
cp .env.example .env
```

Renseigner les variables dans `.env` :

```env
SECRET_KEY=votre_secret_django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost:5432/sos_darek
```

### Appliquer les migrations

```bash
python manage.py migrate
```

### Créer un superutilisateur (admin)

```bash
python manage.py createsuperuser
```

### Charger les données de test (optionnel)

```bash
python manage.py loaddata fixtures/initial_data.json
```

### Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000)  
L'interface d'administration est accessible sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

---

## 📐 Conventions de travail

### Branches Git

```
main          → production stable
develop       → intégration continue
feature/xxx   → nouvelle fonctionnalité  (ex: feature/filter-by-location)
fix/xxx       → correction de bug        (ex: fix/search-empty-results)
hotfix/xxx    → correctif urgent sur main
```

### Messages de commit (Conventional Commits)

```
feat: ajout du filtre par zone géographique
fix: correction de l'affichage des fiches professionnels
refactor: restructuration de la vue SearchView
docs: mise à jour du README
test: ajout des tests sur le modèle Professional
```

### Pull Requests

- Toute PR doit cibler la branche `develop`
- Au moins **1 revue** de code requise avant le merge
- Les tests doivent passer : `python manage.py test`
- La PR doit référencer la user story correspondante (ex: `Closes #42`)

### Style de code

- Suivre les conventions **PEP 8**
- Utiliser `flake8` pour le linting
- Nommer les vues en **Class-Based Views (CBV)** de préférence

---

## 📊 Backlog & Suivi

Le backlog produit et le suivi des sprints sont gérés sur :

- 📌 **[Lien vers Jira/Trello]** — Backlog & sprints
- 📊 **[Lien vers le tableau Kanban]** — Suivi en temps réel
- 📁 **[Lien vers Google Drive / Confluence]** — Documentation & specs

---

## 📄 Licence

Ce projet est développé dans un cadre académique / professionnel. Tous droits réservés © 2025 — Équipe SOS Darek.
## 📄 Licence

Ce projet est développé dans un cadre académique / professionnel. Tous droits réservés © 2025 — Équipe SOS Darek.
