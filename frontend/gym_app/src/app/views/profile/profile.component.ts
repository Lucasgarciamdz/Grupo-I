import { Component } from '@angular/core';
import { AlumnoService } from 'src/app/services/alumno.service';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  alumnos: any[] = [];

  height: string = '';
  weight: string = '';
  age: string = '';

  constructor(private alumnoService: AlumnoService, private usuarioService: UsuariosService) { }

  ngOnInit(): void {
    const userData = JSON.parse(localStorage.getItem('userData') || '{}');
    userData.age = this.age;
    console.log(userData);
  
    this.alumnoService.getAlumnos().subscribe({
      next: (response: any) => {
        this.alumnos = response.alumnos;
        for (let alumno of this.alumnos) {
          if (alumno.id_usuario == userData.id_usuario) {
            this.height = alumno.height;
            this.weight = alumno.weight;
            console.log(`Height: ${this.height}, Weight: ${this.weight}`);
          }
        }
      },
      error: (error) => {
        console.error(error);
      }
    });
  }
}