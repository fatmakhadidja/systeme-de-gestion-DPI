import { Component, OnInit } from '@angular/core';
import { ConsultationService } from '../services/consultation.service';
import { HeaderComponent } from '../header-component/header.component';
import { CommonModule } from '@angular/common';
import { Consultation } from '../models/consultation.model';
import { ConsultationApiService } from '../services/consultation-api.service';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-consultation-home',
  templateUrl: './consultation-home.component.html',
  imports: [HeaderComponent, CommonModule],
  styleUrls: ['./consultation-home.component.css'],
})
export class ConsultationHomeComponent implements OnInit {
  consultation: Consultation;
  
  showModal: boolean = false;
  modalMessage: string = '';
  showWarning = false ;

  constructor(
    private route: ActivatedRoute,
    private consultationService: ConsultationService,
    private consultationApiService: ConsultationApiService,
    private router: Router
  ) {
    this.consultation = this.consultationService.getConsultation();
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      let nss = params['nss'];

      if (nss) {
        // Store the retrieved NSS in localStorage
        localStorage.setItem('nss', nss);
        console.log('NSS stored in localStorage:', nss);
        
      } else {
        // Retrieve NSS from localStorage if not provided in the route
        nss = localStorage.getItem('nss');
        console.log('NSS retrieved from localStorage:', nss);
      }

      if (nss) {
        // Update the service with the NSS
        this.consultationService.updateConsultation('nss', nss);
        console.log('NSS updated in service:', nss);
      } else {
        console.warn('No NSS found in queryParams or localStorage.');
      }
    });
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
      this.showWarning = true ;
    } else {
      // Hide the warning and proceed with saving
    this.showWarning = false;

    // Log the consultation object to check the structure
    const consultation = this.consultationService.getConsultation();
    console.log('Consultation to send:', consultation);
    
    this.consultationApiService.ajouterConsultation(consultation).subscribe({
      next: () => {
        this.modalMessage = 'Consultation enregistrée avec succès.';
        this.showModal = true;
        this.router.navigate(['/recherche-patient']); // Redirect to the desired page after saving
      },
      error: (error) => {
        console.error('Erreur lors de l\'enregistrement de la consultation :', error);
        this.modalMessage = 'Une erreur s\'est produite. Veuillez réessayer.';
        this.showModal = true;
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

  closeModal() {
    this.showModal = false;
  }
}
