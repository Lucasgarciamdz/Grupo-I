import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-lista-planificaciones',
  templateUrl: './lista-planificaciones.component.html',
  styleUrls: ['./lista-planificaciones.component.css']
})
export class ListaPlanificacionesComponent {

  @Input()
  id!: string;
  @Input() 


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
