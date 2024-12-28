import { Routes } from '@angular/router';
import { BilanRadiologiqueComponent } from './bilan-radiologique/bilan-radiologique.component';
import { OrdonnanceComponent } from './ordonnance/ordonnance.component';
import { BilanBiologiqueComponent } from './bilan-biologique/bilan-biologique.component';
import { ResumeComponent } from './resume/resume.component';

export const routes: Routes = [
    { path: 'ordonnance', component: OrdonnanceComponent },
    { path: 'bilan-radiologique', component: BilanRadiologiqueComponent },
    { path: 'bilan-biologique', component: BilanBiologiqueComponent },
    { path: 'resume', component: ResumeComponent },
];
