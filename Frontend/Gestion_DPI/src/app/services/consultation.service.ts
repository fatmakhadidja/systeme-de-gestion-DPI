import { Injectable } from '@angular/core';
import { Consultation } from '../models/consultation.model';

@Injectable({
  providedIn: 'root',
})
export class ConsultationService {
  private consultation: Consultation = {
    resume: {
      diagnostic: '',
      symptomes: '',
      antecedents: '',
      autres_informations: '',
    },
    ordonnance: {
      date_prescription: '',
      etat_ordonnance: false,
      prescriptions: [
        {
          dose: '500mg',
          duree: '7 days',
          medicament: {
            nom: 'Paracetamol',
            description: 'Pain reliever and fever reducer',
            prix: 5,
            quantite: 10,
          },
        },
      ],
    },
    bilan_biologique: {
      description: '',
    },
    bilan_radiologique: {
      description: '',
      type: '',
    },
  };

  getConsultation() {
    return this.consultation;
  }

  updateConsultation<K extends keyof Consultation>(
    section: K,
    data: Consultation[K]
  ): void {
    this.consultation[section] = data;
  }
}
