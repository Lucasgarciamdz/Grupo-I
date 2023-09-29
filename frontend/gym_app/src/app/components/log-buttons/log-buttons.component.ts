import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-log-button',
  templateUrl: './log-buttons.component.html',
  styleUrls: ['./log-buttons.component.css']
})
export class LogButtonComponent {

  constructor(
    private authService: AuthService
    ) {}

  get isToken() {
    return localStorage.getItem('token');
  }

  cerrarSesion() {
    this.authService.logout();
  }
}
