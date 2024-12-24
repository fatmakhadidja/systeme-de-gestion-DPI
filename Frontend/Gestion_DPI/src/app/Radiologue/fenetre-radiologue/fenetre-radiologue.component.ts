import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatDialogContent , MatDialogActions, MatDialogClose , MatDialogTitle, MatDialogContainer  } from '@angular/material/dialog';

@Component({
  selector: 'app-fenetre-radiologue',
  imports: [MatDialogContent ,
    MatDialogActions,
    MatDialogClose , 
    MatDialogTitle ,
    CommonModule,
    MatDialogContainer],
  templateUrl: './fenetre-radiologue.component.html',
  styleUrl: './fenetre-radiologue.component.css'
})
export class FenetreRadiologueComponent {
  
  files: File[] = []; // Liste des fichiers sélectionnés

  // Gestionnaire pour sélectionner plusieurs fichiers
  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;

    if (input.files && input.files.length > 0) {
      // Ajoute les nouveaux fichiers sélectionnés à la liste existante
      Array.from(input.files).forEach(file => {
        this.files.push(file);
      });
    }
  }

  // Fonction simulée pour uploader les fichiers (peut être reliée au backend)
  uploadFiles() {
    if (this.files.length > 0) {
      console.log('Fichiers sélectionnés :', this.files);
      alert(`${this.files.length} fichier(s) chargé(s) avec succès !`);
    } else {
      alert('Aucun fichier sélectionné.');
    }
  }
}
  