import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
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
    return this.get<any[]>('planificaciones');
  }

  updatePlanificacion(id: number, planificacion: any): Observable<any> {
    return this.put<any>(`planificaciones/${id}`, planificacion);
  }

  deletePlanificacion(id: number): Observable<any> {
    return this.delete<any>(`planificaciones/${id}`);
  }

  getPlanificacionesPorClase(claseId: number): Observable<any[]> {
    return this.get<any[]>(`clase/${claseId}/planificaciones`);
  }

  joinPlanificacion(alumnoId: number, planificacionId: number): Observable<any> {
    return this.put<any>(`planificacion/${planificacionId}?alumno_id=${alumnoId}`, {});
  }

  getPlanificacionesPorAlumno(alumnoId: number): Observable<any[]> {
    return this.get<any[]>(`planificaciones?alumno_id_plani=${alumnoId}`);
  }
}