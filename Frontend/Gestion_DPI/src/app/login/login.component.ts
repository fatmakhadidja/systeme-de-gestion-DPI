import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import { LoginService } from '../login.service';
@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  standalone:true
})
export class LoginComponent {
title = 'Connexion';
text='Bienvenue à Amejay, votre portail vers une gestion médicale simplifiée et efficace !';
label1 = `Nom d’Utilisateur`;
label2 = 'Votre mot de passe';
ph1=`Votre nom d'utilisateur`;
ph2='Votre mot de passe';
button='Se Connecter';

constructor(private loginService: LoginService) { }

// onLogin(usernameValue:string){
//   this.loginService.onLogin(usernameValue);
// }

}
