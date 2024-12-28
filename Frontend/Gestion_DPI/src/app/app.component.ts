import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PageRadiologueComponent } from './Radiologue/page-radiologue/page-radiologue.component';
import { ConsulterDpiComponent } from './ConsultationDPI/consulter-dpi/consulter-dpi.component';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,LandingPageComponent,PageRadiologueComponent,ConsulterDpiComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
}
