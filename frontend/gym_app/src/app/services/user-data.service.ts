import { Injectable } from '@angular/core';

export interface UserData {
  nombre: string;
  apellido: string;
  email: string;
  telefono: number;
  sexo: string;
  direccion: string;
  edad: number;
  dni: number;
  rol: string;
  id_usuario: number;
}

@Injectable({
  providedIn: 'root',
})
export class UserDataService {
  private userData: UserData = {
    nombre: '',
    apellido: '',
    email: '',
    telefono: 0,
    sexo: '',
    direccion: '',
    edad: 0,
    dni: 0,
    rol: '',
    id_usuario: 0,
  };

  setUserData(data: UserData) {
    this.userData = data;
  }

  getUserData(): UserData {
    return this.userData;
  }
}
