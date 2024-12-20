import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LoginComponent } from "./login/login.component";
import {RecherchePatientComponent} from "./recherche-patient/recherche-patient.component";
import { LandingPageComponent } from './landing-page/landing-page.component';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, LoginComponent, RecherchePatientComponent, LandingPageComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
}
