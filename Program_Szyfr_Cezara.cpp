#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

void konwertuj (string &wyraz, char* &wyraz_char, int &dlug_wyraz){
  dlug_wyraz=wyraz.length();
  wyraz_char=new char[dlug_wyraz];
  wyraz_char=wyraz.data();
}

void tworz_klucz (char* klucz_char, int dlug_klucz){
    for(int i=0; i<dlug_klucz; ++i) klucz_char[i]-=96;
}

void szyfrowanie(char* wyraz, char* klucz, int dlug_klucz, int dlug_wyraz){
    for (int i=0; i<dlug_wyraz; ++i) {
        if(wyraz[i]+klucz[i%dlug_klucz]>122) wyraz[i]=96+(wyraz[i]+klucz[i%dlug_klucz])%122;
        else wyraz[i]=(wyraz[i]+klucz[i%dlug_klucz]);
    }
    }

void odszyfrowanie (char* wyraz,char* klucz, int dlug_klucz, int dlug_wyraz){
  for (int i=0; i<dlug_wyraz; ++i) { 
    if (wyraz[i]-klucz[i%dlug_klucz]<97) wyraz[i]=123-(97-(wyraz[i]-klucz[i%dlug_klucz]));
      else wyraz[i]=wyraz[i]-klucz[i%dlug_klucz];
}
}

void male (string &wyraz){
  transform(wyraz.begin(),wyraz.end(), wyraz.begin(), [](char c){return tolower(c);});
}

int main(){
    int dlug_klucz, dlug_wyraz;
    char *klucz_char, *wyraz_char;
    string wyraz, klucz;
  cout<<"Podaj wyraz do szyfrowania: "<<endl;
  cin>>wyraz;
  male(wyraz); 
  konwertuj(wyraz, wyraz_char, dlug_wyraz);
  cout<<"Podaj klucz: "<<endl;
  cin>>klucz;
  male(klucz);
  konwertuj(klucz, klucz_char, dlug_klucz);
  tworz_klucz(klucz_char, dlug_klucz);
  szyfrowanie(wyraz_char, klucz_char, dlug_klucz, dlug_wyraz);
  cout<<"Zaszyfrowany wyraz to: "<<wyraz_char<<endl;
  cout<<"Podaj klucz: "<<endl;
  cin>>klucz;
  male(klucz);
  konwertuj(klucz, klucz_char, dlug_klucz);
  tworz_klucz(klucz_char, dlug_klucz);
  odszyfrowanie(wyraz_char, klucz_char, dlug_klucz, dlug_wyraz);
  cout<<"Odszyfrowany wyraz to: "<<wyraz<<endl;
    cin.get(),cin.get();
    return 0;
}