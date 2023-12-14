import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { BaseService } from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class UsuariosService extends BaseService {

  private http: HttpClient;
  
  constructor(httpClient: HttpClient) {
    super(httpClient);
    this.http = httpClient;
  }

  getUsers(): Observable<any[]> {
    return this.get<any[]>('usuarios');
  }

  getUserById(id: number): Observable<any> {
    return this.getById<any>(`usuario`, id);
  }

  getUsersByAge(minAge: number, maxAge: number): Observable<any> {
    const params = `minAge=${minAge}&maxAge=${maxAge}`;
    return this.get<any>('usuarios', params);
  }

  getUsersByRol(rol: string): Observable<any> {
    const params = `rol=${rol}`;
    return this.get<any>('usuarios', params);
  }

  getClasses(): Observable<any[]> {
    return this.get<any[]>('clases');
  }

  putUser(id: number, user: any): Observable<any> {
    return this.put<any>(`usuario/${id}`, user);
  }

  createUser(user: any): Observable<any> {
    const headers = { 'content-type': 'application/json' }  
    const body = JSON.stringify(user);
    return this.http.post<any>('http://localhost:5000/usuario', body, {'headers':headers});
  }
  
  deleteUser(id: number): Observable<any> {
    return this.delete<any>(`usuario/${id}`);
  }
}