import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { BaseService } from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class ProfesoresService extends BaseService {
  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getProfesores(): Observable<any[]> {
    return this.get<any[]>('profesores');
  }

  updateProfesor(id: number, prof: any): Observable<any> {
    return this.put<any>(`profesor/${id}`, prof);
  }

  deleteProfesor(id: number): Observable<any> {
    return this.delete<any>(`profesor/${id}`);
  }

  putProfesor(id: number, prof: any): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.put<any>(`${this.url}/profesor/${id}`, prof, {headers});
  }
}
