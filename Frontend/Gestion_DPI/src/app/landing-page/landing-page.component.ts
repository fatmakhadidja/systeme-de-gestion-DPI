import { Component } from '@angular/core';
import { Router, RouterLink, RouterLinkActive } from '@angular/router';
import { MainHeaderComponent } from '../main-header/main-header.component';
import {ChangeDetectionStrategy} from '@angular/core';
import {MatCardModule} from '@angular/material/card';
@Component({
  selector: 'app-landing-page',
  imports: [MainHeaderComponent, MatCardModule, RouterLink, RouterLinkActive],
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.css',
  standalone:true
})
export class LandingPageComponent {
}
