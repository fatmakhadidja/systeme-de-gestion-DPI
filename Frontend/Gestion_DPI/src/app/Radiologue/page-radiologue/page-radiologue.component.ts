import { Component } from '@angular/core';
import { HeaderComponent } from '../../header/header.component';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatDialog } from '@angular/material/dialog';
import { FenetreRadiologueComponent } from '../fenetre-radiologue/fenetre-radiologue.component';

@Component({
  selector: 'app-page-radiologue',
  imports: [HeaderComponent,CommonModule,MatTableModule],
  templateUrl: './page-radiologue.component.html',
  styleUrl: './page-radiologue.component.css'
})
export class PageRadiologueComponent {
  dropdownOpen = false;
  selectedValue: string | null = null;
  listPatients = [
    'Alice Dupont',
    'Jean Martin',
    'Sophie Bernard',
    'Paul Durand',
    'Nicolas Lambert',
    'Claire Rousseau',
    'Hugo Petit'
];
displayedColumns: string[] = ['Date', 'Type', 'Description', 'compteRendu'];
dataSource = [
  { date: '2023-12-01', type: 'Blood Test', description: 'Routine blood analysis', compteRendu: 'oui' },
  { date: '2023-12-05', type: 'X-Ray', description: 'Chest X-ray for examination', compteRendu: 'non' },
  { date: '2023-12-10', type: 'MRI', description: 'Brain MRI scan', compteRendu: 'oui' }
];

constructor(public dialog : MatDialog){} ;
  toggleDropdown() {
    this.dropdownOpen = !this.dropdownOpen;
  }

  selectItem(item: string) {
    this.selectedValue = item;
   // this.dropdownOpen = false;
   this.dropdownOpen = !this.dropdownOpen;
  }
  openRedactionCompteRendu(): void {
      
        this.dialog.open(FenetreRadiologueComponent, {
          width: '85%',
          height:'90%',
        });
    
  }
}
