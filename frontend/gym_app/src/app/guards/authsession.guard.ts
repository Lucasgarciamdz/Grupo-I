import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { JWTService } from '../services/jwt.service';

@Injectable({
  providedIn: 'root'
})
export class AuthsessionGuard implements CanActivate {
  constructor(
    private router: Router,
    private jwtService: JWTService
  ) {}

  canActivate(route: ActivatedRouteSnapshot): boolean {
    const token = localStorage.getItem('token') ?? '';
    this.jwtService.setToken(token);
    console.log("HOLA SOY EL GUARD Y ESTE ES EL TOKEN:", token);

    if (!token) {
      this.router.navigateByUrl('/home');
      return false;
    }

    if (this.jwtService.isTokenExpired()) {
      this.router.navigateByUrl('/home');
      return false;
    }

    const userRole = this.jwtService.getRol() ?? '';
    const requiredRoles = route.data['roles'] as string[];

    console.log("ESTE ES EL ROL:", userRole);
    console.log("ESTOS SON LOS ROLES REQUERIDOS", requiredRoles);

    if (requiredRoles.includes(userRole)) {
      return true;
    } else {
      this.router.navigateByUrl('/home');
      return false;
    }
  }
}