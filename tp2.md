1. noms des cartes mères de marque Abit

```sql
SELECT DISTINCT nomComp
    FROM Composant
    WHERE type = "CM" AND marque="Abit";
```

2. noms des machines disposant d'un CD-ROM (donner 2 solutions)

```sql
SELECT DISTINCT nomPC
    FROM Machine
    INNER JOIN Assemble ON Machine.numPC = Assemble.numPC
    INNER JOIN Composant ON Assemble.refComp = Composant.refComp
    WHERE type = "CD";
```

```sql
SELECT DISTINCT nomPC
    FROM Machine
    WHERE EXISTS (
        SELECT * 
            FROM Composant
            INNER JOIN Assemble ON Composant.refComp = Assemble.refComp
            WHERE Assemble.numPC = Machine.numPC AND Composant.type = "CD"
    );
```

3. Correspondance entre le nom des machines et le nom des composants qu'elle possède

```sql
SELECT nomPC, nomComp
    FROM Machine
    INNER JOIN Assemble ON Machine.numPC = Assemble.numPC
    INNER JOIN Composant ON Assemble.refComp = Composant.refComp;
```

4. noms des machines équipées d'une carte vidéo avec au moins 8Mo de mémoire vidéo

```sql

```

5. noms des machines équipées d'un processeur supportant les instructions 3DNow

```sql

```

6. noms de tous les composants équipant les machines de l'atelier

```sql

```

7. liste des salles dans lesquelles se trouve au moins une machine équipée d'une carte son

```sql

```

8. noms des cartes vidéos sur lesquelles sont reliés des écrans de la marque teco

```sql

```

9. noms des machines qui ne sont pas équipées de carte son (donner 2 solutions)

```sql

```

10. noms des machines équipées de processeurs Celeron

```sql

```

11. numéros de machines achetées en 1999

```sql

```

12. noms des machines équipées d'au moins un composant de chaque type

```sql

```
