import { Component, OnInit } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { ActivatedRoute } from '@angular/router';
import { BaseService } from 'src/app/services/base.service';
import { ClasesService } from 'src/app/services/clases.service';


@Component({
  selector: 'app-clases',
  templateUrl: './clases.component.html',
  styleUrls: ['./clases.component.css']
})
export class ClasesComponent implements OnInit {

  constructor(private planificacionService: PlanificacionService,
    private claseService: ClasesService,
    private route: ActivatedRoute,
    private baseService: BaseService) {}

  claseId: any;
  claseTitle: string = '';
  claseDescription: string = '';
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

  ngOnInit() {
    // this.planificacionService.getPlanificaciones().subscribe({
    //   next: (data: any) => {
    //     this.planificaciones = data;
    //   },
    //   error: (err: any) => {
    //     console.error('Error al obtener planificaciones', err);
    //   }
    // });
    this.route.params.subscribe(params => {
      this.claseId = params['id'];
      
    });

    // http://127.0.0.1:5000/clase/18
    this.claseService.getClassById(this.claseId).subscribe({
      next: (response: any) => {
        console.log(response);
        this.claseTitle = response.tipo;
        this.claseDescription = response.descripcion;
      },
      error: (error) => {
        console.error(error);
      },
    });
  }
}
