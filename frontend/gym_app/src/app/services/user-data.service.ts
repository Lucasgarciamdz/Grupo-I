import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserDataService {

  constructor() { }

  setUserData(userData: any) {
    localStorage.setItem('userData', JSON.stringify(userData));
  }

  getUserData() {
    const userData = localStorage.getItem('userData');
    if (userData) {
      return JSON.parse(userData);
    }
    return null;
  }
}
