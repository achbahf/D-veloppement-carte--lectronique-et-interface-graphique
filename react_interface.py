import tkMessageBox #module creant des pop up
import ezodf as e #module utilepour la gestion desdocuments libreoffice
import subprocess	#permet de lancer des commandes via python (ie sans passer par le terminal)
import Tkinter as tk #module d'interfaphe graphique
import tkFont #gestion de la police du texte
import math #module pour les fonctions telles que cos,sin, pi...
import datetime #gestion de variables type 'date' 
import time #gestion du temps 
import matplotlib.pyplot as plt #utile pour tracer les coubes de temps
import serial #communication arduino
import tkFileDialog #affichage des dossiers pour l'usb

#Texte pour les boutons radios
NewPlayer='En vous inscrivant vous pourrez enregistrer vos informations \n et acceder aux precedents scores'
PlayerIdentification='En vous identifiant vous pourrez enregistrer vos arddatass\net acceder aux precedentes scores'
Anonyme='Etes-vous sur de vouloir continuer sans vous identifier?'
NewCoach='En vous identifiant vous pourrez enregistrer vos informations \net acceder aux informations des joueurs'
CoachIdentification='En vous inscrivant vous pourrez acceder aux informations des joueurs '
TabInfo=[PlayerIdentification, NewPlayer, Anonyme]
#----------------------------------------------Creation du desktop--------------------------------------------------------------

#__________________________Arret du Raspberry__________________________
#fonction d'extinction : utilisable par un bouton quand l'alimentation du raspberry sera autonome
def eteindre():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE) #envoie de la commande sur le tube
    output = process.communicate()[0] #"output" ie sortie de la commande
    print (output)
    
#______________________________Affichage du desktop__________________________________________   

desktop=tk.Tk() # objet Tkinter "support" de tous les autres objets
screenWidth, screenHeight = desktop.winfo_screenwidth(), desktop.winfo_screenheight() #calcul des dimensions maximales d'affichage possibles
#desktop.overrideredirect(1)#supprime la barre de tache
desktop.attributes('-fullscreen', True) #objet tkinter "Desktop" avec les dimensions maximales 

bgim=tk.PhotoImage(file="img/bg.png") #importation de l'image de fond totalement opaque de taille de "desktop"
background=tk.Label(desktop, image=bgim, padx=0,pady=0) #label pour l'affichage de l'image de fond de "desktop"
background.grid(padx=0,pady=0) #affichage de l'image de fond de "desktop"
#shutdownB=tk.Button(desktop, text= 'Eteindre', command=eteindre) ##bouton appelant la fonction eteindre: utile si utilisation de la fonction "eteindre" (voir commentaire de la fonction)
#shutdownBwidth= BoutonEteindre.winfo_reqwidth() ##affiche du bouton : utile si utilisation de la fonction "eteindre" (voir commentaire de la fonction)
#x = (screenWidth-LargeBoutonEteindre) #calcul de la position du centre du background
#BoutonEteindre.grid(padx=x,pady=0)#padx: Distance entre le bord gauche du bouton et le bord droit de root // pady: Distance entre le bord haut du bouton et le bord haut de root
##ExBouton=tk.Button(desktop, text= 's', command=quit)
##ExBouton.grid()

#-----------------------------Fin Affichage du desktop ---------------------------


#___________________________Definition polices du texte __________________________________________  


myFont = tkFont.Font(family=' KacstDecorative',weight='bold', size=8) #police primaire
myFont2 = tkFont.Font(family=' KacstDecorative',size=7) #police secondaire
myFontB=tkFont.Font(family=' KacstDecorative',weight='bold', size=10) #police des boutons
titlefont=tkFont.Font(family='OpenSymbol',weight='bold', size=18)#police des titres de "topbandL" (voir plus bas)
myFontdatebold=tkFont.Font(family='Arial Black', weight='bold',size=8) #pour un des labels de la "mainpage"
myFontdate=tkFont.Font(family='Arial Black', size=8)#pour un des labels de la "mainpage"
myfont=tkFont.Font(family='Noto Sans CJK TC', size=6) #texte "discret"
#---------------------------Fin definition polices d'ecriture-------------------------

###___________________________ Importation de TOUTES images_________________________________________  
led1im=tk.PhotoImage(file="img/led1.png")
led2im=tk.PhotoImage(file="img/led2.png")
led3im=tk.PhotoImage(file="img/led3.png")
led4im=tk.PhotoImage(file="img/led4.png")
led5im=tk.PhotoImage(file="img/led5.png")
led6im=tk.PhotoImage(file="img/led6.png")
led7im=tk.PhotoImage(file="img/led7.png")
led8im=tk.PhotoImage(file="img/led8.png")
led9im=tk.PhotoImage(file="img/led9.png")
led10im=tk.PhotoImage(file="img/led10.png")
led11im=tk.PhotoImage(file="img/led11.png")
led12im=tk.PhotoImage(file="img/led12.png")
led13im=tk.PhotoImage(file="img/led13.png")
led14im=tk.PhotoImage(file="img/led14.png")
led15im=tk.PhotoImage(file="img/led15.png")
ledlim=tk.PhotoImage(file="img/ledl.png")
ledrim=tk.PhotoImage(file="img/ledr.png")
leddim=tk.PhotoImage(file="img/ledd.png")
ledtim=tk.PhotoImage(file="img/ledt.png")
lediim=tk.PhotoImage(file="img/ledi.png")
ledeim=tk.PhotoImage(file="img/react.png")
ledfim=tk.PhotoImage(file="img/ledf.png")

ledim=[led1im, led2im,led3im,led4im,led5im,led6im,led7im,led8im,led9im,led10im,led11im,led12im,led13im,led14im,led15im]

feetim=tk.PhotoImage(file="img/react.png")
nofeetim=tk.PhotoImage(file="img/nofeet.png")
redledim=tk.PhotoImage(file='img/redl.png')

lledim=tk.PhotoImage(file='img/ledl.png')
rledim=tk.PhotoImage(file='img/ledr.png')
tledim=tk.PhotoImage(file='img/ledt.png')
dledim=tk.PhotoImage(file='img/ledd.png')

im=tk.PhotoImage(file="img/oreoleV.png")
im2=tk.PhotoImage(file="img/1rond.png")
bandim=tk.PhotoImage(file="img/ensiame.png")
bg1im=tk.PhotoImage(file="img/bg1.png")
bgledim=tk.PhotoImage(file="img/bg1.png")

frames = [tk.PhotoImage(file='img/countdown.gif',format = 'gif -index %i' %(i)) for i in range(57)]

#---------------------------Fin importation images-------------------------

#___________________________Definition variables globales__________________________________________
##________variables de gestion de la date
global now # global => variable globale
nowtime = datetime.datetime.now() #date du jour
datenow=nowtime.strftime("%d-%m-%Y") #format de la date

##________variables de gestion de fichiers
global doc 
doc = e.opendoc("BaseDeDonnee.ods") #ouverture du fichier
global sheet
sheet=doc.sheets["Dernieres Donnees"] #feuille calc "Dernieres Donnees" de "BaseDeDonnee.ods" contenant la liste des joueurs et les derniers scores
global nrows 
nrows=tk.IntVar() #Entier tkinter utilisable par les objets tkinter
nrows.set(sheet.nrows()-1) #nombre de lignes du tableau de de la feuille "sheet" <=> nombre d'inscrits
global sheet1
sheet1=doc.sheets["Parametres"]  #feuille calc contenant les moyens d'identifications !!!!

global playerrow #numero de ligne correspondant au joueur s'inscrivant/s'identifiant
playerrow=tk.IntVar()

##________variables de gestion des donnees du joueur
global vName #nom du joueur inscrit lors de l'inscription/l'identification
vName=tk.StringVar() #
#vName.set("Saisir le nom")
global vSurname #prenom du joueur inscrit lors de l'inscription/l'identification
vSurname=tk.StringVar()
#vSurname.set("Saisir le prenom")
global vLog #pseudo du joueur inscrit lors de l'inscription/l'identification
vLog=tk.StringVar()
#vLog.set("Saisir le pseudo")
global vPr #statut du joueur (entraineur ou joueur)
vPr=tk.StringVar()
global vPassw #mot de passe du joueur
vPassw= tk.StringVar()
#vPassw.set("Saisir le mot de passe")
global vPasswConf #confirmation du mot de passe (seulement pour l'inscription))
vPasswConf=tk.StringVar()
global tapedPssw #mot de passe inscrit pendant l'identification/la demande du mot de passe administrateur
tapedPssw=tk.StringVar()

##________variables de gestion des fenetres 
global vWindow #numerote les pages
vWindow=tk.IntVar()
vWindow.set(0) 
#vWindow=
#4 =>Accueil
#1 => NouveauMembre
#11=>createfile()
#0 => Identification
#2 => ChoixMode
#3 => mdpAdmin
#31 => mainparameters
#32 => psswsetting
#5 => stayCo
#6 => Main
global windowwidth #la fenetre garde les memes dimensions
windowwidth=tk.IntVar()
windowwidth.set(screenHeight/2)

##________variables de gestion des parametre
global vIdparams
vIdparams=tk.IntVar() #mode d'identification : vIdparam=1 => nom/prenom, vIdparam=2 => pseudo/mot de passe, vIdparam=3 => seulement pseudo
if str((sheet1[1,0].value)=="nom"):
	vIdparams.set(1)
if str((sheet1[1,0].value)=="mdp"): 
	vIdparams.set(2)
else: 
	vIdparams.set(3)
global vCoach #variable pour la distinction joueur/entraineur vCoach=1 => distinction, vCoach=0 => pas de distinction
vCoach=tk.IntVar()
global vAdm #variable pour la demande de mdp admin vAdm=1 => oui, vAdm=0 => non
vAdm=tk.IntVar()
#est-ce que le statut d'entraineurs existe
if str((sheet1[1,1].value)=="oui"):#oui : joueur!=entraineur
    vCoach.set(1)
