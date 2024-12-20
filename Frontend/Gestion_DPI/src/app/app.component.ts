import { Component } from '@angular/core';
// import { RouterOutlet } from '@angular/router';
import { PageInfirmierComponent } from './page-infirmier/page-infirmier.component';

@Component({
  selector: 'app-root',
  imports: [PageInfirmierComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = "Système de Gestion DPI - Amejay"
}
