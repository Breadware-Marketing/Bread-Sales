import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user';
import { Router } from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  user: User = new User();

  constructor(private auth: AuthService, private router: Router) { }

  onRegister(): void {
    this.auth.register(this.user)
    .then((user) => {
      localStorage.setItem('token', user.json().auth_token);
      console.log(user.json());
      this.router.navigate(['/dashboard']);
    })
    .catch((err) => {
      console.log(err);
    });
  }

  goToLogin(){
    this.router.navigate(['/login']);
  }

}
