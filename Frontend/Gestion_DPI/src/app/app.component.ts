import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PageLaborantinComponent } from './page-laborantin/page-laborantin.component';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, PageLaborantinComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
}
