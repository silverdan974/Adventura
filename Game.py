import pygame

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur = 400
hauteur = 800
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Background RPG 2D")

# Chargement de l'image du fond
fond = pygame.image.load("background.jpg").convert()

# Fonction pour afficher le fond
def afficher_background():
    fenetre.blit(fond, (0, 0))

# Boucle principale du jeu
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    # Affichage du fond
    afficher_background()

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
