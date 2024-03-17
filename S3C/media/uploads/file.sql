-- 1. Création de la table Utilisateurs
CREATE TABLE Utilisateurs (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Nom VARCHAR(255),
    Prénom VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    MotDePasse VARCHAR(255),
    Role ENUM('étudiant', 'organisateur', 'jury'),
    Spécialité VARCHAR(255),
    Niveau ENUM('L1', 'L2', 'L3', 'M1', 'M2')
);

-- 2. Création de la table Équipes
CREATE TABLE Équipes (
    EquipeID INT AUTO_INCREMENT PRIMARY KEY,
    NomEquipe VARCHAR(255),
    LeadID INT,
    AdjointID INT,
    NombreMembres INT,
    FOREIGN KEY (LeadID) REFERENCES Utilisateurs(UserID),
    FOREIGN KEY (AdjointID) REFERENCES Utilisateurs(UserID)
);

-- 3. Création de la table Appartenances
CREATE TABLE Inscription (
    InscriptionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    EquipeID INT,
    Role ENUM('lead', 'adjoint', 'membre'),
    FOREIGN KEY (UserID) REFERENCES Utilisateurs(UserID),
    FOREIGN KEY (EquipeID) REFERENCES Équipes(EquipeID)
);

-- 4. Création de la table Défis
CREATE TABLE Défis (
    DefiID INT AUTO_INCREMENT PRIMARY KEY,
    Titre VARCHAR(255),
    Description TEXT,
    nom_file VARCHAR(255),
    chemin_file VARCHAR(255),
    Date_debut DATE,
    Date_fin DATE
);

-- 5. Création de la table Soumissions
CREATE TABLE Soumissions (
    SoumissionID INT AUTO_INCREMENT PRIMARY KEY,
    EquipeID INT,
    DefiID INT,
    LienGit VARCHAR(255),
    DateSoumission DATETIME,
    Status ENUM('soumis', 'évalué'),
    FOREIGN KEY (EquipeID) REFERENCES Équipes(EquipeID),
    FOREIGN KEY (DefiID) REFERENCES Défis(DefiID)
);

-- 6. Création de la table Évaluations
CREATE TABLE Évaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY,
    SoumissionID INT,
    Score INT,
    Commentaires TEXT,
    FOREIGN KEY (SoumissionID) REFERENCES Soumissions(SoumissionID)
);

-- 7. Création de la table Résultats
CREATE TABLE Résultats (
    ResultatID INT AUTO_INCREMENT PRIMARY KEY,
    EquipeID INT,
    ScoreTotal INT,
    FOREIGN KEY (EquipeID) REFERENCES Équipes(EquipeID)
);
