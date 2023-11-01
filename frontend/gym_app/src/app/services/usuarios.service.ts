import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';
import {BaseService} from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class UsuariosService extends BaseService {
  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getUsers(): Observable<any[]> {
    const headers = this.getHeaders();

    return this.httpClient.get<any[]>(`${this.url}/usuarios`, {headers});
  }

  getUserById<T>(id: number): Observable<T> {
    const headers = this.getHeaders();

    return this.httpClient.get<T>(`${this.url}/usuario/${id}`, {headers});
  }

  getUsersByAge<T>(minAge: number, maxAge: number): Observable<T> {
    const headers = this.getHeaders();

    let params = new HttpParams();
    params = params.set('minAge', minAge);
    params = params.set('maxAge', maxAge);

    return this.httpClient.get<T>(`${this.url}/usuarios`, { headers, params });
  }

  getUsersByRol<T>(rol: string): Observable<T> {
    const headers = this.getHeaders();

    let params = new HttpParams();
    params = params.set('rol', rol);

    return this.httpClient.get<T>(`${this.url}/usuarios?rol=${rol}`, { headers });

  }

  getClasses(): Observable<any[]> {
    const headers = this.getHeaders();

    return this.httpClient.get<any[]>(`${this.url}/clases`, {headers});
  }

  putUser(id: number, user: any): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.put<any>(`${this.url}/usuario/${id}`, user, {headers});
  }

  deleteUser(id: number): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.delete<any>(`${this.url}/usuario/${id}`, {headers});
  }
}
