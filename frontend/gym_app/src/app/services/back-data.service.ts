import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BackendDataService {
  private apiUrl = '##';  // Reemplaza con la URL de tu backend

  constructor(private http: HttpClient) {}

  getStudents(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/students`);
  }

  getClasses(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/classes`);
  }
}
