//https://fre.myservername.com/c-list-dictionary-tutorial-with-code-examples#C_Dictionary
#define NUMPINNUM 11
#define NUMPINANA 6
#define PRECISION 3

int pinNumeriqueHigh[NUMPINNUM];
int compteurPinNumeriqueHigh = 0;

int pinAnalogiqueHigh[NUMPINANA];
int compteurPinAnalogiqueHigh = 0;

int pinNumeriqueHighRam[NUMPINNUM];
int pinAnalogiqueHighRam[NUMPINANA];

int etatPinNumerique;
int etatPinAnalogique;

String boutonPresse;

void setup() {
  
  Serial.begin(115200);
  
  Serial.println("Initialisation de l'Arduino :\n [Void Setup]\n");
  
  // Setup variable
  
  for (int i = 0; i < NUMPINNUM; i++) {pinNumeriqueHighRam[i] = 0;}
  for (int i = 0; i < NUMPINANA; i++) {pinAnalogiqueHighRam[i] = 0;}

  
  // Analyse des PINs Numériques :
  
  Serial.println("Analyse des PINs Numeriques :");
  for (int pinNumerique = 2; pinNumerique <= NUMPINNUM+1; pinNumerique++) { // Parcourt les pins digitaux de 2 à 13
  etatPinNumerique = digitalRead(pinNumerique); // Lit l'état du pin
  Serial.print(etatPinNumerique);
  Serial.print(" - Pin ");
  Serial.print(pinNumerique);
  Serial.print(": ");
  Serial.println(etatPinNumerique == HIGH ? "HIGH" : "LOW"); // Affiche l'état du pin
  
    
  // Récupération des PINs Numérique HIGH :
    if(etatPinNumerique != 0){
      if (compteurPinNumeriqueHigh < NUMPINNUM) {
        pinNumeriqueHigh[compteurPinNumeriqueHigh] = pinNumerique;
        compteurPinNumeriqueHigh++;
    }
   }
  }
  
  // Affiche les PINs Numérique HIGH :
  Serial.print("PINS Numerique HIGH : ");
   for (int i = 0; i < compteurPinNumeriqueHigh; i++) {
    Serial.print(pinNumeriqueHigh[i]);
    Serial.print(" ");
   }
  
  
  Serial.println("\n");
  
  
  // Analyse des PINs Analogique :
  
  Serial.println("Analyse des PINs Analogiques :");
  for (int pinAnalogique = 0; pinAnalogique <= NUMPINANA-1; pinAnalogique++){
  etatPinAnalogique = analogRead(pinAnalogique); // Lit l'état du pin
  Serial.print(etatPinAnalogique);
  Serial.print(" - Pin A");   
  int ensemblePinAnalogique = pinAnalogique;
  Serial.print(ensemblePinAnalogique);
  Serial.print(": ");
  Serial.println(etatPinAnalogique >= 1 ? "HIGH" : "LOW");
  
    
  // Récupération des PINs Analogique HIGH :
  if(etatPinAnalogique != 0){
      if (compteurPinAnalogiqueHigh < NUMPINANA) {
        pinAnalogiqueHigh[compteurPinAnalogiqueHigh] = ensemblePinAnalogique;
        compteurPinAnalogiqueHigh++;
    }
   }
  }
  
  // Affiche les PINs Analogique HIGH :
  Serial.print("PINS Analogiques HIGH : ");
   for (int i = 0; i < compteurPinAnalogiqueHigh; i++) {
    Serial.print("A");
    Serial.print(pinAnalogiqueHigh[i]);
    Serial.print(" ");
   }
  
  Serial.println("\n");
  
  Serial.println("[/Void Setup]\n");
}

void printNumerique(int i,int Value){
  if (Value != pinNumeriqueHighRam[i]){
  pinNumeriqueHighRam[i] = Value;
  Value = Value == 1 ? 0 : 1;
  //Serial.println("[" + String(i) + "] Bouton : " + String(Value)); 
  Serial.println(String(i) + ":" + String(Value)); 
  }
}

void printAnalogique(int i,int Value){
  if (Value > pinAnalogiqueHighRam[i] + PRECISION || Value < pinAnalogiqueHighRam[i] - PRECISION ){
  pinAnalogiqueHighRam[i] = Value;
  //Serial.println("[A" + String(i) + "] Potentiometre : " + String(Value));
  Serial.println("A" + String(i) + ":" + String(Value));
  }
}

void loop(){              
   	for (int i = 0; i < compteurPinNumeriqueHigh; i++) {
    int etatCapteur = digitalRead(pinNumeriqueHigh[i]);
      printNumerique(pinNumeriqueHigh[i],etatCapteur);
    }
  	for (int i = 0; i < compteurPinAnalogiqueHigh; i++) {
    int etatCapteur = analogRead(pinAnalogiqueHigh[i]);
      printAnalogique(pinAnalogiqueHigh[i],etatCapteur);
    }
}
