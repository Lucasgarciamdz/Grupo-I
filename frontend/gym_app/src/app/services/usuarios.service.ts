import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
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
