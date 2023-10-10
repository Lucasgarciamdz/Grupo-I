import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BaseService {
  protected url = '/api';

  private headers= this.getHeaders();

  constructor(protected httpClient: HttpClient) {}

  protected getHeaders(): HttpHeaders {
    const auth_token = localStorage.getItem('token');

    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  }

  public get<T>(endpoint: string): Observable<T> {
    return this.httpClient.get<T>(`${this.url}/${endpoint}`, {
      headers: this.headers
    });
  }

  public post<T>(endpoint: string, body: any): Observable<T> {
    return this.httpClient.post<T>(`${this.url}/${endpoint}`, body, {
      headers: this.headers
    });
  }

  public put<T>(endpoint: string, body: any): Observable<T> {
    return this.httpClient.put<T>(`${this.url}/${endpoint}`, body, {
      headers: this.headers
    });
  }

  public delete<T>(endpoint: string): Observable<T> {
    return this.httpClient.delete<T>(`${this.url}/${endpoint}`, {
      headers: this.headers
    });
  }

}
