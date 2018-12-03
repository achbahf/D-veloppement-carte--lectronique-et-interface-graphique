//Définition des variables:
//Variables de jeu:
int niveau;
int eval;
long tps_partie;//Définition du temps d'une partie
long tps_ON_V = 1500;//Définition du temps d'allumage de la LED Verte
long tps_ON_R = 500;//Définission du temps d'allumage de la LED Rouge
long tps_OFF = 200;//Définition du temps d'attente entre 2 coups

int premier;//Place du premier bouton à prendre en compte
int dernier;//Place du dernier bouton à prendre en compte

long currentMillis0;
long previousMillis0;

//Tableaux des pins des LEDs et des boutons
int pin_LED_V[15]= {
  46,47,51,22,26,30,34,38,42,23,27,31,35,39,43};//Définition des pins des LEDs vertes
int pin_LED_R[15] = {
  48,49,53,24,28,32,36,40,44,25,29,33,37,41,45};//Définition des pins des LEDs rouges
int pin_bouton[15] = {
  13,14,15,1,2,3,4,5,6,7,8,9,10,11,12};//Définition des pins des boutons

//Variables de résultats
long reaction[15];//Définition du tableau contenant les temps de réaction
long S_temps;//Somme des temps de réaction
long bon[15];//Définition du tableau comptant les coups bons
long coups;//Nombre de coups OK
long faute[15];//Définition du tableau comptant les fautes
long S_faute;//Nombre de fautes totales
long tps_moyen;//Temps moyen de réaction



//Démarrage Arduino
void setup()
{
  //Définition de la vitesse de communication USB
  Serial.begin(9600);
  
  randomSeed(analogRead(0));

  //Définition des OUTPUTS et mise à zéro
  for (int k=22; k <= 53; k++)
  {
    pinMode(k,OUTPUT); 
    digitalWrite(k,LOW);
  }

}



//Programme
void loop()
{
  //Mettre à zéro les tableaux reaction, fautes, bon
  reset_tableau(reaction,15);
  reset_tableau(faute,15);
  reset_tableau(bon,15);

  //Attente interface
  start(&niveau, &eval, &tps_partie, &premier, &dernier);

  //Début de la partie
  currentMillis0 = millis();
  previousMillis0 = currentMillis0;

  while(currentMillis0-previousMillis0 < tps_partie)
  {
    jouer_coup(pin_bouton, pin_LED_V, pin_LED_R, reaction, bon, faute, tps_ON_V, tps_ON_R, tps_OFF, niveau, eval, premier, dernier);
    currentMillis0 = millis();
  }

  //Fin de la partie et retour des valeurs
  S_temps = somme_tableau(reaction,15);
  coups = somme_tableau(bon,15);
  S_faute = somme_tableau(faute,15);
  tps_moyen = S_temps / coups;
  Serial.print(tps_moyen);
  Serial.print(";");
  Serial.print(S_faute);
}



//Choix aléatoire de la couleur (renvoi 0 si vert, 1 si rouge)
int choix_couleur()
{
  int color_LED = random(10);
  int color = 0;
  if (color_LED == 1)
  {
    color = 1;
  }
  return color;
}



//Tester les autres boutons (renvoie 1 si un autre bouton que celui attendu appuyé, 0 sinon)
boolean test_autres_boutons(int var,int tab[15])
{
  boolean etat;
  for (int i = 0; i < 15; i++)
  {
    if(i == var)
    {
      etat = 0;
    }
    else if (analogRead (tab[i]) > 512) 
    {
      etat = 1; 
      goto fin;
    }  
  }
fin:
  return etat;
}



//Tester tous les boutons (renvoie 1 si un bouton appuyé, 0 sinon)
boolean test_boutons(int tab[15])
{
  boolean etat = 0;
  for (int i = 0; i < 15; i++)
  {
    if(analogRead (tab[i]) > 512)
    {
      etat = 1; 
      goto fin;
    }
  }
fin:
  return etat;
}




