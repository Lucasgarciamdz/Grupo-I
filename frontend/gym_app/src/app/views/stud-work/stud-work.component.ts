import { Component } from '@angular/core';
import { ClasesService } from 'src/app/services/clases.service';
import { PlanificacionService } from 'src/app/services/planificacion.service';

@Component({
  selector: 'app-stud-work',
  templateUrl: './stud-work.component.html',
  styleUrls: ['./stud-work.component.css']
})
export class StudWorkComponent {

  // workoutItems = [
  //   {
  //     image: 'assets/clases/clase1.jpg',
  //     title: 'Clase 1',
  //     description: 'Fuerza',
  //     buttonText: 'Ver Clase'
  //   },
  //   {
  //     image: 'assets/clases/clase2.jpg',
  //     title: 'Clase 2',
  //     description: 'Fuerza',
  //     buttonText: 'Ver Clase'
  //   },
  //   {
  //     image: 'assets/clases/clase3.jpg',
  //     title: 'Clase 3',
  //     description: 'Fuerza',
  //     buttonText: 'Ver Clase'
  //   },
  // ];

  classItems: any[] = [];
  planItems: any[] = [];

  constructor(private clasesService: ClasesService, private planificacionService: PlanificacionService) {}

  ngOnInit(): void {
    const alumnoId = localStorage.getItem('id_alumno') ?? '';
    const alumnoIdNumber = parseInt(alumnoId, 10);
  
    this.clasesService.getClasesByAlumnoId(alumnoIdNumber).subscribe({
      next: (clases) => {
        console.log('esto trae el recurso', clases);
        for (const clase of clases) {
          this.classItems.push({
            // image: clase.imagen,
            title: clase.tipo,
            description: clase.descripcion,
            buttonText: 'Ver clase',
            id_clase: clase.id
          });
        }
        console.log('esta es la lista', this.classItems);
      },
      error: (error) => {
        // Manejo de errores si es necesario
        console.error('Error al obtener las clases:', error);
      }
    });
  
  //   this.planificacionService.getPlanificacionesByAlumnoId(alumnoIdNumber).subscribe({
  //     next: (planificaciones) => {
  //       for (const planificacion of planificaciones) {
  //         this.planItems.push({
  //           image: planificacion.imagen,
  //           title: planificacion.id_planificacion,
  //           description: planificacion.descripcion,
  //           buttonText: 'Ver Planificación'
  //         });
  //       }
  //       console.log(this.planItems);
  //     },
  //     error: (error) => {
  //       // Manejo de errores si es necesario
  //       console.error('Error al obtener las planificaciones:', error);
  //     }
  //   });
   }
}