else: #non : pas de statut d'entraineur
    vCoach.set(0)
#demande du mot de passe administrateur ?
global adminPssw #mot de passe administrateur
adminPssw=tk.StringVar() #Chaine de caractere tkinter utilisable par les objets tkinter
if str((sheet1[1,2].value)=="oui"):#oui
    vAdm.set(1)
    adminPssw.set(doc.sheets["Mdp Administrateur"][1,1].value)
else:
    adminPssw.set(0) #non
    vAdm.set(0)

#---------------------------Fin definition variables globales------------------------- 

def toPDF():
    filename.set(str(vSurname.get())+"_"+str(vName.get())+"_"+str(vLog.get()))
    command = "unoconv -f pdf "+(filename.get())+".pdf "+(filename.get())+".ods" #conversion du fichier openoffice calc (le tableau du joueur) en pdf
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print (output)
    filename.set(filename.get()+".pdf")#Fichier a copier
    print( str(vSurname.get()),vSurname.get(),filename.get(),str(filename.get()))
    desktop.filename = tkFileDialog.asksaveasfilename(initialdir = "/media/pi",initialfile=filename.get(),title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))

##    askusbname()
####def askusbname ():
####    global vUSB
####    global USBF
####    vUSB=tk.StringVar()
####    USBF=tk.Frame(desktop,bg='#fff3f3')
####    USBF.grid()
####    (USBL,USBE)=makeentry(USBF,'Veuillez rentrer le nom de votre cle usb',1,1,2,font=myFont,bg='#fff3f3', textvariable=vUSB)
####    OKB=tk.Button(USBF, text='ok', command=copytousb)
####    OKB.grid()
####    USBF.place(x=screenWidth/2-(USBL.winfo_reqwidth()+USBE.winfo_reqwidth())/2,y=screenHeight/2-USBL.winfo_reqheight()/2-OKB.winfo_reqheight()/2)
##
##def copytousb ():
##    desktop.filename = tkFileDialog.asksaveasfilename(initialdir = "/media/pi",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    #USBF.destroy()
    #command = "sudo cp "+(filename.get())+" /media/pi/"+str(vUSB.get()) #copie vers USB
##    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
##    output = process.communicate()[0]
##    print (output)
##    command = "pdftoppm "+filename.get()+ " figtodel-png -rx 90 -ry 90 -f 1 -singlefile" #conversion  pdftoppm Courbe_de_LMLM.pdf todel -f 1 -singlefile
##    tableim=tk.PhotoImage(file="figtodel-png.ppm")#recuperation du tableau
##    tableL=tk.Label(exportF, text='Doc sur cle')
##    tableL.grid()
##    OK1B=tk.Button(exportF, text='OK',command=quit)
##    OK1B.grid()
##    exportF.place(x=50,y=topband.winfo_reqheight())
##vled1=tk.IntVar()
def ledchoice():
    global vled1
    vled1=tk.IntVar()
    global vled2
    vled2=tk.IntVar()
    global vled3
    vled3=tk.IntVar()
    global vled4
    vled4=tk.IntVar()
    global vled5
    vled5=tk.IntVar()
    global vled6
    vled6=tk.IntVar()
    global vled7
    vled7=tk.IntVar()
    global vled8
    vled8=tk.IntVar()
    global vled9
    vled9=tk.IntVar()
    global vled10
    vled10=tk.IntVar()
    global vled11
    vled11=tk.IntVar()
    global vled12
    vled12=tk.IntVar()
    global vled13
    vled13=tk.IntVar()
    global vled14
    vled14=tk.IntVar()
    global vled15
    vled15=tk.IntVar()
    global vledl
    vledg=tk.IntVar()
    global vledr
    vledg=tk.IntVar()
    global vledt
    vledg=tk.IntVar()
    global vledd
    vledg=tk.IntVar()
    global vled 
    vled=tk.IntVar()
    ledtable=[vled1,vled2,vled3,vled4,vled5,vled6,vled7,vled8,vled9,vled10,vled11,vled12,vled13,vled14,vled15, vledl, vledr, vledt, vledd]
