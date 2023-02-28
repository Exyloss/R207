BEGIN TRANSACTION;

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Cliente;

CREATE TABLE Cliente (
    NumCliente INTEGER PRIMARY KEY,
    NomCliente TEXT NOT NULL,
    PrénomCliente TEXT NOT NULL,
    AdresseCliente TEXT NOT NULL,
    NumRéunion TEXT NOT NULL
);

DROP TABLE IF EXISTS Réunion;

CREATE TABLE Réunion (
    NumRéunion INTEGER PRIMARY KEY,
    DateRéunion DATE NOT NULL
);

DROP TABLE IF EXISTS accueille;

CREATE TABLE accueille (
    NumRéunion INTEGER PRIMARY KEY,
    NumCliente INTEGER,
    FOREIGN KEY (NumRéunion) REFERENCES Réunion (NumRéunion),
    FOREIGN KEY (NumCliente) REFERENCES Cliente (NumCliente)
);

DROP TABLE IF EXISTS participe;

CREATE TABLE participe (
    NumRéunion INTEGER NOT NULL,
    NumCliente INTEGER NOT NULL,
    FOREIGN KEY (NumRéunion) REFERENCES Réunion (NumRéunion),
    FOREIGN KEY (NumCliente) REFERENCES Cliente (NumCliente)
);

DROP TABLE IF EXISTS Commande;

CREATE TABLE Commande (
    NumCmde INTEGER PRIMARY KEY
);

DROP TABLE IF EXISTS passée_par;

CREATE TABLE passée_par (
    NumCmde INTEGER PRIMARY KEY,
    NumCliente INTEGER,
    FOREIGN KEY (NumCliente) REFERENCES Cliente (NumCliente),
    FOREIGN KEY (NumCmde) REFERENCES Commande (NumCmde)
);

DROP TABLE IF EXISTS Produit;

CREATE TABLE Produit (
    RefProd  INTEGER PRIMARY KEY,
    NomProd TEXT NOT NULL,
    PU INTEGER NOT NULL,
    Couleur TEXT NOT NULL,
    NumCat INTEGER NOT NULL
);

DROP TABLE IF EXISTS fait_la_promo;

CREATE TABLE fait_la_promo (
    NumRéunion INTEGER PRIMARY KEY,
    RefProd INTEGER,
    FOREIGN KEY (NumRéunion) REFERENCES Réunion (NumRéunion),
    FOREIGN KEY (RefProd) REFERENCES Produit (RefProd)
);

DROP TABLE IF EXISTS Catégorie;

CREATE TABLE Catégorie (
    NumCat INTEGER PRIMARY KEY,
    Libellé TEXT NOT NULL
);

DROP TABLE IF EXISTS est_dans;

CREATE TABLE est_dans (
    RefProd INTEGER PRIMARY KEY,
    NumCat INTEGER NOT NULL,
    FOREIGN KEY (RefProd) REFERENCES Produit (RefProd),
    FOREIGN KEY (NumCat) REFERENCES Catégorie (NumCat)
);

DROP TABLE IF EXISTS concerne;

CREATE TABLE concerne (
    NumCmde INTEGER NOT NULL,
    RefProd INTEGER,
    qté INTEGER NOT NULL,
    FOREIGN KEY (NumCmde) REFERENCES Commande (NumCmde),
    FOREIGN KEY (RefProd) REFERENCES Produit (RefProd)
);

DROP TABLE IF EXISTS a_lieu;

CREATE TABLE a_lieu (
    NumCmde INTEGER PRIMARY KEY,
    NumRéunion INTEGER,
    FOREIGN KEY (NumCmde) REFERENCES Commande (NumCmde),
    FOREIGN KEY (NumRéunion) REFERENCES Réunion (NumRéunion)
);

COMMIT;
