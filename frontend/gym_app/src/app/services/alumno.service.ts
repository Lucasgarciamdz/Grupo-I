import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
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
    return this.get<any[]>('alumnos');
  }

  getAlumno(id: number): Observable<any> {
    return this.get<any>(`alumno/${id}?full=1`);
  }

  updateAlumno(id: number, alumno: any): Observable<any> {
    return this.put<any>(`alumnos/${id}`, alumno);
  }

  deleteAlumno(id: number): Observable<any> {
    return this.delete<any>(`alumnos/${id}`);
  }

  getAlumnoFull(id: number): Observable<any> {
    return this.get<any>(`alumno/${id}?full=1`);
  }
}