import { Component } from '@angular/core';
// import { RouterOutlet } from '@angular/router';
import { PageInfirmierComponent } from './page-infirmier/page-infirmier.component';
import { ConsultationHomeComponent } from "./consultation-home/consultation-home.component";
import { ResumeComponent } from './resume/resume.component';
import { BilanBiologiqueComponent } from "./bilan-biologique/bilan-biologique.component";
import { BilanRadiologiqueComponent } from "./bilan-radiologique/bilan-radiologique.component";
import { OrdonnanceComponent } from "./ordonnance/ordonnance.component";

@Component({
  selector: 'app-root',
  imports: [ConsultationHomeComponent, ResumeComponent, BilanBiologiqueComponent, BilanRadiologiqueComponent, OrdonnanceComponent],
import { RouterOutlet,RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = "Système de Gestion DPI - Amejay"
}
