import { Component } from '@angular/core';
import { AlumnoService } from 'src/app/services/alumno.service';
import { JWTService } from 'src/app/services/jwt.service';
import { ActivatedRoute } from '@angular/router';
import { ProfesoresService } from 'src/app/services/profesores.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})
export class ProfileComponent {
  profileName: string = '';
  height: string = '';
  weight: string = '';
  age: string = '';
  profileId: any;
  role: string = '';
  certificacion: string = '';
  fecha_inicio_actividad: string = '';
  currentUser: any;

  constructor(
    private alumnoService: AlumnoService,
    private jwtService: JWTService,
    private route: ActivatedRoute,
    private profesorService: ProfesoresService
  ) {}

  ngOnInit(): void {
    const currentUser = this.jwtService.getId() ?? 1;
    this.role = this.jwtService.getRol() ?? '';

    this.route.params.subscribe(params => {
      this.profileId = params['id'];

      switch (this.role) {
        case 'Alumno':
          const alumno_id = this.profileId || this.jwtService.getIdAlumno();
          const {nombre, apellido, edad} = JSON.parse(localStorage.getItem('usuario') ?? '{}');
          this.profileName = `${nombre} ${apellido}`;
          this.age = edad;
          this.alumnoService.getAlumno(alumno_id).subscribe({
            next: ({usuario: {nombre, apellido, edad}, altura, peso}) => {
              this.profileName = `${nombre} ${apellido}`;
              this.height = altura;
              this.weight = peso;
              this.age = edad;
            },
            error: console.error,
          });
          break;
        case 'Profesor':
          const profesor_id = this.profileId || currentUser;
          this.profesorService.getProfesor(profesor_id).subscribe({
            next: ({usuario: {nombre, apellido}, certificacion, fecha_inicio_actividad}) => {
              this.profileName = `${nombre} ${apellido}`;
              this.certificacion = certificacion;
              this.fecha_inicio_actividad = fecha_inicio_actividad;
            },
            error: console.error,
          });
          break;
      }
    });
  }
}