#global vfig
#vfig=tk.IntVar()
#vfig.set(var)
#creation fenetre pour choix des leds
    global exportF
    exportF=tk.Frame(desktop,bg='#fff3f3')
    exportF.grid()
    def selectall(): #cochage de allled
        if vled.get()==1: # "checkbutton" "toutes les leds" actif
            allled.config(text='Aucune led') #changement de texte
            for widget in  exportF.winfo_children():
                if widget.winfo_class()=='Checkbutton':
                    widget.select()
        else: # "checkbutton" "toutes les leds non actif
            allled.config(text='Toutes les leds') #changement de texte
            for widget in  exportF.winfo_children():
                if widget.winfo_class()=='Checkbutton':
                    widget.deselect()
    
    def ledSel ():
        if sum(ledtable)!=19:
            allled.deselect()
    
    def ledchoiceOK():       
        for widget in exportF.winfo_children():
            widget.destroy()
        plotfigure()
    
        
    allled=tk.Checkbutton(exportF,font=myFont,bg='#fff', text='Toutes les leds', variable=vled,command=selectall)
    allled.grid(row=3,columnspan=5)
    #initialisation de variables pour positionnement de la fenetre
    xim=0
    yim=0
    xCB=0
    yCB=0
    for i in range(15): #un "checkbutton" et une image par led
        CB=tk.Checkbutton(exportF,font=myFont,bg='#fff',text='Led'+str(i),variable=ledtable[i],command=ledSel)
        CB.grid(row=(i)%3, column=2*(i//3))
        label=tk.Label(exportF,highlightbackground='black',font=myFont,bg='#fff3f3',image=ledim[i])
        label.grid(row=(i)%3, column=(1+2*(i//3)),pady=10)
        xim=max(CB.winfo_reqwidth(),xim)
        xCB=max(label.winfo_reqwidth(),xCB)
        yim=max(CB.winfo_reqheight(),yim)
        yCB=max(label.winfo_reqheight(),yCB)
    #un "checkbutton" et une image pour les leds du haut, du bas, de gauche et de droite
    CB=tk.Checkbutton(exportF,font=myFont, text="Leds de gauches", command=ledSel)
    CB.grid(row=0, column=11)
    label=tk.Label(exportF,highlightbackground='black',font=myFont,bg='#fff3f3',image=lledim)
    label.grid(row=0,column=12)
    tk.Checkbutton(exportF,font=myFont, text="Leds de droites",command=ledSel).grid(row=1, column=11)
    tk.Label(exportF,highlightbackground='black',font=myFont,bg='#fff3f3',image=rledim).grid(row=1,column=12)
    tk.Checkbutton(exportF,font=myFont, text="Leds du haut",command=ledSel).grid(row=2, column=11)
    tk.Label(exportF,highlightbackground='black',font=myFont,bg='#fff3f3',image=tledim).grid(row=2,column=12)
    tk.Checkbutton(exportF,font=myFont, text="Leds du bas",command=ledSel).grid(row=3, column=11)
    tk.Label(exportF,highlightbackground='black',font=myFont,bg='#fff3f3',image=dledim).grid(row=3,column=12)
    
    tk.Button(exportF,font=myFont,bg='#fff3f3',text='Valider', command=ledchoiceOK ).grid()
    x=screenWidth/2-5*(xCB+xim)/2-(label.winfo_reqwidth()+CB.winfo_reqwidth())/2
    y=screenHeight/2-3*max(yCB,yim)/2-allled.winfo_reqheight()/2
    exportF.place(x=x,y=y)
def displayfigure ():
    ledchoice(1)
def exportfigure ():
    ledchoice(0)			


def plotfigure():
##    for widget in exportF.winfo_children():
##	widget.destroy()
    #vledStorage=[vled1.get(),vled2.get(),vled3.get(),vled4.get(),vled5.get(),vled6.get(),vled7.get(),vled8.get(),vled9.get(), vled10.get(), vled11.get(), vled12.get(),vled13.get(), vled14.get(), vled15.get()]
    ledtime=[]
    N=[k for k in range (1, nplayerrows.get()+1)]
    compt=0
    for j in range (0, 14):
	if ledtable[j]==1:#vledStorage[j]==1:
	    compt=compt+1
	    ledtime.append([])
	    for i in range(1, nplayerrows.get()+1): 
		ledtime[compt-1].append(playersheet[i, 13+j].value) #scores sur la led j lors du ieme entrainement
		print (playersheet[i, 13+j].value,N)
	    plt.plot(N,ledtime[compt-1])
    #adaptation du titre de la courbe
    if compt>1:
	s='s'
    elif compt==1:
	s=''

    filename.set('Courbe'+str(s)+'_de_'+str(vSurname.get())+'_'+str(vName.get())+'.pdf')#Fichier a copier
    plt.savefig(filename.get()) #enregistrement courbe
    toPDF()
#if vfig.get()==1:
#	Showfigure()

def Showfigure ():
    print(filename.get(),str(filename.get()))
    command = "pdftoppm "+filename.get()+ " figtodel-png -rx 90 -ry 90 -f 1 -singlefile" #conversion  pdftoppm Courbe_de_LMLM.pdf todel -f 1 -singlefile
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print (output)
    figim=tk.PhotoImage(file='figtodel-png.ppm')
    showfigureL=tk.Label(exportF, image=figim,bg='#fff3f3')	
    showfigureL.place(x=0, y=0, relwidth=1, relheight=1)
    showfigureL.grid()
    #tk.Button(exportF,text="Copier vers l'usb",font=myFont, bg='#fff3f3',command='').grid()
    tk.Button(exportF,text="ok",font=myFont, bg='#fff3f3',command=quit).grid() #close supprime le fichier str(filename)
def Mainparams ():
    mdpAdmin(31)
#__________________________________Definition Fenetres__________________________________________  

#Cree une frame encadree de la couleur de highlightbackground et highlightcolor donc highlightcolor=highlightbackground
def bordercolor (master, highlightbackground, highlightcolor, highlightthickness=None, width=None, height=None, bd=None):
    frame = tk.Frame(master, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, width=width, height=height, bd= bd)
    frame.grid()
    return frame

Fenetre=bordercolor(desktop,'#000','#000',3,(screenWidth),screenHeight/2,0)

#creation du borderau du haut	
global topbandF
global topbandL	
global topband		
topbandF=tk.Frame(desktop,bg='#000',name='topband') #borderau du haut
topbandF.grid()
topbandF.place(x=0,y=0) #placement du borderau du haut
topband=tk.Label(topbandF,image=bandim,bg='#000') #logo ENSIAME
topband.grid(ipadx=(screenWidth/2-topband.winfo_reqwidth()/2))
topband.config(anchor=tk.W)
topbandL=tk.Label(topbandF,text='Bienvenue',font=titlefont,foreground='#fff3f3',bg='black')
topbandL.grid()

global keyboardF #fenetre du clavier virtuel
keyboardF=tk.Frame(desktop,bg='white')
#-----------------------------------Fin definition Fenetres---------------------------------

#__________________________________Creation menu__________________________________________ 
menubar = tk.Menu(desktop,bg='black',fg='white',bd=0,font=myFont,activeforeground='black',activebackground='#fff3f3')
filemenu=tk.Menu(menubar,tearoff=0,bg='black',fg='white',font=myFont)
filemenu.add_command(label="Exporter votre tableau", font=myFont,command=toPDF,state=tk.DISABLED)
filemenu.add_command(label="Exporter votre courbe", font=myFont,command=ledchoice,state=tk.DISABLED)
#filemenu.add_command(label="Afficher un tableau", command=quit)
#filemenu.add_command(label="Afficher une courbe", font=myfont,command=displayfigure)
menubar.add_cascade(label="Fichier", menu=filemenu)
optionmenu=tk.Menu(menubar,bg='black',fg='white',font=myFont)
optionmenu.add_command(label="Parametres generaux", font=myFont,command=Mainparams,state=tk.DISABLED)
optionmenu.add_command(label="Parametres de mon profil", font=myFont,command=quit,state=tk.DISABLED)
othermembers=optionmenu.add_command(label="Parametres du profil de ...", font=myFont,command=quit,state=tk.DISABLED)
optionmenu.add_command(label="Mots de passes", font=myFont,command=quit,state=tk.DISABLED)

menubar.add_cascade(label="Options", menu=optionmenu)
print(screenWidth,screenHeight,'dim scrreen')

class Accueil:
    def __init__(self):
	#boucle detruisant tous les objets enfants de 'Fenetre' sauf le fond d'ecran
	for widget in Fenetre.winfo_children():
            if widget.winfo_name()!= 'backg':
                widget.destroy()
	self.background_label = tk.Label(Fenetre, name='backg', image=bg1im) #image de fond de "Fenetre"
	self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
	
	self.LabelInfo=tk.Label(Fenetre,width=60,font=myFont2,anchor=tk.W,justify=tk.LEFT,text=TabInfo[0],bg='#fff3f3')
	#Choix identification ou non
        global RBheight #la hauteur des labels de l'objet "Nouveau Membre"=fonction de la hauteur des boutons radio de l'objet "Accueil" 
	global okpadx #les boutons ok restent de meme largeur
	global y0 #la fenetre maintenue a la hauteur y0

	topbandL.config(text='Bienvenue') #configuration du texte du borderau du haut
	topbandL.grid()
	#placement du texte du borderau
	xtopband=(screenWidth-topband.winfo_reqheight())/2
	ytopband=(topband.winfo_reqheight()-topband.winfo_reqheight())/2
	topbandL.place(x=xtopband,y=ytopband)
	
	#choix identification, inscription ou anonyme avec les boutons radios 
	self.BoutonRadioIdentification= tk.Radiobutton(Fenetre,variable=vWindow,font=myFont , text="Deja membre: Sidentifier", value=0,height=3,width=34,command= self.Selection,anchor=tk.W,activeforeground='#cb6397',bg='#fff3f3',activebackground='#fff3f3',pady=0,padx=0,relief=tk.FLAT)
	self.BoutonRadioNouveauMembre= tk.Radiobutton(Fenetre,variable=vWindow,font=myFont ,text="Nouveau membre: Creer un compte", value=1,height=3,width=34, command= self.Selection,anchor=tk.W,activeforeground='#cb6397',bg='#fff3f3',activebackground='#fff3f3',pady=0,padx=0)
	self.BoutonRadioAnonyme= tk.Radiobutton(Fenetre,variable=vWindow,value=2,font=myFont ,text="Continuer sans s'identifier",height=3, width=34, command= self.Selection,anchor=tk.W,activeforeground='#cb6397',bg='#fff3f3',activebackground='#fff3f3',pady=0,padx=0)
	self.BoutonRadioIdentification.grid(row=1,column=0,columnspan=2,sticky=tk.W,pady=5)
	self.BoutonRadioNouveauMembre.grid(row=2,column=0,columnspan=2,sticky=tk.W,pady=5)
	self.BoutonRadioAnonyme.grid(row=3, columnspan=2,column=0,sticky=tk.W,pady=5) 
	        
	self.BoutonOK=tk.Button(Fenetre,highlightbackground='#003333', foreground='#003333',text="Valider", command=self.OK, font=myFontB,  bg='#fff3f3', height=2) #"height"=hauteur du bouton en ligne de texte
       #placement de la fenetre  
	xFenetre=15+ self.LabelInfo.winfo_reqwidth()+max(self.BoutonRadioAnonyme.winfo_reqwidth(),self.BoutonRadioNouveauMembre.winfo_reqwidth(), self.BoutonRadioIdentification.winfo_reqwidth(), self.BoutonOK.winfo_reqwidth())
	yFenetre=self.BoutonRadioAnonyme.winfo_reqheight()+self.BoutonRadioIdentification.winfo_reqheight()+self.BoutonRadioNouveauMembre.winfo_reqheight()+ self.BoutonOK.winfo_reqheight()
	y0=(screenHeight-(yFenetre+self.BoutonOK.winfo_reqheight()))/2
	ipady=(self.BoutonRadioIdentification.winfo_reqheight()-self.LabelInfo.winfo_reqheight())/2
	Fenetre.place(x=0,y=y0)
#placement du bouton valider 
	okpadx=self.BoutonOK.winfo_reqheight()/4
	xok=(xFenetre-self.BoutonOK.winfo_reqwidth())/2		
	self.BoutonOK.grid(column=0,columnspan=3,row=6, sticky=tk.W,ipadx=okpadx,padx=xok,pady =20)
##dimensionnement et placement de LabelInfo
	self.LabelInfo.config(padx=16)
	self.LabelInfo.grid(row=1,column=2,columnspan=1, sticky=tk.W,ipady=ipady, pady=6)
        RBheight=self.LabelInfo.winfo_reqheight()
        windowwidth.set(self.BoutonRadioNouveauMembre.winfo_reqwidth()+self.LabelInfo.winfo_reqwidth())
    def Selection(self):
	self.LabelInfo.grid_remove() #option d'affichage en memoire
	self.LabelInfo.config(text=TabInfo[vWindow.get()])#,font=myFont2,bg='#fff3f3',anchor=tk.W,justify=tk.LEFT, padx=15 )
	ipady=(self.BoutonRadioIdentification.winfo_reqheight()-self.LabelInfo.winfo_reqheight())/2
	self.LabelInfo.grid(row=vWindow.get()+1,ipady=ipady, pady=5)#,column=2,columnspan=1)#,sticky=tk.W
	ir=0
	#couleur du texte des boutons radios
	for widget in Fenetre.winfo_children():
	    if widget.winfo_class()=='Radiobutton':
		if vWindow.get()==ir:
		    widget.config(foreground='#993366')
		else:
		    widget.config(foreground='black')
		ir=ir+1
    def OK(self):
	Fenetre.grid_propagate(0) #fixe la taille de la fenetre pour le changement de page
	if vWindow.get()==1:
	    id=NouveauMembre()
	if vWindow.get()==0:
	    id=Identification()
	elif vWindow.get()==2 :
	    Fenetre.destroy()
     	    id=ChoixMode()
     	    
class mainparameters:
    def __init__(self):
        global newfile
        newfile=tk.IntVar()
        global paramsF
        paramsF=bordercolor(desktop, '#000', '#000', width=screenWidth, height=screenHeight) #nouvelle fenetre
        paramsF.config(bg='#fff3f3')#couleur du fond
        paramsF.place(x=0,y=100)
        self.admCB=tk.Checkbutton(paramsF,bg='#fff3f3', text="Demander le mot de passe administrateur",font=myFont, variable=vAdm,anchor='w')
        tk.Label(paramsF,bg='#fff3f3', text="L'administrateur defini le statut d'entraineur", font=myfont,anchor='w').grid(row=2,column=1) #information sur le choix fait avec "admCB"
        
        self.coachCB=tk.Checkbutton(paramsF,bg='#fff3f3', text="Distinguer entraineur et joueur", variable=vCoach, command=self.coach,font=myFont)
        tk.Label(paramsF, bg='#fff3f3',text="L'entraineur a acces aux donnees de tous les joueurs",font=myFont).grid(row=1, column=1)#information sur le choix fait avec "coachprofilCB"
        
        tk.Checkbutton(paramsF,text='Nouveau document',bg='#fff3f3',variable=newfile).grid(column=2)
        
        self.identificationparamsL=tk.Label(paramsF, bg='#fff3f3',text="Souhaitez-vous vous identifier par :", font = myFont)
        self.identificationparamsL.grid()
        self.nameidentificationRB=tk.Radiobutton(paramsF,bg='#fff3f3', text="Nom et Prenom", value=1,width=22, variable=vIdparams)
        self.nameidentificationRB.grid()
        self.psswidentificationRB=tk.Radiobutton(paramsF,bg='#fff3f3', text="Pseudo et mdp", value=2,width=22, variable=vIdparams)
        self.psswidentificationRB.grid()
        self.pseudoidentificationRB=tk.Radiobutton(paramsF, bg='#fff3f3',text="uniquement par pseudo", width=22, value=3, variable=vIdparams)
        self.pseudoidentificationRB.grid()
        
        self.coachCB.grid(row=1,column=0)
##        self.coachinfoL.grid(row=2)
        self.admCB.grid(row=2,column=0)
##        self.admL.grid(row=6)
        
        tk.Button(paramsF,text='Valider',highlightbackground='#003333', foreground='#003333', command=self.OKparams, font=myFontB,  bg='#fff3f3', height=2).grid()

    def coach(self):
        if vCoach.get()==1:
            self.psswidentificationRB.config(state=tk.NORMAL)
        else:         
            self.psswidentificationRB.config(state=tk.DISABLED)  
    def OKparams(self):
        for widget in paramsF.winfo_children():
            widget.destroy()
        if newfile.get()==1:
            filename="BaseDeDonnee"+str(datenow)+".ods"
            command = "sudo cp /home/pi/Desktop/REACT/BaseDeDonnee.ods /home/pi/Desktop/REACT/archives/"+filename  #copie vers USB du fichier calc de reference
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            print (output)
        if vIdparams.get()==1:
            sheet1[1,0].set_value('nom')
        elif vIdparams.get()==2:
            sheet1[1,0].set_value('mdp')
        else:
            sheet1[1,0].set_value('pseudo')
            
        if vCoach.get()==0:
            sheet1[1,1].set_value('non')
            
        else:
            sheet1[1,1].set_value('oui')            
        if vAdm.get()==0:           
            sheet1[1,2].set_value('non')
        else:
            sheet1[1,2].set_value('oui')
        doc.save() #enregistrement des modifications       
        tk.Label(paramsF,bg='#fff3f3',text='Voulez-vous changer de mot de passe administrateur?').grid()
        tk.Button(paramsF,bg='#fff3f3',text='oui',command=self.paramsok).grid()
        tk.Button(paramsF,bg='#fff3f3',text='non',command=self.paramsend).grid()
        
    def paramsok(self):
        psswsetting()
        paramsF.destroy()
    def paramsend (self):
        paramsF.destroy()
    

class psswsetting:
    def __init__(self):
        global psswF
        psswF=tk.Frame(desktop, bg='#fff3f3',width=screenWidth,height=screenHeight)
    
        psswF.grid()
        tk.Button(psswF, text='valider', font=myFontB,height=3,bg='white', command=self.psswsettingOK).grid()
        (self.admpsswL, self.admpsswE)=makeentry(psswF,'Choisissez un mdp aministrateur',1,0,1,Labelwidth=30, width=30, bg='white',textvariable=adminPssw)

        psswF.place(x=screenWidth/2-self.admpsswL.winfo_reqwidth()/2-self.admpsswL.winfo_reqwidth()/2,y=y0)
    def psswsettingOK (self):
        psswF.destroy()
	if doc.sheets['Mdp Administrateur'][1,1].value==None:
        	doc.sheets['Mdp Administrateur'][1,0].set_value(1)
	else:
     		doc.sheets['Mdp Administrateur'][1,0].set_value(doc.sheets['Mdp Administrateur'][0,1].value-1)
        doc.sheets['Mdp Administrateur'][1,1].set_value(adminPssw.get())
        doc.sheets['Mdp Administrateur'][1,2].set_value(datenow)
        doc.save()#enregistrement du fichier global           
        
class NouveauMembre:
    def __init__(self):
	for widget in Fenetre.winfo_children():
            if widget.winfo_name()!= 'backg':
                widget.destroy()
	global iPr #variable definissant le profile : joueur(0) ou coach(1)
	iPr=tk.IntVar()#par defaut : nouveau membre=joueur
	vPassw.set('le mot de passe doit contenir au moins 5 caracteres')

	#Creation des labels et zones de texte "Nom" et "Prenom"abs
	idpadx=windowwidth.get()/2
	(self.nameL,self.nameE)=makeentry(Fenetre, "Nom", 1,0,2,tk.W, 28,width=None,font=myFont2,bg='#fff3f3',justify=tk.LEFT,ipadx=idpadx, textvariable=vName)
       # self.EntreeNom.grid(column=1,row=1,columnspan=2)
	(self.surnameL,self.surnameE)=makeentry(Fenetre,"Prenom", 2,0,2,tk.W,28, width=None,font=myFont2,bg='#fff3f3',justify=tk.LEFT,ipadx=idpadx, textvariable=vSurname)
       # self.EntreePrenom.grid(column=1,row=2,columnspan=2)
	(self.logL, self.logE)=makeentry(Fenetre,"Pseudo",3,0,2,tk.W,28, width=None,font=myFont2,bg='#fff3f3',justify=tk.LEFT, ipadx=idpadx,textvariable=vLog)
	(self.psswL,self.psswE)=makeentry(Fenetre,"Mot de Passe",4,0,2,tk.W,28,width=None,font=myFont2,bg='#fff3f3',justify=tk.LEFT, ipadx=idpadx,textvariable=vPassw)
	(self.confPsswL,self.confPsswE)=makeentry(Fenetre,"Confirmation du mot de passe ",5,0, 2,tk.W,28,width=None, font=myFont2 , bg='#fff3f3', justify=tk.LEFT,ipadx=idpadx, textvariable = vPasswConf)
	
	self.coachCB=tk.Checkbutton(Fenetre,state=tk.DISABLED, text='Entraineur',font=myFont,bg='#fff3f3',anchor=tk.W ,variable=iPr, highlightthickness=0,padx=2)#command=self.CoachSelected,
	self.coachCB.grid(row=6,column=0,pady=2)

	self.BoutonOK=tk.Button(Fenetre,font=myFontB,  text="Valider",command=self.AjoutMembre,height=2,padx=okpadx,highlightbackground='#003333', foreground='#003333',  bg='#fff3f3')
	self.BoutonOK.grid(row=7,column=0, pady =20)
	
	self.BoutonRetour=tk.Button(Fenetre,font=myFontB, text="retour",command=self.BackNM,height=2,highlightbackground='#003333', foreground='#003333',  bg='#fff3f3')

	self.BoutonRetour.grid(row=7,column=2, pady=20)
	Backpadx=(2*okpadx+self.BoutonOK.winfo_reqwidth()-self.BoutonRetour.winfo_reqwidth())/2
	self.BoutonRetour.config(padx=Backpadx)

	self.nameE.focus_set()
	self.nameE.icursor(tk.END)
	if vCoach.get()==1: #le statut de coach existe si vCoach=1 =>activation "coachCB"
            self.coachCB.config(state=tk.NORMAL)
	Fenetre.place(x=0,y=topband.winfo_reqheight()+15)
    def BackNM (self):
        Accueil()
        keyboardF.destroy()
	    
    def AjoutMembre (self):
        keyboardF.destroy()
        if (vLog.get()!="" and vSurname.get()!="" and vName.get()!="" and vPassw.get()!=""  ):
            ncols=sheet.ncols() #Nombre de datas ou numero de colonne
            row=1
	    print('nrows',nrows.get())
	    npseudo=0
	    while (row<nrows.get()+1):
		if vLog.get()==sheet[row,3].value:
		    npseudo=npseudo+1
		row=row+1
	    print(('vPassw',vPassw.get()))
	    if npseudo==0:#condition a supprimer mettre if vLog.get()==sheet[row,3].value:makewarining("Pseudo existant","Veuillez vous connecter ou changer de pseudo", 2, "Choisir un autre pseudo",0, "S'identifier",1) 
	        if len(vPassw.get())>4:
	            if (vPasswConf.get()==vPassw.get()):
                        
                        desktop.attributes('-fullscreen', True)
                        if iPr.get()==0:           
                            vPr.set('joueur')
                            createfile()           
                        else:
                            vPr.set('entraineur')
                            mdpAdmin(11,1)#prochaine fenetre, fenetre de retour		
		    else:
		        tkMessageBox.showwarning("mdp incorrect","confirmation mdp incorrect")
		        self.confPsswE.focus_force()
		        self.confPsswE.select_range(0, 15)
		        self.confPsswE.icursor(tk.END)
	        else:
		    tkMessageBox.showwarning("mdp incorrect","mdp trop court")
                    self.psswE.icursor(tk.END)
            else:
                tkMessageBox.showwarning("Pseudo existant","Veuillez vous connecter ou changer de pseudo")
                self.logE.select_range(0, 15)
                self.logE.icursor(tk.END)
                
        else: 
            tkMessageBox.showwarning("informations manquantes","Saisir toutes les infos")
            self.psswE.icursor(tk.END)
            
class createfile:
    def __init__(self):	
	for widget in Fenetre.winfo_children():
            if widget.winfo_name()!= 'backg':
                widget.destroy()
        sheet.append_rows(1) #ajout d'une ligne a la fin du tableau pour le nouveau membre
        playerrow.set(nrows.get()+1) 
        nrows.set(playerrow.get())#Nouveau nombre de membre
        ncols=(playerrow.get())#Nouveau nombre de membre
        sheet[nrows.get(),0].set_value(nrows.get()) #Affectation d'un nombre a chaque membre
        
        filename=vName.get()+"_"+vSurname.get()+"_"+vLog.get()
        command = "sudo cp filetocopy.ods "+filename+".ods"  #copie vers USB du fichier calc de reference
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print (output)
        
        playerdoc=e.opendoc(filename+".ods")
        playersheet = playerdoc.sheets['sheet'] #nom de la feuille copiee        
        playersheet.name = name="Donnees de "+ filename
        playerdoc.save()

        sheet[nrows.get(),1].set_value(vName.get())
        sheet[nrows.get(),2].set_value(vSurname.get())
        sheet[nrows.get(),3].set_value(vLog.get())
        sheet[nrows.get(),4].set_value(vPassw.get())
        sheet[nrows.get(),5].set_value(vPr.get())
        sheet[nrows.get(),6].set_value(datenow)
        doc.save()
	    
        stayCo() 
		
class Identification:
    def __init__(self):
        global v1
	global v2
	global v3
	global id1Ltextvariable
	global id2Ltextvariable		
	#Fenetre.grid_propagate(False)
	for widget in Fenetre.winfo_children():
            if widget.winfo_name()!= 'backg':
                widget.destroy()
        vPassw.set('')
	#Creation de deux zones de texte "Nom" et "Prenom"/"Pseudo" "mdp" ou d'une zone de texte "Pseudo"
	if vIdparams.get()==2:#ligne et col a changer selon le doc calc
	    id1Ltext='Pseudo'
	    v1=3#colonne de doc correspondant au pseudo
	    id2Ltext='Mot de passe'
	    id1Ltextvariable=vLog
	    id2Ltextvariable=vPassw
	    v2=4#colonne de doc correspondant au mdp
	elif vIdparams.get()==1:#ligne et col a changer selon le doc calc
	    id1Ltext='Nom'
	    id2Ltext='Prenom'
	    id1Ltextvariable=vName
	    id2Ltextvariable=vSurname
	    v1=2#colonne de doc correspondant au NOM
	    V2=1#colonne de doc correspondant au prenom
	else: 
	    id1Ltext='Pseudo'
    	    id1Ltextvariable=vLog
	    v1=3#colonne de doc correspondant au pseudo
        idpadx=windowwidth.get()/2
        
	if vIdparams.get()!=3: #Cas avec deux labels
            idpady=(3*RBheight+30)/2
	    (self.id2L,self.id2E)=makeentry(Fenetre, id2Ltext, 2, 0, 2, font=myFont,bg='#fff3f3',Labelwidth=15,ipadx=idpadx , pady=idpady, textvariable=id2Ltextvariable)
        else:
            idpady=(3*RBheight+30)
	(self.id1L,self.id1E)=makeentry(Fenetre, id1Ltext, 1, 0, 2,ipadx=idpadx , pady=idpady, font=myFont,bg='#fff3f3',Labelwidth=15, textvariable=id1Ltextvariable)


	self.BoutonOKId=tk.Button(Fenetre, text="Valider",anchor=tk.W,font=myFontB,bg='#fff3f3', padx=okpadx, command=self.RechercheMembre, height=2)
	self.BoutonOKId.grid(row=4,column=0,pady=20)
	self.BoutonRetourId=tk.Button(Fenetre, text="Retour",font=myFontB,bg='#fff3f3', command=self.Backid, height=2)
	backpadx=(2*okpadx+self.BoutonOKId.winfo_reqwidth()-self.BoutonRetourId.winfo_reqwidth())/2
	self.BoutonRetourId.grid(row=4,column=2,pady=20)

	self.BoutonRetourId.config(padx=backpadx)
	x=max( self.id1L.winfo_reqwidth()+self.id1E.winfo_reqwidth(),(self.BoutonOKId.winfo_reqwidth() + self.BoutonRetourId.winfo_reqwidth()))
	y=max(self.id1L.winfo_reqheight(),self.id1E.winfo_reqheight())+max(self.BoutonRetourId.winfo_reqheight(),self.BoutonOKId.winfo_reqheight())	
	x1=(screenWidth-x)/2
	y1=(screenHeight-y)/2
	
	self.id1E.focus_set()
	self.id1E.icursor(tk.END)
        
	Fenetre.place(x=0,y=topband.winfo_reqheight()+15)

    def RechercheMembre(self):
	keyboardF.destroy() #suppression du clavier virtuel
	Compt=0 #verifie le nombre de joueur avec meme nom et prenom
	row=1 #variable utilisee pour trouver la ligne du joueur "nplayerrow"
	Table=[]#stock les valeurs de row pour lesquelles id1Ltextvariable ET id2Ltextvariable correspondant a la base de donnees
	print('nrow',nrows.get())
	while (row<nrows.get()+1):
	    if str(sheet[row,v1].value)==id1Ltextvariable.get():
                
	        if vIdparams.get()!=3:
		    if str(sheet[row,v2].value)==id2Ltextvariable.get():
		        Compt=Compt+1
			Table.append(row)	
		    row=row+1
		else:
		    #sinon mode d'endentification par pseudo => 1 seule valeurs a verifier et le pseudo est unique donc fin verification
                    Table.append(row)
		    row=nrows.get()	+1
		    Compt=Compt+1
	    else:
		row=row+1
        if Compt==0:
            tkMessageBox.showwarning("Erreur d'identification", "Membre non trouve") #WARNING!!
        elif Compt==1:

            playerrow.set(Table[0])
            print(Table[0],playerrow.get(),'table et tt')
            vName.set(sheet[playerrow.get(),2].value)
            vSurname.set(sheet[playerrow.get(),1].value)
            vLog.set(sheet[playerrow.get(),3].value)
            playerdef()
        else:  #Identification par pseudo car plusieurs membres avec meme nom ET meme prenom
                #Aficher warningwindow "plusieurs membres ont le meme nom et prenom veuillez indiquer votre pseudo
            tkMessageBox.showwarning("Veuillez indiquer votre pseudo","plusieurs membres ont le meme nom et prenom veuillez indiquer votre pseudo")
            (self.idLogL,self.idLogE)=makeentry(Fenetre, 'Pseudo', 3,0, 1, font=myFont,bg='#fff3f3',Labelwidth=50, textvariable=vLog)
            #self.idLogE.force_focus()
            self.IdLogE.icursor(tk.END)
            for i in Table:
                if str(sheet[i, 3].value)==vLog.get():
                    playerrow.set(i)
                    vName.set(sheet[playerrow.get(),2].value)
                    vSurname.set(sheet[playerrow.get(),1].value)
                    vLog.set(sheet[playerrow.get(),3].value)
                    playerdef()		
    def Backid (self):
	keyboardF.destroy() #suppression du clavier virtuel
        Accueil()
def playerdef():
        name= vName.get()+"_"+vSurname.get()+"_"+vLog.get()+".ods"
        global playersheet
        global playerdoc
        global nplayerrows
        nplayerrows=tk.IntVar()
        playerdoc=e.opendoc(str(name))
        playersheet=playerdoc.sheets["Donnees de "+vName.get()+"_"+vSurname.get()+"_"+vLog.get()]
        nplayerrows.set(playersheet.nrows()-2) #-1 pour la premiere ligne et -1 pour la derniere avec les moyennes
        print(nplayerrows.get(),'playerrows')
        id=main()
        
class mdpAdmin: #demande du mot de passe administrateur
    def __init__(self, vFuturwindow):
	global pssw
	pssw=tk.StringVar()
        if vAdm.get()==0: #si mdp administrateur non demande, aucune fenetre non affichee
            self.AdmGoto(vFuturwindow)
        else:
            psswaskedF=tk.Frame(desktop, bg='white')
	    self.background_label = tk.Label(psswaskedF, name='backg', image=bg1im) #image de fond de "psswaskedF"
	    self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bgadm = tk.Label(psswaskedF, image=bg1im)
            self.bgadm.place(x=0, y=0, relwidth=1, relheight=1)
            makeentry(psswaskedF, "mot de passe administrateur",1,0,1,textvariable=tapedPssw)	

	tk.Button(psswaskedF, text="OK",command=self.mdpConf).grid(row=2,column=1)	
	tk.Button(psswaskedF,text="retour",command=self.admGoto).grid(row=2,column=2)#vers NouveauMembre
    def mdpConf(self): #mot de passe correct ?
	keyboardF.destroy() #suppression du clavier virtuel
	if (str(tapedPssw.get())==adminPssw.get()): 
	    othermembers.config(state=tk.NORMAL)
	    vPr.set('entraineur')
	    psswaskedF.destroy()
	    if vFuturwindow==11:
                createfile()
            if vFuturwindow==31:
                mainparams()               
            elif vFuturwindow==32:
                psswsetting()
	    
	else:
	    tkMessageBox.showwarning("mdp incorrect","mdp incorrect")
            tapedPssw.focus_force()
            tapedPssw.icursor(tk.END)
            
    def admGoto (self):
	keyboardF.destroy() #suppression du clavier virtuel
        psswaskedF.destroy()
	NouveauMembre()

class stayCo:
    def __init__(self):
	for widget in Fenetre.winfo_children():
            if widget.winfo_name()!= 'backg':
                widget.destroy()
	topbandL.config(text='Que voulez-vous faire?')
	xtopband=(screenWidth-topband.winfo_reqheight())/2
	ytopband=(topband.winfo_reqheight()-topband.winfo_reqheight())/2
	topbandL.place(x=xtopband,y=ytopband)
	tk.Label(Fenetre, height=3,text="Voulez-vous continuer avec le compte de "+ vLog.get()+"?").grid(row=0,column=0,columnspan=2,pady=10)
	tk.Button(Fenetre, text="Oui",height=3, command=self.mainpage).grid(row=1,column=0)
	tk.Button(Fenetre, text="Non",height=3,command=self.backStCo).grid(row=1,column=1)
    def mainpage(self ):
        playerdef()
    def backStCo (self):
	Accueil()

class main:
    def __init__(self):
        global ledC
	ledC=tk.Canvas(desktop,height=screenHeight,width=screenWidth)
	ledC.coords(0, 0,screenWidth,screenHeight)		
	idF= bordercolor (desktop, '#fff',  '#fff')
	dataF=bordercolor (desktop, '#fff',  '#fff')
	idF.config(bg='white')
	dataF.config(bg='white')
	self.bgmainL = tk.Label(desktop, image=bgledim)
	
	topbandL.config(text='A vous de jouer !')
	xtopband=(screenWidth-topband.winfo_reqheight())/2
	ytopband=(topband.winfo_reqheight()-topband.winfo_reqheight())/2
	topbandL.place(x=xtopband,y=ytopband)

	col=sheet.ncols()
		
	registrationDate=(sheet[playerrow.get(),6]).value
	idtext=str(vSurname.get()) +' '+ str(vName.get())+ '\n Pseudo : '+str(vLog.get())+' \n Membre depuis le : '+str(registrationDate)
	self.playerInfoL=tk.Label(idF, text=idtext, bg='#fff',font=myFont,width=25)
	ledC.create_window(0,0 , window=idF)
	idF.place(x=0,y=topband.winfo_reqheight())

	meanTime=str((sheet[playerrow.get(),7]).value)
        print (meanTime,playerrow.get(),'playerrow')
	if meanTime!='0' and meanTime!='None':
	    i=1
    	    number=int((sheet[playerrow.get(),22]).value)
	    lastDate=str((sheet[playerrow.get(),21]).value)
	    min=int((sheet[playerrow.get(),8]).value)
	    max=int((sheet[playerrow.get(),9]).value)
	    feet=str((sheet[playerrow.get(),10]).value)
    	    pro=str((sheet[playerrow.get(),11]).value)
	    ledr=str((sheet[playerrow.get(),12]).value)
	    time=str((sheet[playerrow.get(),13]).value)

	    datetext="Dernier entrainement:\nle : "+str(lastDate)
	    self.dateL=tk.Label(dataF,text=datetext,font=myFontdate,bg='black', foreground='white')

	    timetext="Temps Moyen : "+str(meanTime) 
	    self.lasttimeL=tk.Label(dataF,bg='#fff',text=timetext,font=myFontdatebold)
	    if feet=='oui':
                modetext="Avec les pieds"
            else:
                modetext='Sans les pieds'
	    if pro=='oui':
	        modetext=modetext+'\nAvec les lumieres exterieures'
	    else:
	        modetext=modetext+'\nSans les lumieres exterieures'
	    if ledr=='oui':
                modetext=modetext+'\nAvec des lumieres rouges'
            else:
                modetext=modetext+'\nSans lumieres rouges'
            
            modetext=modetext+"\nMeilleur temps sur la Led "+str(min)+"\nMoins bon temps sur la led "+str(max)+"\nTemps de la partie: "+str(time)+" sec"
            self.modetimeL=tk.Label(dataF,font=myfont,bg='#fff',text=modetext, justify=tk.LEFT, width=25)


            numbtext="Entrainement numero : "+str(number)
            self.numtimeL=tk.Label(dataF,font=myFontdatebold,text=numbtext, bg='#fff')

            self.lasttimeL.grid(row=1,column=0)
            self.modetimeL.grid(row=2,column=0)
            self.numtimeL.grid(row=3,column=0)

	else:
	    i=0
	    pseudotext="Aucun entrainement fait"
	    self.dateL=tk.Label(dataF,bg='white', text=pseudotext, width=25,font=myFont)
        ipadx=(self.playerInfoL.winfo_reqwidth()-self.dateL.winfo_reqwidth())/2
        self.dateL.grid(row=0,column=0,ipadx=ipadx)
        ledC.create_window(0,0, window=dataF)

        y0=topband.winfo_reqheight()+self.playerInfoL.winfo_reqheight()
        dataF.place(x=0,y=y0)
        ipadx=(-self.playerInfoL.winfo_reqwidth()+self.dateL.winfo_reqwidth())/2
        self.playerInfoL.grid()#ipadx=ipadx)

        if i==0: #aucun entrainement connu
            y0=y0+self.dateL.winfo_reqheight()
        else:
            y0=y0+self.lasttimeL.winfo_reqheight()+self.modetimeL.winfo_reqheight()+self.numtimeL.winfo_reqheight()+self.dateL.winfo_reqheight()

	self.leftledL=tk.Label(desktop,bg='white',width=14,text='Leds de gauche')
        ledC.create_window(0,0, window=self.leftledL)
	self.leftledL.place(x=61,y=y0)
        self.leftledB=makeledbutton(desktop,ledC, self.leftledL.winfo_reqheight(),y0,'l',i)

	self.rightledL=tk.Label(desktop,bg='white',width=14,text='Leds de droite')
        ledC.create_window(0,0, window=self.rightledL)
        self.rightledL.place(x=61,y=y0+60) #les images font 60px de largeur et hauteur
        self.rightledB=makeledbutton(desktop,ledC, self.rightledL.winfo_reqheight(),y0+60,'r',i)

	self.topledL=tk.Label(desktop,bg='white',width=14,text='Leds du haut')
        ledC.create_window(0,0, window=self.topledL)
        self.topledL.place(x=70,y=y0+120)
        self.topledB=makeledbutton(desktop,ledC, self.topledL.winfo_reqheight(),y0+120,'t',i)

	self.downledL=tk.Label(desktop,bg='white',width=14,text='Leds du bas')
        ledC.create_window(0,0, window=self.downledL)
        self.downledL.place(x=70,y=y0+180)
        self.downledB=makeledbutton(desktop,ledC, self.downledL.winfo_reqheight(),y0+180,'d',i)
        
	global vOK 
	vOK=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #variable pour savoir si le bouton de la Led est enfoncee
	#Creation des boutons leds
	for nled in range (6):#les 12 leds du haut
            alpha=9*(math.pi/8)-nled*(math.pi/4)
            R=3*screenHeight/8
            makeledbutton(desktop, ledC, alpha,R, nled+1,i)#leds ext
            makeledbutton(desktop, ledC, alpha,0.50*R, nled+1,i)#leds int
	#les 3leds des pieds
	self.Led13B=makeledbutton(desktop, ledC,9*(math.pi/8),0.5*R,13,i)
	self.Led14B=makeledbutton(desktop, ledC,0,0.5*R,14,i)
	self.Led15B=makeledbutton(desktop, ledC,-(math.pi/8),0.5*R,15,i)
        ledC.grid()
        windowwidth.set(self.playerInfoL.winfo_reqwidth()) #definition de la largeur maximale des differentes frame de main pour placer les boutons de ChoixMode
	id=ChoixMode()

class ChoixMode:
    def __init__(self):
        desktop.config(menu=menubar)
        global code
        code=tk.StringVar()
        global arddatas
        global window
        global vfeet
        vfeet=tk.IntVar()
        global vext
        vext=tk.IntVar()
        global vtime
        vtime=tk.IntVar()
        global vledr
        vledr=tk.IntVar()
	Fenetre.destroy()             
        window=tk.Frame(desktop,bg='#fff3f3') #creation d'une fenetre pour les boutons des modes de jeu
        window.place(x=windowwidth.get()+2,y=topband.winfo_reqheight())
        
        self.modeC=tk.Canvas(desktop)
#creation boutons mode avec ou sans pieds
        FeetBMode=tk.Radiobutton(desktop, image=feetim, indicatoron=0, variable=vfeet, value=50, relief='raised',bg='#fff3f3',command=self.FeetSelection,activebackground='#fff3f3')#S, overrelief='sunken')
        FeetLMode=tk.Label(desktop,text="Avec les pieds",justify=tk.CENTER,bg='#fff3f3',font=myfont,wraplength=60)
        NoFeetModeB=tk.Radiobutton(desktop,image=nofeetim,relief='raised',bg='#fff3f3', indicatoron=0, variable=vfeet,value=66, command=self.FeetSelection,activebackground='#fff3f3')#, overrelief='sunken')
        NoFeetLMode=tk.Label(desktop,text="Sans les pieds",justify=tk.CENTER,bg='#fff3f3',font=myfont,wraplength=60)

#affichage boutons mode avec ou sans pieds
        self.modeC.create_window(0,0, window=FeetBMode)
        FeetBMode.place(x=230, y=topband.winfo_reqheight())
        self.modeC.create_window(0, topband.winfo_reqheight(),window=FeetLMode,anchor=tk.CENTER)
        FeetLMode.place(x=230-(FeetLMode.winfo_reqwidth()-45)/2, y=topband.winfo_reqheight()+FeetBMode.winfo_reqheight())
        self.modeC.create_window(0,0, window=NoFeetModeB)
        NoFeetModeB.place(x=300,y=topband.winfo_reqheight())        
        self.modeC.create_window(0, 0, window=NoFeetLMode)
        NoFeetLMode.place(x=300-(NoFeetLMode.winfo_reqwidth()-45)/2,y=topband.winfo_reqheight()+FeetBMode.winfo_reqheight())
        self.modeC.grid()
        
    def FeetSelection (self):
        JModeB=tk.Radiobutton(desktop, image=lediim,relief='raised', bg='#fff3f3', indicatoron=0, variable=vext,value=1, command= self.ExtSelection,activebackground='#fff3f3',overrelief='sunken')
        JModeL=tk.Label(desktop, text="Sans les leds exterieures",bg='#fff3f3',font=myfont,wraplength=60)
        PModeB=tk.Radiobutton(desktop,image=ledeim, relief='raised', bg='#fff3f3',  indicatoron=0, variable=vext,value=2,command= self.ExtSelection, activebackground='#fff3f3', overrelief='sunken')
        PModeL=tk.Label(desktop, text="Avec les leds exterieures",bg='#fff3f3',font=myfont,wraplength=60)
        
        y0=topband.winfo_reqheight()+80
        self.modeC.create_window(0,0, window=JModeB)
        JModeB.place(x=230, y=y0)
        self.modeC.create_window(0, 0,window=JModeL)
        JModeL.place(x=230-(JModeL.winfo_reqwidth()-45)/2, y=y0+JModeB.winfo_reqheight())
        self.modeC.create_window(0,0, window=PModeB)
        PModeB.place(x=300,y=y0)
        self.modeC.create_window(0, 0, window=PModeL)
        PModeL.place(x=300-(PModeL.winfo_reqwidth()-45)/2,y=y0+JModeB.winfo_reqheight())
 
    def ExtSelection(self):
        EvModeB=tk.Radiobutton(desktop, image=redledim, relief='raised',  bg='#fff3f3',  indicatoron=0, variable=vledr,value=2,command= self.rledSelection, activebackground='#fff3f3', overrelief='sunken')
        EvModeL=tk.Label(desktop, text="Leds vertes et rouges",bg='#fff3f3',font=myfont,wraplength=60)
        EnModeB=tk.Radiobutton(desktop, image=feetim, relief='raised', bg='#fff3f3',  indicatoron=0, variable=vledr, value=1,command= self.rledSelection, activebackground='#fff3f3', overrelief='sunken')
        EnModeL=tk.Label(desktop, text="Leds vertes uniquement",bg='#fff3f3',font=myfont,wraplength=60)
        y0= y0=topband.winfo_reqheight()+180
        self.modeC.create_window(0,0, window=EvModeB)
        EvModeB.place(x=230 ,y=y0)
        self.modeC.create_window(0, 0,window=EvModeL)
        EvModeL.place(x=230-(EvModeL.winfo_reqwidth()-45)/2, y=y0+EvModeB.winfo_reqheight())
        self.modeC.create_window(0,0, window=EnModeB)
        EnModeB.place(x=300,y=y0)
        self.modeC.create_window(0, 0, window=EnModeL)
        EnModeL.place(x=300-(EnModeL.winfo_reqwidth()-45)/2,y=y0+EvModeB.winfo_reqheight())

    def rledSelection(self): #Boutons temps partie
        timeL=tk.Label(desktop, text="Temps de la partie",bg='#fff3f3',font=myfont)
        T1ModeB=tk.Radiobutton(desktop, text="30sec",width=10, font=myfont,relief='raised',  bg='#fff3f3', indicatoron=0, variable=vtime, value=1, command= self.TSelection, activebackground='#fff3f3', overrelief='sunken')
        T2ModeB=tk.Radiobutton(desktop, text="1mn",font=myfont,width=10, relief='raised',bg='#fff3f3', indicatoron=0, variable=vtime, value=2, command= self.TSelection, activebackground='#fff3f3', overrelief='sunken')
        T3ModeB=tk.Radiobutton(desktop, text="1mn30", font=myfont,width=10,relief='raised',   bg='#fff3f3',  indicatoron=0, variable=vtime, value=3, command= self.TSelection, activebackground='#fff3f3', overrelief='sunken')
        T4ModeB=tk.Radiobutton(desktop, text="2mn",font=myfont, width=10,relief='raised',   bg='#fff3f3',  indicatoron=0, variable=vtime, value=4,command= self.TSelection, activebackground='#fff3f3', overrelief='sunken')

        y0= y0=topband.winfo_reqheight()+270
        self.modeC.create_window(0,0, window=timeL)
        timeL.place(x=300-(timeL.winfo_reqwidth()-45), y=y0)
        y0=y0+timeL.winfo_reqheight()
        self.modeC.create_window(0,0, window=T1ModeB,anchor='e')
	x=230-(4*T1ModeB.winfo_reqwidth()-(360-230))/2
        T1ModeB.place(x=x, y=y0)
        self.modeC.create_window(0,0, window=T2ModeB,anchor='e')
        xt=x+T1ModeB.winfo_reqwidth()
        T2ModeB.place(x=xt,y=y0)
        xt=xt+T2ModeB.winfo_reqwidth()
        self.modeC.create_window(0,0, window=T3ModeB,anchor='e')
        T3ModeB.place(x=xt, y=y0)
        self.modeC.create_window(0,0, window=T4ModeB,anchor='e')
        xt=xt+T3ModeB.winfo_reqwidth()
        T4ModeB.place(x=xt,y=y0)
    def TSelection(self):
        y0=y0=topband.winfo_reqheight()+320
        startB=tk.Button(desktop, text="Commencer l'entrainement",bg='#fff3f3',height=2,font=myFont, padx=okpadx,command=self.start)
        self.modeC.create_window(0,0, window=startB)
	x=230-(startB.winfo_reqwidth()-(360-230))/2
        startB.place(x=x,y=y0)
        
    
    def start(self):
        print(nplayerrows.get())
        playerdoc.save()
        for widget in desktop.winfo_children():
                if widget.winfo_name()!='topband':
                    widget.destroy()
        i=0
        code.set(chr((vfeet.get()+8*((vext.get()-1)+(vledr.get()-1)/2)+vtime.get()-1)))
        def update(ind):
            if ind<57: #nombre de calque du gif
                frame = frames[ind]
                ind += 1
                self.countL.configure(image=frame)
                desktop.after(20, update, ind)
            else:
                self.countL.destroy()
                self.serialcom() 
                
        self.countL = tk.Label(desktop)
        self.countL.grid()
        desktop.after(0, update, 0)

    def serialcom (self):
        arddatas=[]
        ser = serial.Serial('/dev/ttyACM0', 9600)
        tosend=code.get()
        print(tosend, 'tosens')#ser.write(code.get().encode())
        ser.write(tosend.encode())
        while 1:
            if(ser.inWaiting() > 0):
                val2 = ser.read() #lecture du HSB de la valeur envoyee
                val3 = ser.read() #lecture du LSB
                i1 = ord(val2) #conversion byte-> entier
                i2 = ord(val3)
                val = i1 * 256 + i2 #reconstruction de la valeur
                print(val, i1, arddatas)
                arddatas.append(val)
        
      
        
class endser: #fin de la liaison serie, remplissage des fichiers
    def __init__(self):
        ser.close()
       # arddatas=[1.001,1, 5, 1.02,71.1,1.001,16, 2, 1.02,1.1, 7.058, 1, 2, 1.02,1.1]#a supp 
        nplayerrows.set(nplayerrows.get()+1)
        playersheet.insert_rows(nplayerrows.get(),1)
        print (len(arddatas))
        for j in range (0,15):
            sheet[playerrow.get(), j+22].set_value(arddatas[j])
            playersheet[nplayerrows.get(), j+13].set_value(arddatas[j])
        n=nplayerrows.get()
        playersheet[nplayerrows.get(), 0].set_value(n)
        sheet[playerrow.get(), 21].set_value(n)
        playersheet[nplayerrows.get(), 1].set_value(now,'date')
        sheet[playerrow.get(), 6].set_value(now,'date')
        print(nplayerrows,'nplayerroows sans serialcom')
        if vfeet==50:
            playersheet[nplayerrows.get(), 3].set_value('oui')
            sheet[playerrow.get(), 10].set_value('oui')
        else:
            playersheet[nplayerrows.get(), 3].set_value('non')
            sheet[playerrow.get(), 10].set_value('non')
        if vext==1:
            playersheet[nplayerrows.get(), 4].set_value('oui')
            sheet[playerrow.get(), 11].set_value('oui')
        else:
            playersheet[nplayerrows.get(), 4].set_value('non')
            sheet[playerrow.get(), 11].set_value('non')
        if vledr==1:
            playersheet[nplayerrows.get(), 5].set_value('oui')
            sheet[playerrow.get(), 12].set_value('oui')
        else:
            playersheet[nplayerrows.get(), 5].set_value('non')
            sheet[playerrow.get(), 12].set_value('non')
        if vtime==1:
            playersheet[nplayerrows.get(), 6].set_value('30 sec')
            sheet[playerrow.get(), 13].set_value('30 sec')
        elif vtime==2:
            playersheet[nplayerrows.get(), 6].set_value('1 min')
            sheet[playerrow.get(), 13].set_value('1 min')
        elif vtime==3:
            playersheet[nplayerrows.get(), 6].set_value('1 min 30')
            sheet[playerrow.get(), 13].set_value('1 min 30')
        else:
            playersheet[nplayerrows.get(), 6].set_value('2 min')
            sheet[playerrow.get(), 13].set_value('2 min')
            
        playerdoc.save()        
        doc.save()
        main()
    
class makeledbutton:
	def __init__(self,parent,C, alpha, R, nLed,i):#x,y positions du bouton, nLed=numero de Led, i indique ule nombre d'entrainement >0
		global timetext
		R1=screenHeight/2
		timetext=tk.StringVar()
		global nLed1
		nLed1=tk.IntVar()

		self.TimeFocusL=tk.Label(desktop)
		if type(nLed)!=int:
			x=0
			y=R
			if nLed=='l':
				nLed1.set(1)
				self.button=tk.Button(parent,image=lledim,relief=tk.FLAT,activebackground='#fff3f3',highlightcolor='#fff3f3',bg='#fff3f3')
			elif nLed=='r':
				nLed1.set(2)
				self.button=tk.Button(parent,image=rledim,relief=tk.FLAT,activebackground='#fff3f3',highlightcolor='#fff3f3',bg='#fff3f3')
			elif nLed=='t':
				nLed1.set(3)
				self.button=tk.Button(parent,image=tledim,relief=tk.FLAT,activebackground='#fff3f3',highlightcolor='#fff3f3',bg='#fff3f3')
			else:
				nLed1.set(4)
				self.button=tk.Button(parent,image=dledim,relief=tk.FLAT,activebackground='#fff3f3',highlightcolor='#fff3f3',bg='#fff3f3')
		else:
			if nLed>12:                   
		            y=screenHeight-80
		        else:
		            y=topband.winfo_reqheight()+R1*0.75-R*math.sin(alpha)
		        if nLed==14:
		            x=0.75*screenWidth-45-45/4 #taille de l'image=45px
		        else:
		            x=0.75*R1*3+R*math.cos(alpha)
			if i==1: #si des temps sont disponibles alors les evenements qui les affichent sont actifs
				self.timedisplay(C, x, y, nLed)
			self.button=tk.Button(parent,image=im,relief=tk.FLAT,activebackground='#fff3f3',highlightcolor='#fff3f3',bg='#fff3f3')
		C.create_window(x,y,window=self.button)
		self.button.place(x=x,y=y)

	def timedisplay(self,C, x, 
y, nLed):
		def ledclickedB(event, nLed=nLed,vOK=vOK):
			return(self.ledclicked(event, nLed,C,x,y,alpha))
		def focusInB ( event,nLed=nLed,C=C):
			return self.focusIn(event,nLed,C,x,y,alpha)
		def focusOutB (event):
			return self.focusOut(event)
	
		self.button.bind('<Enter>', focusInB) #souris arrive sur le bouton de la led nLed
		self.button.bind('<Button-1>', ledclickedB)
		self.button.bind('<Leave>', focusOutB)#souris quite le bouton de la led nLed

	def focusIn (self,event, nLed,C,x,y,alpha): #nLed = position de la led ayant le focus, ledPosition={0;1} avec 0=>interieur et 1=>exterieur
		if vOK[nLed-1]==0:
			self.TimeFocusL.destroy()
			if type(nLed)!=int:
				timevalue=(playersheet[nplayerrows.get()-1,6+nLed1.get()].value) #derniere ligne = dernier temps
				meantimevalue=(playersheet[nplayerrows.get(),6+nLed1.get()].value)
				timetext.set('Dernier temps :  '+str(timevalue) +' sec \n Temps moyen : '+str(meantimevalue)+' sec')
				self.TimeFocusL=tk.Label(desktop, text=timetext.get(),font=myfont, bg='#fff')
				id=(C.create_window(x+60,y,window=self.TimeFocusL))
				self.TimeFocusL.place(x=x+60,y=y)
			else:
				timevalue=(playersheet[nplayerrows.get()-1,12+nLed].value) #derniere ligne = dernier temps
				meantimevalue=(playersheet[nplayerrows.get(),12+nLed].value)
				timetext.set('Dernier temps :  '+str(timevalue) +' sec \n Temps moyen : '+str(meantimevalue)+' sec')
				self.TimeFocusL=tk.Label(desktop, text=timetext.get(),font=myfont, bg='#fff')
				id=(C.create_window(x,y,window=self.TimeFocusL))
				self.TimeFocusL.place(x=x,y=y-self.TimeFocusL.winfo_reqheight())
		else:
			self.TimeFocusL.destroy()
	def focusOut (self,event):
		self.TimeFocusL.destroy()
	def ledclicked(self,event, nLed,C,x,y,alpha):
		if vOK[nLed-1]==0:
			if type(nLed)!=int:
				vOK[nLed-1]=1
				self.TimeFocusL.destroy()
				timevalue=(playersheet[nplayerrows.get()-1,6+nLed1.get()].value )#derniere ligne = dernier temps
				meantimevalue=(playersheet[nplayerrows.get(),6+nLed1.get()].value)
				timetext.set('Dernier temps :  '+str(timevalue) +' sec \n Temps moyen : '+str(meantimevalue)+' sec')
				self.TimeclickL=tk.Label(desktop,  text=timetext.get(),font=myfont, bg='#fff')
				self.button.config(image=im2)
				id=(C.create_window(x+45,y-self.TimeclickL.winfo_reqheight(),window=self.TimeclickL))
				self.TimeclickL.place(x=x,y=y-self.TimeclickL.winfo_reqheight())
			else:
				vOK[nLed-1]=1
				self.TimeFocusL.destroy()
				timevalue=(playersheet[nplayerrows.get()-1,12+nLed].value )#derniere ligne = dernier temps
				meantimevalue=(playersheet[nplayerrows.get(),12+nLed].value)
				timetext.set('Dernier temps :  '+str(timevalue) +' sec \n Temps moyen : '+str(meantimevalue)+' sec')
				self.TimeclickL=tk.Label(desktop,  text=timetext.get(),font=myfont, bg='#fff')
				self.button.config(image=im2)
				id=(C.create_window(x+45,y-self.TimeclickL.winfo_reqheight(),window=self.TimeclickL))
				self.TimeclickL.place(x=x,y=y-self.TimeclickL.winfo_reqheight())
		else:
			self.TimeclickL.destroy()
			vOK[nLed-1]=0
			self.button.config(image=im)

def makeentry(parent, caption, row, columnL,columnE, anchor=None,Labelwidth=None,  width=None,font=None,bg=None,justify=None,pady=None,ipadx=None, **options):
	label= tk.Label(parent, text=caption,width=Labelwidth, anchor=anchor,font=font, bg=bg, justify=justify)	
	entry = tk.Entry(parent,font=font,bg=bg,width=width ,**options)
	
	if ipadx:
		padxL=(ipadx-label.winfo_reqwidth())/2
		ipadxE=(ipadx-entry.winfo_reqwidth())/2
	else:
		padxL=0
		ipadxE=0
	if pady:
		padyL=(pady-label.winfo_reqheight())/2
		padyE=(pady-entry.winfo_reqheight())/2
	else:
		padyL=0
		padyE=0
	
	label.grid(column=columnL,row=row,pady=padyL,padx=padxL)
##	if width:
##		entry.config(width=width)
	entry.grid(column=columnE,row=row,pady=padyE,ipady=5,ipadx=ipadxE)
	

	def showkb(event, Entry=entry):
		entry.delete(0,tk.END) #supprime les caracteres dans entree
		return clavier(Entry) #affiche le clavier
	entry.bind('<FocusIn>',showkb) #appel de la fonction showkb lors de l'evenement "FocusIn" : lorsque le curseur est mit dans "entry"
	def delkb(event, Entry=entry):
		keyboardF.destroy()
	entry.bind('<FocusOut>',delkb) #appel de la fonction delkb lors de l'evenement "FocusOut" : lorsque le curseur sort de "entry"
	return (label,entry)

class clavier: #creation su clavier virtuel
	def __init__(self, Entry):		
		global keyboardF
		keyboardF=tk.Frame(desktop,bg='white')
		keyboardF.grid()
		global entry
		entry=Entry
		global compt
		compt=tk.IntVar()
		compt.set(0)
		r=0
		c=0
		#creation des touches
		self.aB=tk.Button(keyboardF,text='A',command=self.tapedA)
		self.zB=tk.Button(keyboardF,text='Z',command=self.tapedZ)
		self.eB=tk.Button(keyboardF,text='E',command=self.tapedE)
		self.rB=tk.Button(keyboardF,text='R',command=self.tapedR)
		self.tB=tk.Button(keyboardF,text='T',command=self.tapedT)
		self.yB=tk.Button(keyboardF,text='Y',command=self.tapedY)
		self.uB=tk.Button(keyboardF,text='U',command=self.tapedU)
		self.iB=tk.Button(keyboardF,text='I',command=self.tapedI)
		self.reB=tk.Button(keyboardF,text='<=',command=self.tapedret)
		self.oB=tk.Button(keyboardF,text='O',command=self.tapedO)
		self.pB=tk.Button(keyboardF,text='P',command=self.tapedP)
		self.qB=tk.Button(keyboardF,text='Q',command=self.tapedQ)
		self.sB=tk.Button(keyboardF,text='S',command=self.tapedS)
		self.dB=tk.Button(keyboardF,text='D',command=self.tapedD)
		self.fB=tk.Button(keyboardF,text='F',command=self.tapedF)
		self.gB=tk.Button(keyboardF,text='G',command=self.tapedG)
		self.hB=tk.Button(keyboardF,text='H',command=self.tapedH)
		self.jB=tk.Button(keyboardF,text='J',command=self.tapedJ)
		self.kB=tk.Button(keyboardF,text='K',command=self.tapedK)
		self.lB=tk.Button(keyboardF,text='L',command=self.tapedL)
		self.mB=tk.Button(keyboardF,text='M',command=self.tapedM)
		self.wB=tk.Button(keyboardF,text='W',command=self.tapedW)
		self.xB=tk.Button(keyboardF,text='X',command=self.tapedX)
		self.cB=tk.Button(keyboardF,text='C',command=self.tapedC)
		self.vB=tk.Button(keyboardF,text='V',command=self.tapedV)
		self.bB=tk.Button(keyboardF,text='B',command=self.tapedB)
		self.nB=tk.Button(keyboardF,text='N',command=self.tapedN)

		for widget in keyboardF.winfo_children():
			if widget.winfo_class()=='Button':
				ipady=(screenHeight/2-3*self.reB.winfo_reqwidth())/6#-self.reB.winfo_reqwidth()/2 
				if c==9:
					c=0
					r=r+1
				ipadx=(-widget.winfo_reqwidth()+self.reB.winfo_reqwidth())/2+(screenWidth-9*self.reB.winfo_reqwidth())/18
				#affichage des lettres
				widget.grid(row=r,column=c,ipadx=ipadx,ipady=ipady)
				c=c+1
#ecriture des lettres appuyees dans "entry"
	def tapedA (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'A')
	def tapedZ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Z')
	def tapedE (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'E')
	def tapedR (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'R')
	def tapedT (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'T')
	def tapedY (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Y')
	def tapedU (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'U')
	def tapedI (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'I')
	def tapedO (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'O')
	def tapedret (self):
		compt.set(compt.get()-1)
		entry.delete(compt.get())
	def tapedP (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'P')
	def tapedQ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Q')
	def tapedS (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'S')
	def tapedD (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'D')
	def tapedF (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'F')
	def tapedG (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'G')
	def tapedH (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'H')
	def tapedJ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'J')
	def tapedK (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'K')
	def tapedL (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'L')
	def tapedM (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'M')
	def tapedW (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'W')
	def tapedX (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'X')
	def tapedC (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'C')
	def tapedV (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'V')
	def tapedB (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'B')
	def tapedN (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'N')
	
if nrows.get()==0:
	wind=mainparameters()
else:
	wind=Accueil()
desktop.mainloop()   

