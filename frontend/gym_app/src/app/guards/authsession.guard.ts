import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthsessionGuard implements CanActivate {
  constructor(private router: Router) {}

  canActivate(): boolean {
    const token = localStorage.getItem('token');

    if (!token) {
      this.router.navigateByUrl('/home');
      return false;
    } else {
      const userRole = localStorage.getItem('role'); // Obtener el rol del usuario desde el local storage

      if (userRole === 'profesor') {
        this.router.navigateByUrl('/home-prof');
      } else if (userRole === 'admin') {
        this.router.navigateByUrl('/home-admin'); // Ruta para administradores
      } else {
        this.router.navigateByUrl('/profile');
      }
      return true;
    }
  }
}
