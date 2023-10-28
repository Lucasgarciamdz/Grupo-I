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

    // Create a HttpParams object to include query parameters
    let params = new HttpParams();
    params = params.set('minAge', minAge);
    params = params.set('maxAge', maxAge);

    // Include the params in the request
    return this.httpClient.get<T>(`${this.url}/usuarios/sort_by_edad`, { headers, params });
  }

  getUsersByRol<T>(rol: string): Observable<T> {
    const headers = this.getHeaders();

    // Create a HttpParams object to include the 'rol' query parameter
    let params = new HttpParams();
    params = params.set('rol', rol);

    // Include the params in the request
    return this.httpClient.get<T>(`${this.url}/usuarios/rol`, { headers, params });
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
