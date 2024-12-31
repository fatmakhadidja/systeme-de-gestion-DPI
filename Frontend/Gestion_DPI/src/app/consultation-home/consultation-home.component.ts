import { Component } from '@angular/core';
import { ConsultationService } from '../services/consultation.service';
import { HeaderComponent } from '../header-component/header.component';
import { CommonModule } from '@angular/common';
import { Consultation } from '../models/consultation.model';

@Component({
  selector: 'app-consultation-home',
  templateUrl: './consultation-home.component.html',
  imports: [HeaderComponent, CommonModule],
  styleUrls: ['./consultation-home.component.css'],
})
export class ConsultationHomeComponent {
  consultation: Consultation;
  showWarning: boolean = false;

  constructor(private consultationService: ConsultationService) {
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
      alert('Consultation enregistrée avec succès !');
      // Implement save logic here
    }
  }
}
