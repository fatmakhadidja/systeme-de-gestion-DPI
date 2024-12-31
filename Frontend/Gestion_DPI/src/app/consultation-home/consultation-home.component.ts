import { Component } from '@angular/core';
import { ConsultationService } from '../services/consultation.service';
import { HeaderComponent } from '../header-component/header.component';
import { CommonModule } from '@angular/common';
import { Consultation } from '../models/consultation.model';
import { ConsultationApiService } from '../services/consultation-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-consultation-home',
  templateUrl: './consultation-home.component.html',
  imports: [HeaderComponent, CommonModule],
  styleUrls: ['./consultation-home.component.css'],
})
export class ConsultationHomeComponent {
  consultation: Consultation;
  showWarning: boolean = false;

  constructor(
    private consultationService: ConsultationService,
    private consultationApiService: ConsultationApiService,
    private router: Router) {
    this.consultation = this.consultationService.getConsultation();
  }

  // Function to check if the résumé is valid
  isResumeValid(): boolean {
    const resume = this.consultation?.resume;
    if (!resume) {
      return false; // Resume object is missing
    }
    // Check if required fields are empty
    return !!(
      resume.diagnostic?.trim() &&
      resume.symptomes?.trim() &&
      resume.antecedents?.trim()
    );
  }

  // Save handler
  handleSave() {
    if (!this.isResumeValid()) {
      // Show warning if the résumé is invalid
      this.showWarning = true;
    } else {
      // Hide the warning and proceed with saving
    this.showWarning = false;

    // Log the consultation object to check the structure
    const consultation = this.consultationService.getConsultation();
    console.log('Consultation to send:', consultation);
    
    this.consultationApiService.ajouterConsultation(consultation).subscribe({
      next: () => {
        alert('Consultation enregistrée avec succès.');
        this.router.navigate(['/recherche-patient']); // Redirect to the desired page after saving
      },
      error: (error) => {
        console.error('Erreur lors de l\'enregistrement de la consultation :', error);
        alert('Une erreur s\'est produite. Veuillez réessayer.');
      },
    });     
    }
  }

  handleButton1() {
    this.router.navigate(['/resume']);
  }

  handleButton2() {
    this.router.navigate(['/bilan-biologique']);
  }

  handleButton3() {
    this.router.navigate(['/bilan-radiologique']);
  }

  handleButton4() {
    this.router.navigate(['/ordonnance']);
  }
}
