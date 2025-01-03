import { Component } from '@angular/core';
import { ConsultationService } from '../services/consultation.service';
import { HeaderComponent } from '../header-component/header.component';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BilanBiologique } from '../models/consultation.model';

@Component({
  selector: 'app-bilan-biologique',
  templateUrl: './bilan-biologique.component.html',
  imports: [ HeaderComponent, FormsModule, CommonModule ],
  styleUrls: ['./bilan-biologique.component.css']
})
export class BilanBiologiqueComponent {
  bilanBiologique : BilanBiologique ;

  showModal: boolean = false;
  modalMessage: string = '';

  constructor(private consultationService: ConsultationService, private router: Router) {
    this.bilanBiologique = this.consultationService.getConsultation().bilan_biologique;
  }

  closeModal() {
    this.showModal = false;
  }

  navigateToConsultation() {
    this.router.navigate(['/creation-consult']);
  }

  saveBilanBiologique() {
    // Vérifie si la description est vide
    if (!this.bilanBiologique.description.trim()) {
      this.modalMessage = 'La description du bilan est vide. Veuillez la remplir avant de confirmer. ';
      this.showModal = true;
    } else {
      // Ajouter ici la logique pour sauvegarder l'examen biologique
      this.consultationService.updateConsultation('bilan_biologique', this.bilanBiologique);
      this.modalMessage = 'Examen biologique enregistré avec succès !';
      this.showModal = true ;
      this.router.navigate(['/creation-consult']);
    }
  }
}