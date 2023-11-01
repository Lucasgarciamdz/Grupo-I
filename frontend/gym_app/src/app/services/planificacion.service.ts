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


  updatePlanificacion(id: number, planificacion: any): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.put<any>(`${this.url}/planificaciones/${id}`, planificacion, { headers });
  }

  deletePlanificacion(id: number): Observable<any> {
    const headers = this.getHeaders();
    return this.httpClient.delete<any>(`${this.url}/planificaciones/${id}`, { headers });
  }

  getPlanificacionesPorClase(claseId: number): Observable<any[]> {
    const headers = this.getHeaders();
    return this.httpClient.get<any[]>(`${this.url}/clase/${claseId}/planificaciones`, { headers });
  }

}
