# Banque Grolandaise

On a un fichier C très simple qui tient compte de notre solde. Notre solde est négatif, et il faut le rendre positif. Problème, on ne peut que soustraire !

Notre solde est évidemment un entier signé, puisqu'il est négatif. On peut essayer d'entrer un nombre négatif, mais c'est évidemment empêché : 
```c
	}else if (num < 0){
            printf("tu ne peux pas dépenser une quantité négative d'argent\n");
        }
```

Mais les entiers C ne peuvent représenter qu'un certain intervalle (de -2\*\*31 à 2\*\*31 - 1), et si on essaie de soustraire un trop gros nombre on obtient un nombre positif (ce qu'on appelle un integer underflow).

Ainsi, en dépensant 2147483647 (2\*\*31 - 1) puis une quantité quelconque comme 5, on aura underflow notre solde et il sera positif !
