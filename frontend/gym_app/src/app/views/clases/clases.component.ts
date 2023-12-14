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
    private route: ActivatedRoute,) {}

  claseId: any;
  claseTitle: string = '';
  claseDescription: string = '';
  claseImage: string = '';

  get isToken() {
    return localStorage.getItem('token');
  }
  
  planificaciones: any[] = [];

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.claseId = params['id'];
    });
    
    this.claseService.getClassById(this.claseId).subscribe({
      next: (response: any) => {
        // console.log(response);
        this.claseTitle = response.tipo;
        this.claseDescription = response.descripcion;
        this.claseImage = response.imagen;
      },
      error: (error) => {
        console.error(error);
      },
    });
  }
}
