import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { JWTService } from '../services/jwt.service';
import { BaseService } from '../services/base.service';


@Injectable({
  providedIn: 'root'
})
export class AlumnoClaseGuard implements CanActivate {
  constructor(
    private jwtService: JWTService,
    private router: Router,
    private backendService: BaseService,
  ) {}

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> | Promise<boolean> | boolean {
    const alumnoId = next.paramMap.get('id');
    const profesorId = this.jwtService.getIdProfesor();
    console.log("HOLA SOY EL GUARD DEL PERFIL")
    console.log("ESTE ES EL ID DEL ALUMNO:", alumnoId);

    if (alumnoId && profesorId) {
      return this.backendService.get("/profesor/" + profesorId, "myAlumno=" + alumnoId).pipe(
        map((response: any) => {
          if (response) {
            return true;
          } else {
            this.router.navigate(['/home']);
            return false;
          }
        })
      );
    } else {
      this.router.navigate(['/home']);
      return false;
    }
  }
}