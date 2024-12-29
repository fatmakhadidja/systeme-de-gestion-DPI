import { Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component'; 
import { LoginComponent } from './login/login.component';
import { RecherchePatientComponent } from './recherche-patient/recherche-patient.component';
import { CreationDPIComponent } from './creation-dpi/creation-dpi.component';
import { ConsulterDpiComponent } from './ConsultationDPI/consulter-dpi/consulter-dpi.component';
export const routes: Routes = [
    { path: '', component: LandingPageComponent},
    { path: 'login', component: LoginComponent },
    { path: 'recherche-patient', component: RecherchePatientComponent },
    {path: 'creation-dpi', component: CreationDPIComponent},
    // { path: 'ConsultationDPI/consulter-dpi', component: ConsulterDpiComponent },
    { path: '', redirectTo: '/recherche-patient', pathMatch: 'full' },
    {path: 'ConsultationDPI/consulter-dpi/:id',component: ConsulterDpiComponent}
];
