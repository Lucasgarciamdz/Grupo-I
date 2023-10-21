import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { BaseService } from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class AlumnoService extends BaseService {
  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getAlumnos(): Observable<any[]> {
    const headers = this.getHeaders();
    return this.httpClient.get<any[]>(`${this.url}/alumnos`, { headers });
  }

  // createAlumno(alumno: any): Observable<any> {
  //   const headers = this.getHeaders();
  //   return this.httpClient.post<any>(`${this.url}/alumnos`, alumno, { headers });
  // }

  updateAlumno(id: number, alumno: any): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.put<any>(`${this.url}/alumnos/${id}`, alumno, { headers });
  }

  deleteAlumno(id: number): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.delete<any>(`${this.url}/alumnos/${id}`, { headers });
  }
}
