import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Ordonnance, Prescription, Medicament } from '../models/consultation.model';
import { HeaderComponent } from '../header-component/header.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ordonnance',
  imports: [HeaderComponent, CommonModule, FormsModule],
  templateUrl: './ordonnance.component.html',
  styleUrls: ['./ordonnance.component.css'],
})
export class OrdonnanceComponent {
  ordonnance: Ordonnance = {
    date_prescription: '',
    etat_ordonnance: false,
    prescriptions: [],
  };

  medicament: Medicament = {
    nom: '',
    description: '',
    prix: 0,
    quantite: 0,
  };

  prescription: Prescription = {
    dose: '',
    duree: '',
    medicament: this.medicament,
  };

  showModal: boolean = false;
  modalMessage: string = '';

  constructor(private router: Router) {}

  addPrescription(): void {
    if (this.medicament.nom && this.prescription.dose && this.prescription.duree) {
      const newPrescription: Prescription = {
        dose: this.prescription.dose,
        duree: this.prescription.duree,
        medicament: { ...this.medicament },
      };

      this.ordonnance.prescriptions.push(newPrescription);

      // Reset input fields
      this.medicament.nom = '';
      this.prescription.dose = '';
      this.prescription.duree = '';
    } else {
      this.modalMessage = 'Veuillez remplir tous les champs avant d’ajouter.';
      this.showModal = true;
    }
  }

  confirm(): void {
    if (this.ordonnance.prescriptions.length === 0) {
      this.modalMessage = 'Vous devez ajouter au moins une prescription avant de confirmer l’ordonnance.';
      this.showModal = true;
      return;
    }

    // Enregistrer l'ordonnance si au moins une prescription existe
    this.modalMessage = 'Ordonnance enregistrée avec succès.';
    this.showModal = true;

    // Simuler une redirection ou effectuer des actions supplémentaires
    this.router.navigate(['/']);
  }

  cancel(): void {
    this.ordonnance.prescriptions = [];
    this.router.navigate(['/']);
  }

  closeModal() {
    this.showModal = false;
  }
}
