import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private router: Router){};

onLogin(usernameValue:string):void{
  //navigate to page based on the role

  //admin creer dpi
  //medecin consulter et cree dpi
  // if(email === 'meriem'){
  //   console.log('clicked')
  //   this.router.navigate(['/recherche-patient']);
  //   console.log(usernameValue);
  // }
  // if(email==='amira'){
  //   console.log('clicked')
  //   this.router.navigate(['/creation-dpi']);
  //   console.log(usernameValue);
  // }
}
}
