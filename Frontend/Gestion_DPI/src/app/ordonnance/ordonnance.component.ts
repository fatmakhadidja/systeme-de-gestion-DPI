import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Ordonnance, Prescription } from '../models/consultation.model';
import { HeaderComponent } from '../header-component/header.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ConsultationService } from '../services/consultation.service';

@Component({
  selector: 'app-ordonnance',
  imports: [HeaderComponent, CommonModule, FormsModule],
  templateUrl: './ordonnance.component.html',
  styleUrls: ['./ordonnance.component.css'],
})
export class OrdonnanceComponent {
  ordonnance : Ordonnance;
  prescription: Prescription = { dose: '', duree: '', medicament: '' };

  showModal: boolean = false;
  modalMessage: string = '';

  constructor(private consultationService: ConsultationService, private router: Router) {
    this.ordonnance = this.consultationService.getConsultation().ordonnance;
  }

  addPrescription(): void {
    if (this.prescription.medicament && this.prescription.dose && this.prescription.duree) {
      this.ordonnance.prescription.push({ ...this.prescription });
      this.prescription = { dose: '', duree: '', medicament: '' };

    } else {
      this.modalMessage = 'Veuillez remplir tous les champs avant d’ajouter.';
      this.showModal = true;
    }
  }

  confirm(): void {
    if (this.ordonnance.prescription.length === 0) {
      this.modalMessage = 'Vous devez ajouter au moins une prescription avant de confirmer l’ordonnance.';
      this.showModal = true;
    } else {
    // Enregistrer l'ordonnance si au moins une prescription existe
    this.consultationService.updateConsultation('ordonnance', this.ordonnance);
    this.modalMessage = 'Ordonnance enregistrée avec succès.';
    this.showModal = true;
    this.router.navigate(['/creation-consult']);
    }
  }

  cancel(): void {
    this.router.navigate(['/creation-consult']);
  }

  closeModal() {
    this.showModal = false;
  }
}
