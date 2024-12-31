import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Consultation } from '../models/consultation.model';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ConsultationApiService {
  private apiUrl = 'http://127.0.0.1:8000/api/miseajourdpi/ajouterConsultation/';

  constructor(private http: HttpClient) {}

  ajouterConsultation(consultation : Consultation): Observable<any> {
    const headers = new HttpHeaders({
        'Content-Type': 'application/json' // Set Content-Type to JSON
      });
    return this.http.post(this.apiUrl, consultation, { headers: headers })
  }
}
