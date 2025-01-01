import {Injectable}  from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class LaborantinService {
  private apiUrl = 'http://127.0.0.1:8000/api/biology/dpis/';
  private bilanUrl = 'http://127.0.0.1:8000/api/biology/dpi/int consult Id/biobilansparconsult/';

  constructor(private http: HttpClient) {}
  getPatientList(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
  getBilanList(): Observable<any> {
    return this.http.get(this.bilanUrl);
  }
}
