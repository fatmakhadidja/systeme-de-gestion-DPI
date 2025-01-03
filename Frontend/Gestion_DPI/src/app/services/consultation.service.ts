import { Injectable } from '@angular/core';
import { Consultation } from '../models/consultation.model';

@Injectable({
  providedIn: 'root',
})
export class ConsultationService {
  private consultation: Consultation = {
    nss: '2222222', // constant for now, needed from amira
    resume: {
      diagnostic: '',
      symptomes: '',
      antecedents: '',
      autres_informations: '',
    },
    ordonnance: {
      prescription: [],
    },
    bilan_biologique: {
      description: '',
    },
    bilan_radiologue: {
      description: '',
      type: '',
    },
  };

  getConsultation(): Consultation {
    return this.consultation;
  }

  updateConsultation<T extends keyof Consultation>(key: T, value: Consultation[T]): void {
    this.consultation[key] = value;
  }
}
