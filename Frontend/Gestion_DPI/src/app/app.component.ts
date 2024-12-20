import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PageInfirmierComponent } from './page-infirmier/page-infirmier.component';
import { HeaderComponent } from './header-component/header.component';
import { CreationConsultationComponent } from "./creation-consultation/creation-consultation.component";

@Component({
  selector: 'app-root', // the selector <app-root></app-root> is used to insert this component
  imports: [PageInfirmierComponent], //CreationConsultationComponent
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Gestion_DPI';
}
