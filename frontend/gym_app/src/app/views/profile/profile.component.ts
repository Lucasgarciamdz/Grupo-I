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
  currentUser: string = '';

  constructor(
    private alumnoService: AlumnoService,
    private jwtService: JWTService,
    private route: ActivatedRoute,
    private profesorService: ProfesoresService
  ) { }

  ngOnInit(): void {
    this.currentUser = this.jwtService.getId() ?? '';
    this.role = this.jwtService.getRol() ?? '';

    this.route.params.subscribe(params => {
      this.profileId = params['id'];
      console.log(this.profileId)
      switch (this.role) {
        case 'Alumno':
          if (this.profileId){
            this.role = 'Profesor';
            this.getProfesorProfile(this.profileId);
          }
          else {
            this.getAlumnoProfile();
          }
          break;
        case 'Profesor':
          if (this.profileId){
            this.role = 'Alumno';
            this.getAlumnoProfile(this.profileId);
          }
          else {
            this.getProfesorProfile();
          }
          break;
      }
    });
  }

  getAlumnoProfile(id?: string): void {
    const alumno_id = id || this.jwtService.getIdAlumno();
    if (alumno_id) {
      console.log(alumno_id)
      const { nombre, apellido, edad } = JSON.parse(localStorage.getItem('usuario') ?? '{}');
      this.profileName = `${nombre} ${apellido}`;
      this.age = edad;
      this.alumnoService.getAlumno(parseInt(alumno_id)).subscribe({
        next: (response) => {
          this.profileName = response.usuario.nombre + ' ' + response.usuario.apellido;
          this.height = response.altura;
          this.weight = response.peso;
          this.age = edad;
        },
        error: console.error,
      });
    } else {
      // Handle the case when alumno_id is null
      console.error('alumno_id is null');
    }
  }

  getProfesorProfile(id?: string): void {
    const profesor_id = id || this.jwtService.getIdProfesor();
    if (profesor_id) {
      this.profesorService.getProfesorFull(parseInt(profesor_id)).subscribe({
        next: (response) => {
          this.profileName = response.nombre + ' ' + response.apellido;
          this.certificacion = response.certificacion;
          this.fecha_inicio_actividad = response.fecha_inicio_actividad;
          this.age = response.edad;
        },
        error: console.error,
      });
    } else {
      // Handle the case when profesor_id is null
      console.error('profesor_id is null');
    }
  }
}