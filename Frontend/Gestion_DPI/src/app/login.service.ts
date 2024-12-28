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
  // if(usernameValue === 'meriem'){
  //   console.log('clicked')
  //   this.router.navigate(['/recherche-patient']);
  //   console.log(usernameValue);
  // }
  // if(usernameValue==='amira'){
  //   console.log('clicked')
  //   this.router.navigate(['/creation-dpi']);
  //   console.log(usernameValue);
  // }
}
}
