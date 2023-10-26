import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-edit-profile-form',
  templateUrl: './edit-profile-form.component.html',
  styleUrls: ['./edit-profile-form.component.css']
})
export class EditProfileFormComponent {
  form: FormGroup;

  constructor(private usuariosService: UsuariosService, private jwtService: JWTService) {
    this.form = new FormGroup({
      name: new FormControl(''),
      lastname: new FormControl(''),
      email: new FormControl(''),
      phone: new FormControl(''),
      gender: new FormControl(''),
      address: new FormControl('')
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
            address: data.direccion
          });
        },
        error: (error) => {
          console.error(error);
        }
      });
    }
  }
}