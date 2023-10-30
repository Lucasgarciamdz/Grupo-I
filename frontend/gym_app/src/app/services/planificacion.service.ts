import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { BaseService } from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class PlanificacionService extends BaseService {
  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getPlanificaciones(): Observable<any[]> {
    const headers = this.getHeaders();
    return this.httpClient.get<any[]>(`${this.url}/planificaciones`, { headers });
  }


  // CREAR LA PLANI ES DE 1 PROFESOR A 1 ALUMNO
  // 1 ALUMNO N PLANIS

  // createPlanificacion(planificacion: any): Observable<any> {
  //   const headers = this.getHeaders();
  //   return this.httpClient.post<any>(`${this.url}/planificaciones`, planificacion, { headers });
  // }

  updatePlanificacion(id: number, planificacion: any): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.put<any>(`${this.url}/planificaciones/${id}`, planificacion, { headers });
  }

  deletePlanificacion(id: number): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.delete<any>(`${this.url}/planificaciones/${id}`, { headers });
  }

  getPlanificacionesByAlumnoId(alumnoId: number): Observable<any[]> {
    const headers = this.getHeaders();
    return this.httpClient.get<any[]>(`${this.url}/planificaciones?alumno_id_plani=${alumnoId}`, { headers });
  }
}
