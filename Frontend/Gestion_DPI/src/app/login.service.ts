import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private apiUrl = 'http://127.0.0.1:8000/api/v1/auth/login/';

  constructor(private http: HttpClient, private router: Router) {}

login(email: string, password:string):Observable<any>{
    return this.http.post(this.apiUrl, {email,password});
}

handleLoginSuccess(response: any): void {
    const  {role, id, full_name}= response;

    // Store tokens if needed
    localStorage.setItem('fullname', response.full_name);
    localStorage.setItem('id', response.id);
    localStorage.setItem('access_token', response.access_token);
    localStorage.setItem('refresh_token', response.refresh_token);

    // Navigate based on the user's role
    if (role === 'admin') {
      this.router.navigate(['/creation-dpi']);
    }if (role === 'patient') {
      this.router.navigate(['']);
    }else if (role === 'medecin') {
      this.router.navigate(['/creation-consult']); //recherche-patient
    } else if (role === 'infirmier') {
      this.router.navigate(['/soins-infirmiers']);
    } else if (role === 'pharmacien'){
      this.router.navigate(['']);
    }else if (role === 'laborantin'){
      this.router.navigate(['/page-laborantin']);
    } else if (role === 'radiologue'){
      this.router.navigate(['']);
    }
  }
}
