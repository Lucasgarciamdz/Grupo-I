import { Injectable } from '@angular/core';
import jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class JWTService {

  jwtToken: string | undefined;
  decodedToken: { [key: string]: string; } | undefined;

  constructor() {
  }

  setToken(token: string) {
    if (token) {
      this.jwtToken = token;
    }
  }

  decodeToken(): { [key: string]: string; } | undefined {
    if (this.jwtToken) {
      return jwt_decode(this.jwtToken);
    }
    return undefined;
  }

  getDecodeToken(): { [key: string]: string; } | undefined {
    return this.decodedToken;
  }

  getRol(): string | null {
    const decodedToken = this.decodeToken();
    console.log("ESTE ES EL TOKEN DECODIFICADO:", decodedToken);
    return decodedToken ? decodedToken['rol'] : null;
  }

  getEmailId(): string | null {
    const decodedToken = this.decodeToken();
    return decodedToken ? decodedToken['email'] : null;
  }
  
  getId(): string | null {
    const decodedToken = this.decodeToken();
    return decodedToken ? decodedToken['id'] : null;
  }

  getExpiryTime(): number | null {
    const decodedToken = this.decodeToken();
    return decodedToken ? parseInt(decodedToken['exp'], 10) : null;
  }

  isTokenExpired(): boolean {
    const expiryTime: number | null = this.getExpiryTime();
    if (expiryTime) {
      return ((1000 * expiryTime) - (new Date()).getTime()) < 5000;
    } else {
      return false;
    }
  }
}