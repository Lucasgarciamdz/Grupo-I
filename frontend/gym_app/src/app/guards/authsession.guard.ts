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
      const userRole = 'profesor'; //Chequear name de rol

      if (userRole === 'profesor') {
        this.router.navigateByUrl('/home-prof');
      } else {
        this.router.navigateByUrl('/profile');
      }
      return true;
    }
  }
}
