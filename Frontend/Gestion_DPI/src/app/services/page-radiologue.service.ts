import { Injectable } from '@angular/core';
import { Observable,of } from 'rxjs';
import {  HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PageRadiologueService {
  private patienturl = 'http://127.0.0.1:8000/api/miseajourdpi/getPatients/';
 

  constructor(private http: HttpClient) { }

  //getListPatients(): Observable<any> {}
}
