import { Component, Input, OnInit } from '@angular/core';
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

  constructor(private planificacionService: PlanificacionService) {}  // Inyecta el servicio de planificaciones

  ngOnInit() {
    // Realiza la solicitud al servicio para obtener las planificaciones
    this.planificacionService.getPlanificaciones().subscribe({
      next: (data: any) => {
        // Asigna los datos de las planificaciones a la propiedad 'planificaciones'
        this.planificaciones = data;
      },
      error: (err: any) => {
        console.error('Error al obtener planificaciones', err);
      }
    });
  }
}