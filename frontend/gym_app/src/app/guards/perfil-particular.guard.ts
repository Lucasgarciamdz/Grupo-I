import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot } from '@angular/router';
import { JWTService } from '../services/jwt.service';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from '../services/base.service';

@Injectable({
  providedIn: 'root'
})
export class PerfilParticularGuard implements CanActivate {
  constructor(
    private router: Router,
    private jwtService: JWTService,
    private backendService: BaseService
  ) {
    console.log('perfilParticularGuard instantiated');
  }

  canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
    const alumnoId = route.params['id'];
    const profesorId = this.jwtService.getIdProfesor();
      return this.backendService.get("/profesor/" + profesorId, "myAlumno=" + alumnoId).pipe(
        map((response: any) => {
          if (response) {
            return true;
          } else {
            this.router.navigate(['/home']);
            return false;
          }
        }),
        catchError(() => {
          this.router.navigate(['/home']);
          return of(false);
        })
      );
  }
}