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
    const headers = this.getHeaders();

    return this.httpClient.get<any[]>(`${this.url}/clases`, { headers });
  }

  putClase(id: number, clase: any): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.put<any>(`${this.url}/clase/${id}`, clase, { headers });
  }

  deleteClase(id: number): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.delete<any>(`${this.url}/clase/${id}`, { headers });
  }
}
