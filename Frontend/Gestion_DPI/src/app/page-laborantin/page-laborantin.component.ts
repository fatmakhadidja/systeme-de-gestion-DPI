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
import { Chart,CategoryScale,BarController, LinearScale, BarElement, Title, Tooltip, Legend} from 'chart.js';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { ColdObservable } from 'rxjs/internal/testing/ColdObservable';
interface Patient {
  nom: string;
  prenom: string;
}

export interface Resultats {
  date:string;
  description: string;
  rempli:boolean;
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


export class PageLaborantinComponent{
  patientControl = new FormControl<Patient | null>(null, Validators.required);
  selectFormControl = new FormControl('', Validators.required);
  patientSelecione: Patient | null = null;
  patients: Patient[] = [
    {nom: 'Boussaid', prenom: 'Meriem'},
    {nom: 'Bouderbala', prenom: 'Amira'},
    {nom: 'Agale', prenom: 'Imene'},
    {nom: 'Mendjel', prenom: 'Chahrazed'},
    {nom: 'Djerfi', prenom: 'Fatima'},
    {nom: 'Marouane', prenom: 'Meriem'},
  ];

  displayedColumns: string[] = ['date', 'description', 'resultat',];
  dataSource : Resultats[] =([
    { date: '12/2/2025', description: 'Hydrogen',  rempli:true },
    { date: '12/2/2025', description: 'Helium', rempli:false},
    { date: '12/2/2025', description: 'Lithium', rempli:true},
    { date: '12/2/2025', description: 'Beryllium', rempli:false},
    { date: '12/2/2025', description: 'Boron',  rempli:true},
    { date: '12/2/2025', description: 'Carbon',  rempli:false},
    { date: '12/2/2025', description: 'Nitrogen', rempli:true},
    { date: '12/2/2025', description: 'Oxygen',  rempli:false},
    { date: '12/2/2025', description: 'Fluorine', rempli:false},
    { date: '12/2/2025', description: 'Neon', rempli:false},
  ]);
  clickedRows = new Set<Resultats>();
  trackByPatient(index: number, patient: Patient): string {
    return `${patient.nom}-${patient.prenom}`; 
  }
//AFFICHER LES FENETRES

  readonly dialog = inject(MatDialog);

  openDialog_remplirResultat(): void {
    const dialogRef = this.dialog.open(RemplirResultat, {
      width: '80vw', 
      height: 'auto',  
      maxWidth: '80vw',
      data: {},
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
  // readonly data = inject<DialogData>(MAT_DIALOG_DATA);

   params :string[] = ['Glycémie',
    'Cholestérol total',
    'HDL',
   ' LDL ',
    'Triglycérides',
    'Créatinine',
    'Urée',
   ' Acide urique'
   ]

  onNoClick(): void {
    this.dialogRef.close();
  }
  readonly panelOpenState = signal(false);
  divs: { id: number; parametre: string; valeur: string ; unite: string}[] = [];
  nextId = 1;

  ajouter() {
    this.divs.push({ id: this.nextId++, parametre: '', valeur: '', unite:''});
  }

  deleteDiv(id: number) {
    this.divs = this.divs.filter(div => div.id !== id);
  }
  readonly dialog = inject(MatDialog);
  openDialog_genererGraphe(): void{
    const dialogRef = this.dialog.open(GenererGraphe, {
      width: '80vw', 
      height: 'auto',  
      maxWidth: '80vw',
      data: {},
    });
    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  isDisable: boolean = true; 
 
  enregistrer() {
    this.isDisable = false; 
    
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
  // readonly data = inject<DialogData>(MAT_DIALOG_DATA);

   graphe : Graphe[]=[
    {nom: 'Cholestérol total', valAnc: '12', valNouv:'7'},
    {nom: 'HDL', valAnc: '5', valNouv:'13'},
    {nom: ' LDL ', valAnc: '12', valNouv:'4'},
   ]

   chart: any;

   constructor() {
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

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    this.createChart();
  }

  createChart() {
    const labels = this.graphe.map(item => item.nom);
    const valAnc = this.graphe.map(item => parseFloat(item.valAnc));
    const valNouv = this.graphe.map(item => parseFloat(item.valNouv));

    const ctx = document.getElementById('barChart') as HTMLCanvasElement;  
    if (ctx) {
      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Ancien',
              data: valAnc,
              backgroundColor: 'rgb(33, 150, 243)',
              
              borderWidth: 1,
              barThickness: 'flex', 
              maxBarThickness: 50,
            },
            {
              label: 'Nouveau',
              data: valNouv,
              backgroundColor: 'rgb(76, 175, 80)',
              
              borderWidth: 1,
              barThickness: 'flex', 
              maxBarThickness: 50,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            x: {
              stacked: true,
              grid: {
                display: false, 
              }, 
            },

            y: {
              stacked: true,
            },
          },
        },
      });
    } else {
      console.error('Canvas element not found!');
    }
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
  
}