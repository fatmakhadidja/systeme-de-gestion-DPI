import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from '../header-component/header.component';
import { PatientSelectionComponent } from '../patient-selection/patient-selection.component';
import { SoinFormComponent } from '../soin-form/soin-form.component';
import { Soin } from '../models/soin.model';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-page-infirmier',
  imports: [HeaderComponent, PatientSelectionComponent, SoinFormComponent, CommonModule],
  templateUrl: './page-infirmier.component.html',
  styleUrls: ['./page-infirmier.component.css']
})
export class PageInfirmierComponent {
  patientSelected: number | null = null; // ID du patient sélectionné
  soins: Soin[] = []; // Liste des soins à enregistrer
  infirmierId: number = 1; // ID constant de l'infirmier
  apiUrl: string = 'http://127.0.0.1:8000/api/miseajourdpi/remplirSoin/';

  constructor(private http: HttpClient) {}

  // Méthode appelée lorsque le patient est sélectionné
  onPatientSelected(patientId: number): void {
    this.patientSelected = patientId;
    this.soins = [];
  }

  addSoin(): void {
    this.soins.push({ description: '', observation: '' });
  }

  updateSoinData(updatedSoin: { description: string; observation: string }, index: number): void {
    this.soins[index].description = updatedSoin.description;
    this.soins[index].observation = updatedSoin.observation;
  }

  deleteSoin(index: number): void {
    this.soins.splice(index, 1);
  }

  cancel(): void {
    this.patientSelected = null;
    this.soins = [];
    alert('Soins annulés!');
  }

  save(): void {
    if (this.soins.length === 0) {
      alert('Aucun soin à enregistrer.');
      return;
    }

    if (!this.patientSelected) {
      alert('Veuillez sélectionner un patient avant de sauvegarder.');
      return;
    }

    // Save each soin one by one
    this.soins.forEach((soin, index) => {
      const soinData = {
        patient: this.patientSelected,
        infirmier: this.infirmierId,
        description: soin.description,
        observation: soin.observation
      };

      this.http.post(this.apiUrl, soinData)
        .pipe(
          catchError(error => {
            console.error(`Erreur lors de l’enregistrement du soin ${index + 1}:`, error);
            alert(`Erreur lors de l’enregistrement du soin ${index + 1}`);
            return of(null); // Return an observable to allow the loop to continue
          })
        )
        .subscribe(response => {
          console.log(`Soin ${index + 1} enregistré avec succès:`, response);
        });
    });

    alert('Les soins ont été enregistrés avec succès!');
    this.patientSelected = null;
    this.soins = [];
  }
}
