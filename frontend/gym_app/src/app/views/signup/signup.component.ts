import { Component } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {

  hidePassword = true;
  hideConfirmPassword = true;
  confirmarContrasena = '';
  user = {
    nombre: '',
    apellido: '',
    direccion: '',
    edad: null,
    telefono: null,
    dni: null,
    rol: '',
    sexo: '',
    mail: '',
    contrasena: ''
  };

  constructor(private usuariosService: UsuariosService) { }

    onSubmit() {
      if (this.user.contrasena === this.confirmarContrasena) {
        this.usuariosService.createUser(this.user).subscribe(response => {
            console.log(response);
        });
    } else
      alert('Las contraseñas no coinciden');
  }

  togglePasswordVisibility() {
    this.hidePassword = !this.hidePassword;
  }
  
  toggleConfirmPasswordVisibility() {
    this.hideConfirmPassword = !this.hideConfirmPassword;
  }
}