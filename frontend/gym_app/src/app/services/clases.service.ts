import { Injectable } from '@angular/core';
import {BaseService} from "./base.service";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ClasesService extends BaseService{

  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getClases(): Observable<any[]> {
    return this.get<any[]>('clases');
  }

  getClassById(id: number): Observable<any> {
    return this.getById<any>('clase', id);
  }

  putClase(id: number, clase: any): Observable<any> {
    return this.put<any>('clase', clase);
  }

  deleteClase(id: number): Observable<any> {
    return this.delete<any>('clase');
  }

  getClasesByAlumnoId(alumnoId: number): Observable<any[]> {
    return this.get<any[]>('clases', `alumno_id_clase=${alumnoId}`);
  }
}