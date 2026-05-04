from datetime import date
from django.db import models

class Role(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Region(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos_service/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nom

class Profile(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos_profils/', blank=True, null=True)
    services = models.ManyToManyField(Service)
    contact=models.CharField(max_length=11, blank=True, null=True)
    experience=models.CharField(max_length=100, blank=True, null=True, help_text="Description de l'expérience (ex : 6 mois, 2 ans, etc.)")
    clients_satisfaits = models.PositiveIntegerField(default=0,help_text="Nombre de clients satisfaits")
    date_naissance = models.DateField(blank=True,null=True,help_text="Date de naissance")
    facebook_url = models.URLField(max_length=200,blank=True,null=True,help_text="Lien vers le profil Facebook")
    instagram_url = models.URLField(max_length=200,blank=True,null=True,help_text="Lien vers le profil Instagram")
    linkedin_url = models.URLField(max_length=200,blank=True,null=True,help_text="Lien vers le profil LinkedIn")

    def note_moyenne(self):
        evaluations = self.evaluations.all()
        if evaluations.exists():
            return round(sum(e.note for e in evaluations) / evaluations.count(), 1)
        return 0
    def age(self):
        if self.date_naissance is None:
            return None 
        today = date.today()
        age = today.year - self.date_naissance.year
        if (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day):
            age -= 1
        return age

    def __str__(self):
        return f"Profil de {self.utilisateur.nom}"
    

class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    

    def __str__(self):
        return self.titre
class Evaluation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='evaluations')
    client = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role__nom': 'Client'})
    note = models.PositiveSmallIntegerField()  
    commentaire = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Évaluation de {self.profile.utilisateur.nom} - {self.note}/5"