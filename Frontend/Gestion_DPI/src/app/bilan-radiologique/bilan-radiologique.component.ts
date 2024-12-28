import { Component } from '@angular/core';
import { HeaderComponent } from '../header-component/header.component';
import { ConsultationService } from '../services/consultation.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { BilanRadiologique } from '../models/consultation.model';

@Component({
  selector: 'app-bilan-radiologique',
  templateUrl: './bilan-radiologique.component.html',
  imports: [HeaderComponent, FormsModule, CommonModule],
  styleUrls: ['./bilan-radiologique.component.css']
})
export class BilanRadiologiqueComponent {
  bilanRadiologique : BilanRadiologique ;

  showModal: boolean = false;
  modalMessage: string = '';

  constructor(private consultationService: ConsultationService, private router: Router) {
    this.bilanRadiologique = this.consultationService.getConsultation().bilan_radiologique;
  }

  saveBilanRadiologique() {
    if (!this.bilanRadiologique.type && !this.bilanRadiologique.description) {
      this.modalMessage = 'Veuillez remplir le bilan et sélectionner un type avant d\'enregistrer.';
      this.showModal = true ;
    } else {
    if (!this.bilanRadiologique.type) {
      this.modalMessage = 'Veuillez sélectionner un type de bilan radiologique.';
      this.showModal = true ;
    } else {

    if (!this.bilanRadiologique.description) {
      this.modalMessage = 'Veuillez remplir le bilan avant de l\'enregistrer.';
      this.showModal = true ;
    } else {

    this.consultationService.updateConsultation('bilan_radiologique', this.bilanRadiologique);
    this.modalMessage = 'Bilan radiologique enregistré !';
    this.showModal = true ;
    }
  }
  }
  }

  navigateToConsultation() {
    this.router.navigate(['/consultation-home']); // Remplacez par la route correcte
  }

  closeModal() {
    this.showModal = false;
  }
}
