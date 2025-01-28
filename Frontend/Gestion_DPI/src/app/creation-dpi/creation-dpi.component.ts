 import { Component } from '@angular/core';
import { HeaderComponent } from "../header-component/header.component";
import { CreationDPIService } from '../creation-dpi.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-creation-dpi',
  imports: [HeaderComponent, FormsModule],
  templateUrl: './creation-dpi.component.html',
  styleUrls: ['./creation-dpi.component.css']
})
export class CreationDPIComponent {
  title = "Création du DPI";
  labels = ["Nom", "Prénom", "Numéro de sécurité sociale", "Date de naissance", "Adresse", "Téléphone", "Mutuelle", "Médecin traitant", "Personne à contacter"];
  buttons = ["Ajouter le DPI", "Annuler"];
  names = ["nom", "prenom", "nss", "ddn", "adresse", "num_tel", "mutuelle", "medecin", "contact"];

  constructor(private creationDPIService: CreationDPIService) { }

  onSubmit(formData: any): void {
    // Log the form data to verify its structure
    console.log('Form Data:', formData);

    // Prepare the data object for the API call
    const dpiData = {
      nom_patient: formData.nom,
      prenom_patient: formData.prenom,
      nss: formData.nss,
      date_de_naissance: formData.ddn,
      adresse: formData.adresse,
      telephone: formData.num_tel,
      mutuelle: formData.mutuelle,
      personne_a_contacter: formData.contact,
      nom_complet_medecin: formData.medecin
    };

    console.log('DPI Data:', dpiData);

    // Call the service to create the DPI
    this.creationDPIService.createDPI(dpiData).subscribe({
      next: (response) => {
        console.log('DPI créé avec succès:', response);
        localStorage.setItem('dpi_id', response.dpi_id);
        alert('Le dossier a été créé avec succès.');
        window.location.reload();
      },
      error: (err) => {
        console.error('Erreur lors de la création du DPI:', err);
        if (err.error) {
          alert(`Erreur : ${err.error.message || 'Problème de validation ou serveur.'}`);
        } else {
          alert('Une erreur est survenue. Veuillez réessayer.');
        }
      }
    });
  }
}
