import os

# La fonction ci après est récursive, c'est-à-dire qu'elle s'appelle elle même
# Elle affiche les éléments (dossiers ou fichiers) contenus dans le dossier (path)
# passé en paramètre, si c'est un dossier elle s'appelle elle même sur ce dossier pour en afficher
# son contenu et ainsi de suite...
# Le paramètre niveau (par défaut 0) sert à déterminer la profondeur du dossier dans lequel on se trouve
# et à afficher des |_ devant le nom du fichier pour décaler en fonction de la profondeur
def afficheDossier(path, niveau=0):
    elements = os.listdir(path)
    for element in elements:
        if os.path.isdir(os.path.join(path, element)):
            print('|'+'_'*(niveau*2),'Dossier :',element)
            afficheDossier(os.path.join(path, element), niveau+1)
        else:
            print('|'+'_'*(niveau*2), element)

cheminDepart = "C:\\Users\\domin\\OneDrive - Dijon formation\\Documents"

afficheDossier(cheminDepart)