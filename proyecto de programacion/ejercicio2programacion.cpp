/*********************************************************************************************
   Ha sido seleccionado para nuestra vacante como Analista de Datos. Para asegurarnos de
que está listo para entrar a nuestro equipo de programadores de software necesitamos que
primero realice unos cálculos sencillos de estadística. Un cliente nos ha Suministrado una
data emitida en forma de lista por lo que usted cómo programador debe diseñar un código
que: 
● Leer desde el teclado la data del cliente, con un mínimo de 20 valores.
● Mostrar la data en la pantalla
● Encuentre la media
● La mediana
● La desviación estándar


*********************************************************************************************/

#include <iostream>
#include <math.h>
using namespace std;

int main ()
{
    short int i, j , n;
    cout << "Introduzca el numero de elementos: " ;
    cin>>n;
    
    float A[n];
    float suma=0 , media, mediana, desviacion=0 , aux;
    
    for (i=0; i<n; i++)
    {
        cout<<"A["<<i<<"]:";
        cin>>A[i];
        suma+=A[i];
    }  
    
    
    media= suma/n ;    //media aritmetica
    
    //Organizacion del conjunto
    
    for (j=0 ; j<n ; j++)
     for (i=0; i<n-1 ; i++)
     if (A[i]>A[i+1])
{
    aux=A[i];
    A[i]=A[i+1];
    A[i+1]=aux;
}
   if ((n/2)==1) // mediana para numeros impares
   mediana =A[n/2];
   else 
   mediana=(A[n/2]+A[n/2-1])/2;   // mediana para numeros pares

  cout <<"Media: "<<media<<endl;
  cout <<"Mediana: "<<mediana<<endl;

//calculo para la desviacion estandar//
 aux=0;
 for(i=0; i<n; i++)
  aux=aux+pow(A[i]-media,2);
 aux=aux/n;
 desviacion=sqrt(aux);
 cout<<"Desviacion estandar :" <<desviacion<<endl;

    return 0 ;

}
    
   
        
    


    


