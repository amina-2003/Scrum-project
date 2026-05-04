from django.shortcuts import render
from .models import Utilisateur 
from .models import  Service , Profile
import json
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from math import floor


def home(request):
    return render(request, 'home.html')
def listing(request):
    return render(request, 'listing.html')
def contact(request):
    return render(request, 'contact.html')





def recherche_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        service = data.get("service", "")
        region = data.get("region", "")
        search = data.get("search", "")
        
        professionnels = Utilisateur.objects.filter(role__nom='Professionnel')

        if service:
            print(service)
            profils = Profile.objects.filter(services__nom__icontains=service)
            professionnels = Utilisateur.objects.filter(role__nom='Professionnel', profile__in=profils)
        if region:
            professionnels = professionnels.filter(region__nom__icontains=region)
        if search:
            professionnels = professionnels.filter(nom__icontains=search)
    
        professionnels = professionnels.distinct()
        for pro in professionnels:
            try:
                note = pro.profile.note_moyenne() or 0
                pro.stars_full = int(floor(note))
                pro.has_half_star = (note - pro.stars_full) >= 0.5
                pro.stars_empty = 5 - pro.stars_full - (1 if pro.has_half_star else 0)
            except Exception as ex:
                continue
        
        html = render_to_string("partials/resultats.html", {"professionnels": professionnels})
        return JsonResponse({"html": html})

    return JsonResponse({"error": "Requête non autorisée"}, status=400)


def category_view(request, ):
    finition = Service.objects.filter(categorie__nom="finition")
    reparation = Service.objects.filter(categorie__nom="Réparation")
    securite = Service.objects.filter(categorie__nom="Sécurité")
    nettoyage = Service.objects.filter(categorie__nom="Nettoyage")
    demenagement = Service.objects.filter(categorie__nom="Déménagement")
    exterieur = Service.objects.filter(categorie__nom="Extérieur")

    return render(request, 'category.html', {
        'finition': finition,
        'reparation': reparation,
        'securite': securite,
        'nettoyage': nettoyage,
        'demenagement': demenagement,
        'exterieur': exterieur,
    })


@csrf_exempt
def recherche_par_service(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nom_service = data.get("service", "")

        profils = Profile.objects.filter(services__nom__icontains=nom_service).select_related('utilisateur').distinct()
        for profil in profils:
            note = profil.note_moyenne() or 0
            profil.stars_full = int(floor(note))
            profil.has_half_star = (note - profil.stars_full) >= 0.5
            profil.stars_empty = 5 - profil.stars_full - (1 if profil.has_half_star else 0)

        html = render_to_string("partials/professionnels_resultats.html", {"profils": profils})
        return JsonResponse({"html": html})

    return JsonResponse({"error": "Méthode non autorisée"}, status=400)

def profile_detail(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except Profile.DoesNotExist:
        return render(request, 'profile_detail.html', {'error': "Ce profil n'existe pas."})

    return render(request, 'profile_detail.html', {'profile': profile})





