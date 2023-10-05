import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {
  private url = '/api';

  constructor(private httpClient: HttpClient) {}

  getUsers(): Observable<any[]> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.get<any[]>(`${this.url}/usuarios`, { headers });
  }

  getClasses(): Observable<any[]> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.get<any[]>(`${this.url}/clases`, { headers });
  }
}
