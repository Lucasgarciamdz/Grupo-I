import { Component, OnInit } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';

@Component({
  selector: 'app-clases',
  templateUrl: './clases.component.html',
  styleUrls: ['./clases.component.css']
})
export class ClasesComponent implements OnInit {
  items: { image: string, title: string, description: string, buttonText: string }[] = [
    {
      image: 'assets/clases/clase1.jpg',
      title: 'Clase 1',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    },
    {
      image: 'assets/clases/clase2.jpg',
      title: 'Clase 2',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    },
    {
      image: 'assets/clases/clase3.jpg',
      title: 'Clase 3',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    }
  ];
  get isToken() {
    return localStorage.getItem('token');
  }


  planificaciones: any[] = [];

  constructor(private planificacionService: PlanificacionService) {}

  ngOnInit() {
    this.planificacionService.getPlanificaciones().subscribe({
      next: (data: any) => {
        this.planificaciones = data;
      },
      error: (err: any) => {
        console.error('Error al obtener planificaciones', err);
      }
    });
  }
}
