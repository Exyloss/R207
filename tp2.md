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
SELECT nomPC
    FROM Machine
    INNER JOIN Assemble ON Machine.numPC = Assemble.numPC
    INNER JOIN CarteVideo ON Assemble.refComp = CarteVideo.refComp
    WHERE ramVideo >= 8;
```

5. noms des machines équipées d'un processeur supportant les instructions 3DNow

```sql
SELECT nomPC
    FROM Machine
    INNER JOIN Assemble ON Machine.numPC = Assemble.numPC
    INNER JOIN Processeur ON Assemble.refComp = Processeur.refComp
    WHERE TroisDNow = "oui";
```

6. noms de tous les composants équipant les machines de l'atelier

```sql
SELECT nomComp
    FROM Composant
    INNER JOIN Assemble ON Composant.refComp = Assemble.refComp
    INNER JOIN Machine ON Assemble.numPC = Machine.numPC
    WHERE salle = "atelier";

```

7. liste des salles dans lesquelles se trouve au moins une machine équipée d'une carte son

```sql
SELECT DISTINCT salle
    FROM Machine
    INNER JOIN Assemble ON Machine.numPC = Assemble.numPC
    INNER JOIN Composant ON Assemble.refComp = Composant.refComp
    WHERE type = "Son";
```

8. noms des cartes vidéos sur lesquelles sont reliés des écrans de la marque teco

```sql
SELECT DISTINCT C1.nomComp
    FROM Assemble A1
    INNER JOIN Composant C1 ON A1.refComp = C1.refComp
    WHERE type="Video" AND EXISTS (
        SELECT *
            FROM Composant C2
            INNER JOIN Assemble A2 ON C2.refComp = A2.refComp
            WHERE A2.numPC = A1.numPC AND C2.type = "Ecran" AND C2.marque = "teco"
    );
```

9. noms des machines qui ne sont pas équipées de carte son (donner 2 solutions)

```sql
SELECT M.nomPC
    FROM Machine M
    WHERE NOT EXISTS (
        SELECT *
            FROM Assemble A
            INNER JOIN Composant C ON A.refComp = C.refComp
            WHERE A.numPC = M.numPC AND C.type = "Son"
    );
```

10. noms des machines équipées de processeurs Celeron

```sql
SELECT M.nomPC
    FROM Machine M
    WHERE EXISTS (
        SELECT *
            FROM Assemble A
            INNER JOIN Composant C ON A.refComp = C.refComp
            WHERE A.numPC = M.numPC AND C.nomComp LIKE 'Celeron%'
    );
```

11. numéros de machines achetées en 1999

```sql
SELECT nompc
    FROM Machine
    WHERE dateachat LIKE '%/1999';
```

12. noms des machines équipées d'au moins un composant de chaque type (noms des machines telles qu'il n'y ait pas de type de composant dont elles ne possèdent pas au moins un élément

```sql
SELECT nompc
    FROM Machine
    WHERE NOT EXISTS (
        SELECT DISTINCT C1.type
            FROM Composant C1
            WHERE NOT EXISTS (
                SELECT *
                    FROM Assemble
                    INNER JOIN Composant C2 ON Assemble.refComp = C2.refComp
                    WHERE Assemble.numpc = Machine.numpc AND C2.type = C1.type
            )
    );
```

13. noms des machines équipées de disques durs SCSI

```sql
SELECT nompc
    FROM Machine
    INNER JOIN Assemble ON Machine.numpc = Assemble.numpc
    INNER JOIN DisqueDur ON Assemble.RefComp = DisqueDur.refComp
    WHERE DisqueDur.interface = 'SCSI';
```

14. noms des machines qui ne sont pas équipées de disques durs IDE

```sql
SELECT DISTINCT nompc
    FROM Machine
    INNER JOIN Assemble ON Machine.numpc = Assemble.numpc
    INNER JOIN DisqueDur ON Assemble.refComp = DisqueDur.RefComp
    WHERE DisqueDur.interface != 'IDE';
```

15. liste des marques de cartes mères utilisées dans l'entreprise

```sql
SELECT DISTINCT marque
    FROM Composant
    WHERE type = 'CM';
```
