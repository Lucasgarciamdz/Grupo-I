import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-log-button',
  templateUrl: './log-buttons.component.html',
  styleUrls: ['./log-buttons.component.css']
})
export class LogButtonComponent {

  constructor(
    private authService: AuthService,
    private router: Router
    ) {}

  get isToken() {
    return localStorage.getItem('token');
  }

  cerrarSesion() {
    this.authService.logout();
  }
}