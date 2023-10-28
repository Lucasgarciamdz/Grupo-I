import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';
import { UserDataService } from 'src/app/services/user-data.service';

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
        },
        error: (error) => {
          console.error(error);
        },
      });
    }
  }
}
