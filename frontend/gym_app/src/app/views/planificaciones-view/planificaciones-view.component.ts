import { Component, OnInit } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-planificaciones-view',
  templateUrl: './planificaciones-view.component.html',
  styleUrls: ['./planificaciones-view.component.css']
})
export class PlanificacionesViewComponent implements OnInit {

  constructor(private planificacionService: PlanificacionService,
    private route: ActivatedRoute,
    private snackBar: MatSnackBar,
    private router: Router,
    private jwtService: JWTService) {} 
    
  planificacionId: any;
  planificacionHoras: any;
  planificacionNivel: any;
  planificacionObjetivo: any;
  alumnoId: any = localStorage.getItem('id_alumno') || null;
  planificacionActive: boolean = false;
  planificacionesAlumno: any[] = [];

  ngOnInit() {

    this.route.params.subscribe(params => {
      this.planificacionId = params['id'];
    });

    if (this.alumnoId == null) {
      this.alumnoId = this.jwtService.getIdAlumno();
    }

    console.log("planificacion id:", this.planificacionId);
    console.log("alumno id:", this.alumnoId);

    this.planificacionService.getPlanificacionesPorAlumno(this.alumnoId).subscribe({
      next: (data: any) => {
        this.planificacionesAlumno = data;
        // console.log("planificaciones alumno", this.planificacionesAlumno);
        this.planificacionesAlumno.forEach((planificacion) => {
          if (planificacion.id_planificacion == this.planificacionId) {
            this.planificacionActive = true;
          }
        });
      },
      error: (err: any) => {
        console.error('Error al obtener planificaciones por alumno', err);
      }
    });

    this.planificacionService.getPlanificacionById(this.planificacionId).subscribe({
      next: (response: any) => {
        this.planificacionHoras = response.horas_semanales;
        this.planificacionNivel = response.nivel;
        this.planificacionObjetivo = response.objetivo;
        console.log(response);
      },
      error: (error) => {
        console.error(error);
      },
    });
  }

  joinPlanificacion(planificacionId: number) {
    this.planificacionService.joinPlanificacion(this.alumnoId, planificacionId).subscribe(response => {
      console.log(response);
      this.router.navigate(['/views/planificacion', this.planificacionId]).then(() => {
        this.snackBar.open('Te has unido a la planificación correctamente', 'Cerrar', {
          duration: 3000,
          });
        });
      });
    }
  
  removePlanificacion(planificacionId: number) {
    this.planificacionService.removePlanificacion(this.alumnoId, planificacionId).subscribe(response => {
      console.log(response);
      this.router.navigate(['/views/planificacion', this.planificacionId]).then(() => {
        this.snackBar.open('Has abandonado la planificación correctamente', 'Cerrar', {
          duration: 3000,
          });
        });
      });
    }
}
