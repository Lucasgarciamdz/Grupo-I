import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ClasesService } from 'src/app/services/clases.service';
import { JWTService } from 'src/app/services/jwt.service';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-class-card',
  templateUrl: './class-card.component.html',
  styleUrls: ['./class-card.component.css']
})
export class ClassCardComponent implements OnInit {
  @Input() title!: string;
  @Input() items!: { image: string, title: string, description: string, buttonText: string }[];
  planificacionesClase: any[] = [];
  planificacionesAlumno: any[] = [];
  profesoresClase: any[] = [];
  claseId: any;
  alumnoId: any;
  profesorId: any;
  rol: any;
  profesorInClass: boolean = false;

  constructor(private planificacionService: PlanificacionService,
    private claseService: ClasesService,
    private route: ActivatedRoute,
    private snackBar: MatSnackBar,
    private router: Router,
    private jwtService: JWTService) {} 

    ngOnInit() {
      this.route.params.subscribe(params => {
        this.claseId = params['id'];
      });

      let usuario = JSON.parse(localStorage.getItem('usuario') || '{}');
      this.rol = usuario.rol;
      console.log("Rol:", this.rol);

      this.alumnoId = this.jwtService.getIdAlumno();
      this.profesorId = this.jwtService.getIdProfesor();

      console.log("clase id:", this.claseId);
      console.log("alumno id:", this.alumnoId);
      console.log("profesor id:", this.profesorId);

      this.claseService.getPlanificacionesPorClase(this.claseId).subscribe({
        next: (response: any) => {
          this.title = response.clase.titulo;
          this.planificacionesClase = response.planificaciones;
          console.log("planificaciones clase", this.planificacionesClase);
        },
        error: (err: any) => {
          console.error('Error al obtener planificaciones por clase', err);
        }
      });

      this.planificacionService.getPlanificacionesPorAlumno(this.alumnoId).subscribe({
        next: (data: any) => {
          this.planificacionesAlumno = data;
          console.log("planificaciones alumno", this.planificacionesAlumno);
        },
        error: (err: any) => {
          console.error('Error al obtener planificaciones por alumno', err);
        }
      });

      this.claseService.getProfesoresPorClase(this.claseId).subscribe({
        next: (response: any) => {
          this.profesoresClase = response.profesores;
          console.log("Profesores clase", this.profesoresClase);
          this.profesorInClass = this.isProfesorClase(this.profesorId);
        },
        error: (err: any) => {
          console.error('Error al obtener profesores por clase', err);
        }
      });
  }

  isPlanificacionComun(planificacionId: number) {
    if (this.planificacionesAlumno.some(planificacion => planificacion.id_planificacion === planificacionId)) {
      return true;
    } else {
      return false;
    }
  }

  isProfesorClase(profesorId: number) {
      if (this.profesoresClase.some(profesor => Number(profesor.id_profesor) === Number(profesorId))){
        return true;
      } else {
        return false;
      }
  }

  joinPlanificacion(planificacionId: number) {
  this.planificacionService.joinPlanificacion(this.alumnoId, planificacionId).subscribe(response => {
    console.log(response);
    window.location.reload();
    this.router.navigate(['/views/class', this.claseId]).then(() => {
      this.snackBar.open('Te has unido a la planificación correctamente', 'Cerrar', {
        duration: 3000,
        });
      });
    });
  }

removePlanificacion(planificacionId: number) {
  this.planificacionService.removePlanificacion(this.alumnoId, planificacionId).subscribe(response => {
    console.log(response);
    window.location.reload();
    this.router.navigate(['/views/class', this.claseId]).then(() => {
      this.snackBar.open('Has abandonado la planificación correctamente', 'Cerrar', {
        duration: 3000,
        });
      });
    });
  }

  joinProfesorClase(profesorId: number) {
    this.claseService.joinProfesorClase(profesorId, this.claseId).subscribe(response => {
      console.log(response);
      this.router.navigate(['/views/class', this.claseId]).then(() => {
        window.location.reload();
        this.snackBar.open('Te has unido a la clase correctamente', 'Cerrar', {
          duration: 3000,
          });
        });
      });
    }

  removeProfesorClase(profesorId: number) {
    this.claseService.removeProfesorClase(profesorId, this.claseId).subscribe(response => {
      console.log(response);
      this.router.navigate(['/views/class', this.claseId]).then(() => {
        window.location.reload();
        this.snackBar.open('Has abandonado la clase correctamente', 'Cerrar', {
          duration: 3000,
          });
        });
      });
    }
}