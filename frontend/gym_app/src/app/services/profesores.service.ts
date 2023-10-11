import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {BaseService} from "./base.service";

@Injectable({
  providedIn: 'root'
})
export class ProfesoresService extends BaseService {
  constructor(httpClient: HttpClient) {
    super(httpClient);
  }

  getProfesores(): Observable<any[]> {
    const headers = this.getHeaders();

    return this.httpClient.get<any[]>(`${this.url}/profesores`, {headers});
  }

  putProfesor(id: number, prof: any): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.put<any>(`${this.url}/profesor/${id}`, prof, {headers});
  }

  deleteProfesor(id: number): Observable<any> {
    const headers = this.getHeaders();

    return this.httpClient.delete<any>(`${this.url}/profesor/${id}`, {headers});
  }
}
