import { Routes } from '@angular/router';
import { BilanRadiologiqueComponent } from './bilan-radiologique/bilan-radiologique.component';
import { OrdonnanceComponent } from './ordonnance/ordonnance.component';
import { BilanBiologiqueComponent } from './bilan-biologique/bilan-biologique.component';
import { ResumeComponent } from './resume/resume.component';
import { LandingPageComponent } from './landing-page/landing-page.component'; 
import { LoginComponent } from './login/login.component';
import { RecherchePatientComponent } from './recherche-patient/recherche-patient.component';

export const routes: Routes = [
    { path: 'ordonnance', component: OrdonnanceComponent },
    { path: 'bilan-radiologique', component: BilanRadiologiqueComponent },
    { path: 'bilan-biologique', component: BilanBiologiqueComponent },
    { path: 'resume', component: ResumeComponent },
    { path: '', component: LandingPageComponent},
    { path: 'login', component: LoginComponent },
    { path: 'recherche-patient', component: RecherchePatientComponent },
];
