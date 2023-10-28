import { Component } from '@angular/core';
import { AlumnoService } from 'src/app/services/alumno.service';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  alumnos: any[] = [];
  usuario: any;

  height: string = '';
  weight: string = '';
  age: string = '';

  constructor(private alumnoService: AlumnoService, private usuarioService: UsuariosService, private jwtService: JWTService) { }

  ngOnInit(): void {
    const userData = JSON.parse(localStorage.getItem('usuario') || '{}');
    this.usuario = userData;
    this.age = this.usuario.edad;
    this.alumnoService.getAlumnos().subscribe({
      next: (response: any) => {
        this.alumnos = response.alumnos;
        for (let alumno of this.alumnos) {
          // console.log(alumno);
          if (alumno.id_usuario == this.usuario.id_usuario) {
            this.height = alumno.altura;
            this.weight = alumno.peso;
            // console.log(`Height: ${this.height}, Weight: ${this.weight}`);
          }
        }
      },
      error: (error) => {
        console.error(error);
      }
    });
  }
}