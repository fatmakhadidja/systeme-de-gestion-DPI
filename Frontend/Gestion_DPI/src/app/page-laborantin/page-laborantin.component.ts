import {ChangeDetectionStrategy, Component, inject, model, signal, AfterViewInit} from '@angular/core';import { HeaderComponent } from '../header-component/header.component';
import {FormControl, Validators, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import { CommonModule } from '@angular/common';
import {MatTableModule} from '@angular/material/table';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatButtonModule} from '@angular/material/button';
import {OnInit } from '@angular/core';
import { LaborantinService } from '../laborantin.service';
import { Chart,CategoryScale,BarController, LinearScale, BarElement, Title, Tooltip, Legend, UpdateModeEnum} from 'chart.js';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { ChangeDetectorRef } from '@angular/core';

import { ColdObservable } from 'rxjs/internal/testing/ColdObservable';

interface Patient{
  nom:string,
  prenom: string,
  id_dpi: number,
  bilans: Bilan[],
}

interface Bilan{
  blan_id:number,
  description: string,
  remplit: string,
}

@Component({
  selector: 'app-page-laborantin',
  imports: [HeaderComponent,
    MatFormFieldModule,
    MatSelectModule,
    FormsModule,
    MatInputModule,
    CommonModule,
    MatTableModule,
    ReactiveFormsModule,
  ],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './page-laborantin.component.html',
  styleUrl: './page-laborantin.component.css',
})


export class PageLaborantinComponent implements OnInit{
  patients: Patient[] = [];
  patientControl = new FormControl(null, Validators.required);
  patientSelecione: any;
  displayedColumns: string[] = ['description', 'resultat',];
  dataSource : any[] =[];
selectedBilanId: number | null = null;
  constructor(private laborantinService: LaborantinService,   private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.fetchPatients();
  }
  fetchPatients(): void {
    this.laborantinService.getPatientList().subscribe({
      next: (data) => {
        this.patients = data.map((item: any) => ({
          nom: item.utilisateur.last_name,
          prenom: item.utilisateur.first_name,
          id_dpi: item.id_dpi,
          bilans: [],
        }
      ));
    },
      error: (err) => console.error('Error fetching patients:', err),
    });
  }
  loadPatientData(): void {
    // Get the selected patient from the dropdown
    this.patientSelecione = this.patientControl.value;

    if (this.patientSelecione) {
      // Fetch bilans for the selected patient
      this.laborantinService.getBilanList(this.patientSelecione.id_dpi).subscribe({
        next: (data) => {
          // Map bilans and set as dataSource
          this.dataSource = data.map((item: any) => ({
            description: item.bilan.description,
            remplit: item.bilan.laborantin !== null,
            bilan_id: item.bilan.id_bilanbiologique,
          }));
          this.cdr.detectChanges();
        },
        error: (err) => console.error('Error fetching bilans for patient', err),
      });
    } else {
      // Clear dataSource if no patient is selected
      this.dataSource = [];
    }
  }



  clickedRows = new Set<any>();
  trackByPatient(index: number, patient: any): string {
    return `${patient.nom}-${patient.prenom}`; 
  }

  


// //AFFICHER LES FENETRES

  readonly dialog = inject(MatDialog);

  openDialog_remplirResultat(row: any): void {
    const dialogRef = this.dialog.open(RemplirResultat, {
      width: '80vw',
      height: 'auto',
      maxWidth: '80vw',
      data: { bilan_id: row.bilan_id, id_dpi: this.patientSelecione.id_dpi, }, // Pass bilan_id here
    });
  
    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  
}
@Component({
  selector: 'dialog-remplir-resultat',
  templateUrl: 'dialog-remplir-resultat.html',
  imports: [
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatDialogClose,
    MatExpansionModule,
    CommonModule,
    MatButtonModule
  ],
})


//REMPLIR RESULTATS
export class RemplirResultat {
  readonly dialogRef = inject(MatDialogRef<RemplirResultat>);
  readonly data = inject(MAT_DIALOG_DATA);

  params: { name: string; id: number }[] = [
    { id: 1, name:'Pression_arterielle' },
    { id: 2, name: 'Glycemie' },
    { id: 3, name: 'Niveau_cholesterol' },
  ];
   divs: { id: number; parametre: string; valeur: string ; date: string}[] = [];
   nextId = 1;
   isDisable: boolean = true; 

   constructor(private laborantinUpdate: LaborantinService){};
  
   onNoClick(): void {
    this.dialogRef.close();
  }
  readonly panelOpenState = signal(false);

  ajouter() {
    this.divs.push({ id: this.nextId++, parametre: '', valeur: '', date:''});
  }

