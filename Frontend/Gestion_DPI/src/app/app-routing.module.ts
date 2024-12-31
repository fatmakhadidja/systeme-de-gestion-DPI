import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ConsultationHomeComponent } from './consultation-home/consultation-home.component';
import { ResumeComponent } from './resume/resume.component';
import { OrdonnanceComponent } from './ordonnance/ordonnance.component';
import { BilanBiologiqueComponent } from './bilan-biologique/bilan-biologique.component';
import { BilanRadiologiqueComponent } from './bilan-radiologique/bilan-radiologique.component';

const routes: Routes = [
  { path: '', component: ConsultationHomeComponent },
  { path: 'resume', component: ResumeComponent },
  { path: 'ordonnance', component: OrdonnanceComponent },
  { path: 'bilan-biologique', component: BilanBiologiqueComponent },
  { path: 'bilan-radiologique', component: BilanRadiologiqueComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }