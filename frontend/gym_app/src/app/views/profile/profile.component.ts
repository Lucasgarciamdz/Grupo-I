import { Component } from '@angular/core';
import { AlumnoService } from 'src/app/services/alumno.service';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';
import { ActivatedRoute } from '@angular/router';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})
export class ProfileComponent {
  alumnos: any[] = [];
  usuario: any;
  currentUser: any;

  profileName: string = '';
  height: string = '';
  weight: string = '';
  age: string = '';
  profileId: any;
  alumno_id: any;


  constructor(
    private alumnoService: AlumnoService,
    private usuarioService: UsuariosService,
    private jwtService: JWTService,
    private route: ActivatedRoute,
    private baseService: BaseService
  ) {}

  ngOnInit(): void {
    this.currentUser = this.jwtService.getId();
    this.route.params.subscribe(params => {
      this.profileId = params['id'];
    });

  
    console.log(this.profileId);
    console.log(this.currentUser);
    if (this.profileId) {
      console.log('viendo usuario particular');
      this.alumnoService.getAlumnoFull(this.profileId).subscribe({
        next: (response: any) => {
          console.log(response);
          // this.usuario = response.usuario;
          this.profileName = response.usuario.nombre + ' ' + response.usuario.apellido;
          this.age = response.usuario.edad;
          this.height = response.altura;
          this.weight = response.peso;
        },
        error: (error) => {
          console.error(error);
        },
      });
    } else {
      this.alumno_id = this.jwtService.getIdAlumno();
      console.log('viendo mi perfil');
      const userData = JSON.parse(localStorage.getItem('usuario') ?? '{}');
      console.log(userData);
      this.usuario = userData;
      this.age = this.usuario.edad;
      this.profileName = this.usuario.nombre + ' ' + this.usuario.apellido;
      this.alumnoService.getAlumno(this.alumno_id).subscribe({
        next: (response: any) => {
          console.log(response);
          this.profileName = response.usuario.nombre + ' ' + response.usuario.apellido;
          this.height = response.altura;
          this.weight = response.peso;
          this.age = response.usuario.edad;

        },
        error: (error) => {
          console.error(error);
        },
      });
    }
  }
}