//Sous-programme fesant jouer un coup
void jouer_coup(int tab_bouton[15], int tab_LED_V[15], int tab_LED_R[15], long tab_reaction[15], long tab_bon[15], long tab_faute[15], long time_ON_V, long time_ON_R, long time_OFF, int level, int ev, int first, int last)
{
  int alea = first + random(last-first);
  int couleur = 0;

  if(ev == 0) //Mode entrainement rouges OK
  {
    couleur = choix_couleur();
  }

  long previousMillis = 0;
  long currentMillis = millis();

  switch(couleur)
  {
    //Cas diode verte allumée
  case 0:
    previousMillis = currentMillis;
    digitalWrite(tab_LED_V[alea], HIGH);
    while( currentMillis-previousMillis < time_ON_V )
    {
      currentMillis = millis();
      if(analogRead(tab_bouton[alea]) > 512)
      {
        tab_reaction[alea] = tab_reaction[alea] + currentMillis - previousMillis;
        tab_bon[alea] = tab_bon[alea] + 1;
        goto fin0;
      }
      else if(test_autres_boutons(alea, pin_bouton) == 1)
      {
        tab_faute[alea] = tab_faute[alea] + 1; 
        goto fin0;
      }
    }
    tab_reaction[alea] = tab_reaction[alea] + time_ON_V;
    tab_bon[alea] = tab_bon[alea] + 1;
    tab_faute[alea] = tab_faute[alea] + 1;
    break;

    //Cas diode rouge allumée
  case 1:
    previousMillis = currentMillis;
    digitalWrite(tab_LED_R[alea],HIGH);
    while( currentMillis-previousMillis < time_ON_R )
    {
      if( test_boutons(tab_bouton) == 1 )
      {
        tab_faute[alea] = tab_faute[alea] + 1;
        goto fin0;
      }
      currentMillis = millis();
    }
    break;
  }
fin0:
  //Éteindre les LEDs
  digitalWrite(tab_LED_R[alea],LOW);
  digitalWrite(tab_LED_V[alea],LOW);

  //Attente entre 2 coups
  delay(time_OFF);

  return;
}



//Fonction de démarrage
void start(int *level, int *ev, long *time_partie, int *first, int *last)
{
  int mode0;
  int mode1 = -1;
  int mode2;
  while (mode1 == -1)
  { 
    if(Serial.available() > 0)
    {
      mode0 = Serial.read()-50; // L'arduino reçoit un caractère pour le mode.
      //Serial.print(mode0);
      delay(50); 
      if (mode0 >= 0 && mode0 <= 31)
      {
        mode1 = mode0;

        //Choix du niveau Amateur-Pro
        if (mode1 / 16 == 0)
        {
          *first = 0;
        }
        else
        {
          *first = 3;
        }
        if ((mode1 % 16) / 8 == 0)
        {
          *level = 0;
        }
        else
        {
          *level = 1;
        }

        //Choix du mode Entrainement - Evaluation
        if ((mode1 % 8) / 4 == 0)
        {
          *ev = 0;
        }
        else
        {
          *ev = 1;
        }

        //Choix du temps de la partie 30 - 60 - 90 - 120 (secondes)
        mode2 = mode1 % 4;
        switch(mode2)
        {
        case 0:
          {
            *time_partie = 30000; // 30s
            break;
          }
        case 1:
          {
            *time_partie = 60000; // 60s
            break;
          }
        case 2:
          {
            *time_partie = 90000; // 90s
            break;
          }
        case 3:
          {
            *time_partie = 120000; // 120s
            break;
          }
        }
      }
    }
  }
  if(*level == 0)
  {
    *last = 8;
  }
  else if(*level == 1)
  {
    *last = 14;
  }
}



//Fontion de somme des éléments d'un tableau
long somme_tableau(long tab[15], int l)
{
  long s = 0;
  for (int i = 0; i < l; i++)
  {
    s = s + tab[i];
  }
  return s;
}



//Fonction de mise à zéro d'un tableau
void reset_tableau(long tab[15], int l)
{
  for (int i = 0; i < l; i++)
  {
    tab[i] = 0;
  }
  return;
}


















