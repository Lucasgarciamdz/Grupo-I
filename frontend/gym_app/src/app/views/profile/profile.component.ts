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

  constructor(
    private alumnoService: AlumnoService,
    private usuarioService: UsuariosService,
    private jwtService: JWTService,
    private route: ActivatedRoute,
    private baseService: BaseService
  ) {}

  ngOnInit(): void {
    this.currentUser = this.jwtService.getId();
    this.route.queryParams.subscribe(params => {
      this.profileId = params['id'];
    });

    console.log(this.profileId);
    console.log(this.currentUser);
    if (this.profileId) {
      console.log('viendo usuario particular');
      this.baseService.get('/alumno/' + this.profileId, 'full=1').subscribe({
        next: (response: any) => {
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
      console.log('viendo mi perfil');
      const userData = JSON.parse(localStorage.getItem('usuario') ?? '{}');
      this.usuario = userData;
      this.age = this.usuario.edad;
      this.profileName = this.usuario.nombre + ' ' + this.usuario.apellido;
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
        },
      });
    }
  }
}
