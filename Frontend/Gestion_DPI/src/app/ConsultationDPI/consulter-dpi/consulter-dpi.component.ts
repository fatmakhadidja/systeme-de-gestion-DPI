import { Component , OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatTableModule} from '@angular/material/table';
import { HeaderComponent } from '../../header-component/header.component';
import {OrdonnanceComponent} from '../ordonnance/ordonnance.component';
import { ResumeComponent } from '../resume/resume.component';
import { MatDialog } from '@angular/material/dialog';
import {ConsulterDpiService ,ListConsultation, ListSoins} from '../../services/consulter-dpi.service'
import { BilanBiologiqueComponent } from '../bilan-biologique/bilan-biologique.component';
import { BilanRadiologiqueComponent } from '../bilan-radiologique/bilan-radiologique.component';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient , HttpParams } from '@angular/common/http';
//import { provideHttpClient } from '@angular/common/http';

@Component({
  selector: 'app-consulter-dpi',
  imports: [CommonModule,MatTableModule,OrdonnanceComponent,HeaderComponent,HttpClientModule],
  templateUrl:'./consulter-dpi.component.html' ,
  styleUrl: './consulter-dpi.component.css',
  standalone: true
})
export class ConsulterDpiComponent implements OnInit{
 // items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
  //data = 12 ;
  antecedent = "bla bla bla ";
  displayedColumns: string[] = [ 'NConsultation','date', 'Ordo', 'Bilan_bio','Bilan_rad','Resume'];
  dataSource : ListConsultation[] = [];
  displayedColumns2: string[] = ['Date','Description','Observation'];
  dataSource2 : ListSoins[] = [];
 

  constructor(public dialog : MatDialog , private consulterDpiService : ConsulterDpiService , private http : HttpClient){} ;
  /*
  ngOnInit(): void {
    const dpi = 1 ;
    this.consulterDpiService.getListConsultation(dpi).subscribe({ 
      next: data => console.log(data),
       error: err => console.error(err)
    });

    this.consulterDpiService.getListSoins().subscribe(data => {
      this.dataSource2 = data;
    });
  }
*/
    ngOnInit(): void {
      const dpi = 1; // Remplacer par le DPI du patient
        this.consulterDpiService.getListConsultation(dpi).subscribe(data => {
        this.dataSource = data;
      }, error => {
        console.error('Erreur lors de la récupération des consultations:', error);
      });
      /*const params = new HttpParams().set('dpi', dpi.toString());
      this.http.get('http://127.0.0.1:8000/api/miseajourdpi/getConsultations/', {params}).subscribe({
        next: data => console.log(data),
        error: err => console.error(err)
      });*/
      this.consulterDpiService.getListSoins().subscribe(data => {
        this.dataSource2 = data;
      });
    }



  openOrdonnance(): void {
    this.dialog.open(OrdonnanceComponent, {
      width: '85%',
      height:'90%',
    });
  }
  openResume(): void {
    this.dialog.open(ResumeComponent, {
      width: '85%',
      height:'90%',
    });
  }
  openBilanBio(): void {
    this.dialog.open(BilanBiologiqueComponent, {
      width: '85%',
      height:'90%',
    });
  }
  openBilanRad(): void {
    this.dialog.open(BilanRadiologiqueComponent, {
      width: '85%',
      height:'90%',
    });
  }
}
