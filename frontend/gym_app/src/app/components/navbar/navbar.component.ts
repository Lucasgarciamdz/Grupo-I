import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})

export class NavbarComponent {
    userRole: string;

    constructor(private jwtService: JWTService) {
    const token = localStorage.getItem('token') ?? '';
    this.jwtService.setToken(token);
    this.userRole = this.jwtService.getRol() ?? '';
  }
}
