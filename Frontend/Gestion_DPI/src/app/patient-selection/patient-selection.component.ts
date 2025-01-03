import { Component, EventEmitter, Output, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-patient-selection',
  imports: [CommonModule],
  templateUrl: './patient-selection.component.html',
  styleUrls: ['./patient-selection.component.css']
})
export class PatientSelectionComponent implements OnInit {
  @Output() patientSelected = new EventEmitter<number>(); // Emit the selected patient's ID

  patients: { id_patient: number; first_name: string; last_name: string }[] = []; // List of patients fetched from backend
  loading = true; // Indicator for loading state
  errorMessage = ''; // Error message if fetching fails

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchPatients();
  }

  fetchPatients(): void {
    const url = 'http://127.0.0.1:8000/api/miseajourdpi/getPatients/';

    this.http.get<{ id_patient: number; first_name: string; last_name: string }[]>(url).subscribe({
      next: (response) => {
        this.patients = response;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error fetching patients:', error);
        this.errorMessage = 'Erreur lors du chargement des patients.';
        this.loading = false;
      }
    });
  }

  onPatientChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    const selectedPatientId = Number(selectElement.value);
    this.patientSelected.emit(selectedPatientId); // Emit the selected patient ID
  }
}
