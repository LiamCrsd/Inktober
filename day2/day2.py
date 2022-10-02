from PIL import Image
import math

def a_modif(x,y,syze,epaisseur,theme):
    if theme == "feu" or theme == "eau":
        if y < epaisseur:
            return True
        decalage = ((y-epaisseur)/2)+1
        if decalage <= x <= min(decalage + epaisseur,syze-decalage-1):
            return True
        if max(syze-decalage-epaisseur-1,decalage+1) <= x < syze - decalage:
            return True
    elif theme == "air" or theme == "terre":
        if y < epaisseur:
            return True
        if syze/2 - epaisseur/2 <= y < syze/2 + epaisseur/2:
            return True
        decalage = ((y-epaisseur)/2)+1
        if decalage <= x <= min(decalage + epaisseur,syze-decalage-1):
            return True
        if max(syze-decalage-epaisseur-1,decalage+1) <= x < syze - decalage:
            return True

def ajout_symbole(img,theme):
    data = img.load()
    epaisseur = 4
    symbole_syze = min(int(img.width/5),int(img.height/5))
    if symbole_syze%2 != 0:
        symbole_syze -= 1
    epaisseur = int(symbole_syze/10)+1
    if epaisseur%2 != 0:
        epaisseur -= 1
    for a in range(symbole_syze):
        for b in range(symbole_syze):
            c = int(math.sqrt(img.width*img.height))//15
            if a_modif(a,b,symbole_syze,epaisseur,theme):
                if theme == "feu":
                    case = c + a, c - b + symbole_syze
                    r,g,b = 255,0,0
                elif theme == "terre":
                    case = c + a, c + b
                    r,g,b = 0,255,0
                elif theme == "eau":
                    case = c + a, c + b
                    r,g,b = 0,0,255
                elif theme == "air":
                    case = c + a, c - b + symbole_syze
                    r,g,b = 255,255,255
                data[case] = r,g,b


def modif_image(name,theme,out=None):
    if out == None:
        out = name.split(".")[0] + "_de_" + theme + "." + name.split(".")[1]
    img = Image.open(name)
    data = img.load()
    print("TEST2")
    print(img.width,img.height)
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = data[i,j]
            if theme == "feu":
                r = min(255,r+50)
            elif theme == "terre":
                g = min(255,g+50)
            elif theme == "eau":
                b = min(255,b+50)
            elif theme == "air":
                r = min(255,r+75)
                g = min(255,g+75)
                b = min(255,b+75)
            data[i,j] = r,g,b
    ajout_symbole(img,theme)
    img.save(out)
