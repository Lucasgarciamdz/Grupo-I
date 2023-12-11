import { Component } from '@angular/core';
import { ClasesService } from 'src/app/services/clases.service';
import { PlanificacionService } from 'src/app/services/planificacion.service';

@Component({
  selector: 'app-stud-work',
  templateUrl: './stud-work.component.html',
  styleUrls: ['./stud-work.component.css']
})
export class StudWorkComponent {

  classItems: any[] = [];
  planItems: any[] = [];

  constructor(private clasesService: ClasesService, 
    private planificacionService: PlanificacionService) {}

  ngOnInit(): void {
    const alumnoId = localStorage.getItem('id_alumno') ?? '';
    const alumnoIdNumber = parseInt(alumnoId, 10);
    console.log('alumnoId:', alumnoIdNumber);

    this.planificacionService.getPlanificacionesPorAlumno(alumnoIdNumber).subscribe({
      next: (planificaciones) => {
        console.log('planificaciones:', planificaciones);
        const uniqueClaseIds = [...new Set(planificaciones.map(item => item.id_clase))];
        for (const id of uniqueClaseIds) {
          this.getClaseName(id, planificaciones.filter(p => p.id_clase === id));
        }
      },
      error: (error) => {
        console.error('Error al obtener las planificaciones:', error);
      }
    });
  }

  getClaseName(id: number, planificaciones: any[]) {
    this.clasesService.getClassById(id).subscribe({
      next: (clase) => {
        console.log('clase:', clase);
        this.classItems.push({
          title: clase.tipo,
          planificaciones: planificaciones.map(p => ({
            image: 'https://i.blogs.es/410bab/danielle-cerullo-cqfnt66ttzm-unsplash/1366_2000.jpeg',
            title: `Planificación ${p.id_planificacion}`,
            // description: `Objetivo: ${p.objetivo}, Nivel: ${p.nivel}, Horas Semanales: ${p.horas_semanales}`,
            buttonText: 'Ver Planificación',
            id_planificacion: p.id_planificacion,
            link: `/planificaciones/${p.id_planificacion}`
          }))
        });
      },
      error: (error) => {
        console.error('Error al obtener la clase:', error);
      }
    });
  }
}