import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';
import { UserDataService } from 'src/app/services/user-data.service';
import { Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-edit-profile-form',
  templateUrl: './edit-profile-form.component.html',
  styleUrls: ['./edit-profile-form.component.css'],
})
export class EditProfileFormComponent {
  public get userDataService(): UserDataService {
    return this._userDataService;
  }
  public set userDataService(value: UserDataService) {
    this._userDataService = value;
  }
  form: FormGroup;

  constructor(
    private router: Router,
    private usuariosService: UsuariosService,
    private jwtService: JWTService,
    private _userDataService: UserDataService
  ) {
    this.form = new FormGroup({
      name: new FormControl(''),
      lastname: new FormControl(''),
      email: new FormControl(''),
      phone: new FormControl(''),
      gender: new FormControl(''),
      address: new FormControl(''),
    });
  }
  userData: any = {
    nombre: '',
    apellido: '',
    email: '',
    telefono: 0,
    sexo: '',
    direccion: '',
    edad: 0,
    dni: 0,
    rol: '',
    id_usuario: 0
  };

  ngOnInit() {
    const userId = parseInt(this.jwtService.getId() || '', 10);
    if (userId) {
      this.usuariosService.getUserById<any>(userId).subscribe({
        next: (data) => {
          this.form.patchValue({
            name: data.nombre,
            lastname: data.apellido,
            email: data.email,
            phone: data.telefono,
            gender: data.sexo,
            address: data.direccion,
          });

          // Almacena los datos del formulario en el servicio UserDataService
          this.userDataService.setUserData(this.form.value);

          this.userData.id_usuario = data.id_usuario;
          this.userData.edad = data.edad;
          this.userData.dni = data.dni;
          this.userData.rol = data.rol;


        },
        error: (error) => {
          console.error(error);
        },
      });
    }
  }
  
  onSubmit() {

    this.userData.nombre = this.form.value.name;
    this.userData.apellido = this.form.value.lastname;
    this.userData.email = this.form.value.email;
    this.userData.telefono = this.form.value.phone;
    this.userData.direccion = this.form.value.address;
    this.userData.sexo = this.form.value.gender;

    this.usuariosService.putUser(this.userData.id_usuario, this.userData).subscribe({
      next: (data: any) => {
        this.router.navigate(['/profile']);
      },
      error: (error) => {
        console.error(error);
      },
    });
    }
  }

  // ngOnInit() {
  //   const userData = JSON.parse(localStorage.getItem('userData') || '{}');
  //   this.form.patchValue({
  //     name: userData.nombre,
  //     lastname: userData.apellido,
  //     email: userData.email,
  //     phone: userData.telefono,
  //     gender: userData.sexo,
  //     address: userData.direccion,
  //   });
  
  //   // Almacena los datos del formulario en el servicio UserDataService
  //   this.userDataService.setUserData(this.form.value);
  // }
