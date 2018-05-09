import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user';
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  user: User = new User();
  constructor(private auth: AuthService, private router: Router) {}
  onLogin(): void {
    this.auth.login(this.user)
    .then((user) => {
      console.log(user.json());
      this.router.navigate(['/dashboard']);
    })
    .catch((err) => {
      console.log(err);
    });
  }
}
