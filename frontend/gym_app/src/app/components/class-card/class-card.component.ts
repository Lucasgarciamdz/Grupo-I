import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BaseService } from 'src/app/services/base.service';
import { JWTService } from 'src/app/services/jwt.service';
import { PlanificacionService } from 'src/app/services/planificacion.service';  // Importa el servicio de planificaciones

@Component({
  selector: 'app-class-card',
  templateUrl: './class-card.component.html',
  styleUrls: ['./class-card.component.css']
})
export class ClassCardComponent implements OnInit {
  @Input() title!: string;
  @Input() items!: { image: string, title: string, description: string, buttonText: string }[];
  planificaciones: any[] = [];
  planificacionesAlumno: any[] = [];
  claseId: any;
  alumnoId: any;

  constructor(private planificacionService: PlanificacionService,
    private route: ActivatedRoute,
    private baseService: BaseService,
    private jwtService: JWTService) {} 

    ngOnInit() {
      this.route.params.subscribe(params => {
        this.claseId = params['id'];
      });

    this.alumnoId = this.jwtService.getIdAlumno()

    this.planificacionService.getPlanificacionesPorAlumno(this.alumnoId).subscribe({
      next: (data: any) => {
        // Asigna los datos de las planificaciones a la propiedad 'planificaciones'
        this.planificacionesAlumno = data.planificacion;
        console.log(this.planificacionesAlumno);
      },
      error: (err: any) => {
        console.error('Error al obtener planificaciones', err);
      }
    });
    
    if (this.claseId > 0) {
      this.baseService.get('/clase/' + this.claseId, "planificaciones=1").subscribe({
        next: (response: any) => {
          this.title = response.clase.titulo;
          this.planificaciones = response.planificaciones;
        },
        error: (error) => {
          console.error(error);
        },
      });
    } else {
    // Realiza la solicitud al servicio para obtener las planificaciones
    this.planificacionService.getPlanificaciones().subscribe({
      next: (data: any) => {
        // Asigna los datos de las planificaciones a la propiedad 'planificaciones'
        this.planificaciones = data.planificacion;
        console.log(this.planificaciones);
      },
      error: (err: any) => {
        console.error('Error al obtener planificaciones', err);
      }
    });
  }
}
  joinPlanificacion(planificacionId: number) {
    this.planificacionService.joinPlanificacion(this.alumnoId, planificacionId).subscribe(response => {
      console.log(response);
    });
  }
}