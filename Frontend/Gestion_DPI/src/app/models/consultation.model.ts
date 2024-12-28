export interface Resume {
  diagnostic: string;
  symptomes: string;
  antecedents: string;
  autres_informations: string; // Not mandatory
}

export interface Medicament {
  nom: string;
  description: string; // Added field
  prix: number; // Added field
  quantite: number; // Added field
}

export interface Ordonnance {
  date_prescription: string;
  etat_ordonnance: boolean;
  prescriptions : Prescription[] ;
}

export interface Prescription {
  dose: string;
  duree: string;
  medicament: Medicament; // Corrected to match structure
}

export interface BilanBiologique {
  description : string;
}

export interface BilanRadiologique {
  description : string;
  type : string;
}

export interface Consultation {
  resume: Resume;
  ordonnance : Ordonnance;
  bilan_biologique: BilanBiologique;
  bilan_radiologique: BilanRadiologique;
}