  deleteDiv(id: number) {
    this.divs = this.divs.filter(div => div.id !== id);
  }
  readonly dialog = inject(MatDialog);
  openDialog_genererGraphe(): void {
    const newValues = this.divs.map((div) => ({
      parametre: div.parametre,
      valeur: div.valeur,
    }));
  
    const dialogRef = this.dialog.open(GenererGraphe, {
      width: '80vw',
      height: 'auto',
      maxWidth: '80vw',
      data: {
        id_dpi: this.data.id_dpi,
        newValues,
      },
    });
  }
  
 
  enregistrer() {
    this.isDisable = false;
    const mesures = this.divs.map(div => {
      // Find the ID for the entered parameter name
      const matchedParam = this.params.find(param => param.name === div.parametre);
      if (!matchedParam) {
        alert(`Paramètre "${div.parametre}" non valide`);
        throw new Error(`Invalid paramètre: ${div.parametre}`);
      }
  
      return {
        "id-mesure": matchedParam.id, // Send the ID of the parameter
        "valeur_mesure": div.valeur,
        "date_mesure": div.date,
      };
    });
  
    const bilan_id = this.data.bilan_id;
    const updateData = {
      bilan_id: bilan_id, // Include the bilan_id passed from the parent
      laborantin_id: 1,
      mesure: mesures,
    };
  
    this.laborantinUpdate.postBilanResultat(updateData).subscribe({
      next: response => {
        console.log("L'ajout des paramètres a réussi", response);
        // Show a success message (optional), but keep the dialog open
        alert("Les données ont été enregistrées avec succès.");
      },
      error: err => {
        console.log("L'ajout des paramètres a échoué", err);
        console.error("Failed to send data:", err.error); // Log the error body
      },
    });
  }
  
}


interface Graphe{
  nom : string;
  valAnc : string;
  valNouv : string
}
@Component({
  selector: 'dialog-generer-graphe',
  templateUrl: 'dialog-generer-graphe.html',
  imports: [
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatDialogClose,
    MatExpansionModule,
    CommonModule
  ],
})

export class GenererGraphe implements AfterViewInit{
  readonly dialogRef = inject(MatDialogRef<GenererGraphe>);
  readonly data = inject(MAT_DIALOG_DATA);

   grapheData : Graphe[]=[]
   newValues: any[] = [];
   chart: any;

   constructor(private laborantinService: LaborantinService) {
    Chart.register(
      CategoryScale, 
      LinearScale,    
      BarElement,     
      Title,          
      Tooltip,       
      Legend,
      BarController        
    );
    
  }


  ngAfterViewInit(): void {
    this.newValues = this.data.newValues || []; // Store new values
    this.fetchGraphData();
    }
    fetchGraphData(): void {
      const id_dpi = this.data.id_dpi; // Use the passed id_dpi
  
      this.laborantinService.getGraphData(id_dpi).subscribe({
        next: (response) => {
          console.log('Graph data fetched successfully:', response);
          this.combineGraphData(response, this.newValues); // Combine old and new values
          this.createChart();
        },
        error: (err) => {
          console.error('Error fetching graph data:', err);
        },
      });
    }
    combineGraphData(oldValues: any, newValues: any[]): void {
      // Ensure oldValues is an object with a 'parametres' array
      if (!oldValues || !Array.isArray(oldValues.parametres)) {
        console.error("Invalid oldValues format. Defaulting to empty array.");
        oldValues = { parametres: [] };
      }
    
      // Map through the parameters in oldValues
      this.grapheData = oldValues.parametres
        .filter((param: any) =>
          ["Glucose", "Cholesterol", "Pression_arterielle"].includes(param.nom)
        )
        .map((oldItem: any) => {
          const newItem = newValues.find(
            (newVal) => newVal.parametre === oldItem.nom
          );
    
          return {
            nom: oldItem.nom,
            valAnc: oldItem.valeur_mesuree, // Old value from parametres
            valNouv: newItem ? newItem.valeur : null, // New value (if available)
          };
        });
    
      console.log("Combined graph data:", this.grapheData);
    }
       
  
    createChart(): void {
      // Parameters to visualize
      const requiredParameters = ["Glucose", "Cholesterol", "Pression_arterielle"];
      const colors = {
        old: 'rgb(33, 150, 243)', // Blue for old values
        new: 'rgb(76, 175, 80)',  // Green for new values
      };
    
      // Iterate through each parameter to create individual charts
      requiredParameters.forEach((parameter) => {
        const data = this.grapheData.find((item) => item.nom === parameter);
    
        if (data) {
          const ctx = document.getElementById(`barChart`) as HTMLCanvasElement;
    
          if (ctx) {
            new Chart(ctx, {
              type: 'bar',
              data: {
                labels: ['Ancien (Old)', 'Nouveau (New)'], // Top (Old) and bottom (New) bars
                datasets: [
                  {
                    label: 'Ancien (Old Values)',
                    data: [parseFloat(data.valAnc)],
                    backgroundColor: colors.old,
                    barThickness: 'flex',
                    maxBarThickness: 50,
                  },
                  {
                    label: 'Nouveau (New Values)',
                    data: [parseFloat(data.valNouv || '0')], // Default to 0 if no new value
                    backgroundColor: colors.new,
                    barThickness: 'flex',
                    maxBarThickness: 50,
                  },
                ],
              },
              options: {
                responsive: true,
                indexAxis: 'y', // Vertical orientation (bars stack top to bottom)
                scales: {
                  x: {
                    beginAtZero: true,
                    grid: { display: false },
                  },
                  y: {
                    grid: { display: false },
                  },
                },
                plugins: {
                  legend: {
                    position: 'top',
                  },
                  title: {
                    display: true,
                    text: `Comparaison des Valeurs (${parameter})`, // Dynamic title per chart
                  },
                },
              },
            });
          } else {
            console.error(`Canvas element for ${parameter} not found!`);
          }
        } else {
          console.error(`No data found for parameter: ${parameter}`);
        }
      });
    }
    
    
  
    onNoClick(): void {
      this.dialogRef.close();
    }

  
}