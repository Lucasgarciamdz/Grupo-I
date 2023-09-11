import { Component } from '@angular/core';

@Component({
  selector: 'app-planificaciones',
  templateUrl: './planificaciones.component.html',
  styleUrls: ['./planificaciones.component.css']
})
export class PlanificacionesComponent {

  arrayPlanificaciones: any[] = [
    {
      id: 1,
      Nombre: 'Plan 1',
      Clase: 'Spinning',
      Objetivo: 'Bajar de peso',
    },
    {
      id: 2,
      Nombre: 'Plan 2',
      Clase: 'Spinning',
      Objetivo: 'Bajar de peso',
    },
    {
      id: 3,
      Nombre: 'Plan 3',
      Clase: 'Spinning',
      Objetivo: 'Bajar de peso',
    },];
}
