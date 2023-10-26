import { Component } from '@angular/core';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-prof-buttons',
  templateUrl: './prof-buttons.component.html',
  styleUrls: ['./prof-buttons.component.css']
})
export class ProfButtonsComponent {
  // students: string[] = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6'];
  classes: string[] = ['Class A', 'Class B', 'Class C', 'Class D', 'Class E', 'Class F'];
  students: any[] = [];

  constructor(private backSvc: BaseService) { }

  ngOnInit() {
    this.backSvc.get("/alumnos").subscribe({
      next: (students: any) => {
        console.log('Respuesta alumnos: ', students);
        this.students = students.alumnos;
      },
      error: (error) => {
        alert('Error al obtener estudiantes');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }


}
