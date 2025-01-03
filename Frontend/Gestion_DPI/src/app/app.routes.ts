import { Routes } from '@angular/router';
import { BilanRadiologiqueComponent } from './bilan-radiologique/bilan-radiologique.component';
import { OrdonnanceComponent } from './ordonnance/ordonnance.component';
import { BilanBiologiqueComponent } from './bilan-biologique/bilan-biologique.component';
import { ResumeComponent } from './resume/resume.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { RecherchePatientComponent } from './recherche-patient/recherche-patient.component';
<<<<<<< HEAD
import { CreationDPIComponent } from './creation-dpi/creation-dpi.component';
import { ConsulterDpiComponent } from './ConsultationDPI/consulter-dpi/consulter-dpi.component';
<<<<<<< HEAD
import { ConsultationHomeComponent } from './consultation-home/consultation-home.component';
=======
import { ConsultationHomeComponent } from './consultation-home/consultation-home.component';
import { CreationDPIComponent } from './creation-dpi/creation-dpi.component';
import { ConsulterDpiComponent } from './ConsultationDPI/consulter-dpi/consulter-dpi.component';
import { PageRadiologueComponent } from './Radiologue/page-radiologue/page-radiologue.component';
>>>>>>> e46932016749790127e376879d64d413e26e6483
import { PageInfirmierComponent } from './page-infirmier/page-infirmier.component';

=======
import { PageLaborantinComponent } from './page-laborantin/page-laborantin.component';
>>>>>>> mary
export const routes: Routes = [
    { path: 'ordonnance', component: OrdonnanceComponent },
    { path: 'bilan-radiologique', component: BilanRadiologiqueComponent },
    { path: 'bilan-biologique', component: BilanBiologiqueComponent },
    { path: 'resume', component: ResumeComponent },
    { path: '', component: LandingPageComponent},
    { path: 'login', component: LoginComponent },
    { path: 'recherche-patient', component: RecherchePatientComponent },


    {path: 'creation-dpi', component: CreationDPIComponent},
    { path : 'creation-consult', component : ConsultationHomeComponent},
    { path : 'soins-infirmiers', component : PageInfirmierComponent},
    // { path: 'ConsultationDPI/consulter-dpi', component: ConsulterDpiComponent },
    // { path: '', redirectTo: '/recherche-patient', pathMatch: 'full' },
<<<<<<< HEAD
    {path: 'ConsultationDPI/consulter-dpi/:id',component: ConsulterDpiComponent},
    {path: 'page-laborantin', component: PageLaborantinComponent},
=======
    {path: 'ajouter-consult',component:ConsultationHomeComponent},
    {path: 'consulter-dpi/:id/:role',component: ConsulterDpiComponent},
    {path:'page-radiologue' , component: PageRadiologueComponent}
>>>>>>> e46932016749790127e376879d64d413e26e6483
];

   



