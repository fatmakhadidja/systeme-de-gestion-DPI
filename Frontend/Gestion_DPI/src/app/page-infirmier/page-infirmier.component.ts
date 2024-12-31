import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from '../header-component/header.component';
import { PatientSelectionComponent } from '../patient-selection/patient-selection.component';
import { SoinFormComponent } from '../soin-form/soin-form.component';
import { Soin } from '../models/soin.model';

@Component({
  selector: 'app-page-infirmier',
  imports: [HeaderComponent, PatientSelectionComponent, SoinFormComponent, CommonModule],
  templateUrl: './page-infirmier.component.html',
  styleUrls: ['./page-infirmier.component.css']
})
export class PageInfirmierComponent {
  patientSelected: number | null = null; // ID du patient sélectionné
  soins: Soin[] = []; // Liste des soins à enregistrer

  // Méthode appelée lorsque le patient est sélectionné
  onPatientSelected(patientId: number): void {
    this.patientSelected = patientId;
    this.soins = [];
  }

  // Update dans la méthode "addSoin" pour ajouter un ID unique à chaque soin
addSoin(): void {
  this.soins.push({ description: '', observation: '' });
}

// Update la méthode "updateSoinData" pour s'assurer que les données sont mises à jour correctement
updateSoinData(updatedSoin: { description: string; observation: string }, index: number): void {
  this.soins[index].description = updatedSoin.description;
  this.soins[index].observation = updatedSoin.observation;
}

  // Supprimer un soin à un index donné
  deleteSoin(index: number): void {
    this.soins.splice(index, 1);
  }

  // Annuler : Réinitialiser tout
  cancel(): void {
    this.patientSelected = null;
    this.soins = [];
    alert('Soins annulés!');
  }

  // Sauvegarder les soins
  save(): void {
    if (this.soins.length === 0) {
      alert('Aucun soin à enregistrer.');
      return;
    }
  
    console.log('Patient sélectionné :', this.patientSelected);
    console.log('Soins à sauvegarder :', this.soins);

    alert('Les soins ont été enregistrés avec succès!');
    this.patientSelected = null;
    this.soins = [];
  }
  
}
