import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BaseService } from 'src/app/services/base.service';
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
  claseId: any;

  constructor(private planificacionService: PlanificacionService,
    private route: ActivatedRoute,
    private baseService: BaseService) {}  // Inyecta el servicio de planificaciones

    ngOnInit() {
      this.route.params.subscribe(params => {
        this.claseId = params['id'];
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
}