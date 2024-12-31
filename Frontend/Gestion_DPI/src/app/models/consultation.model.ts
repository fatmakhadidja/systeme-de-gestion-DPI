export interface Resume {
  diagnostic: string;
  symptomes: string;
  antecedents: string;
  autres_informations: string; // Not mandatory
}

export interface Ordonnance {
  prescription : Prescription[] ;
}

export interface Prescription {
  dose: string;
  duree: string;
  medicament: string; // Corrected to match structure
}

export interface BilanBiologique {
  description : string;
}

export interface BilanRadiologique {
  description : string;
  type : string;
}

export interface Consultation {
  nss: string;
  resume: Resume;
  ordonnance : Ordonnance;
  bilan_biologique: BilanBiologique;
  bilan_radiologique: BilanRadiologique;
}
