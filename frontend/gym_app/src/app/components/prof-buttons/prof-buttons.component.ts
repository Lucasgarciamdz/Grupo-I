import { Component } from '@angular/core';
import { BaseService } from 'src/app/services/base.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-prof-buttons',
  templateUrl: './prof-buttons.component.html',
  styleUrls: ['./prof-buttons.component.css']
})
export class ProfButtonsComponent {
  // students: string[] = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6'];
  classes: any[] = [];
  students: any[] = [];

  constructor(
    private backSvc: BaseService,
    private jwtService: JWTService ) { }

  ngOnInit() {
    const profesorId = localStorage.getItem('id_profesor');
    this.backSvc.get("/profesor/" + profesorId, "alumnosyclases=1").subscribe({
      next: (profesorData: any) => {
        this.students = profesorData.alumnos.map((alumno: any) => ({
          id: alumno.id_alumno,
          name: `${alumno.usuario.nombre} ${alumno.usuario.apellido}`
        }));
        console.log(profesorData);
        this.classes = profesorData.clases.map((clase: any) => ({
          id: clase.id,
          name: clase.tipo
        }));
      },
      error: (err: any) => {
        alert('Error al obtener estudiantes');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }


}
