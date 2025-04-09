# The BurgerKing Crack

On nous donne une archive zip chiffrée, et on nous dit que les initiales de Burger King, `BK`, ont probablement une importance. En cherchant par exemple `BK crypted zip` dans son moteur de recherche préféré, on tombe sur https://github.com/kimci86/bkcrack, qui est une implémentation d'une attaque à clair connu.
Pour que l'attaque fonctionne, il faut 12 octets de texte clair connu minimum. Heureusement, on sait que l'archive contient un fichier PDF, qui a un header d'une longueur suffisante.
On peut extraire le header d'un PDF existant de cette manière : `head -c 12 ../../stegano/ascii_table.pdf > header.plain`.
Ensuite il ne reste plus qu'à lancer l'attaque en suivant la documentation du repo github : 
`bkcrack -C burgerking.zip -c kings_birthday.pdf -p header.plain`
On obtient les trois clés de déchiffrement, et on peut ainsi enlever le mot de passe de l'archive et lire le ficher texte qui contient le flag. (Et le PDF c'était une promo pour BK)
