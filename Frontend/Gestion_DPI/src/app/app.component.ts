import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import {ConsulterDpiComponent} from './ConsultationDPI/consulter-dpi/consulter-dpi.component'
import { HeaderComponent } from './header/header.component';

import { PageRadiologueComponent } from './Radiologue/page-radiologue/page-radiologue.component';





@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ConsulterDpiComponent,PageRadiologueComponent],

  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Gestion_DPI';
}
