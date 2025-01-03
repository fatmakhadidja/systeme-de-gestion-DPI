import { Component } from '@angular/core';

import { RouterOutlet } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PageRadiologueComponent } from './Radiologue/page-radiologue/page-radiologue.component';
import { ConsulterDpiComponent } from './ConsultationDPI/consulter-dpi/consulter-dpi.component';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';




@Component({
  selector: 'app-root',

  imports: [CommonModule, RouterOutlet, LoginComponent,LandingPageComponent,PageRadiologueComponent,ConsulterDpiComponent],


  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = "Système de Gestion DPI - Amejay"
}
