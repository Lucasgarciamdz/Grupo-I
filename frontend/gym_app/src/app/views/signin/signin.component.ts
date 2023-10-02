import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  loginForm!: FormGroup;

  constructor(
    private authService: AuthService,
    private router: Router,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      email: ["francobertoldi@gmail.com", Validators.required],
      password: ['12345', Validators.required]
    });
  }

  login(dataLogin: any = {}) {
    console.log('Comprobando credenciales');
    this.authService.login(dataLogin).subscribe({
      next: (rta: any) => {
        alert('Login exitoso');
        console.log('Respuesta login: ', rta.access_token);

        // Almacenar el token y el rol en el almacenamiento local
        localStorage.setItem('token', rta.access_token);
        localStorage.setItem('role', rta.role); // Suponiendo que el backend envía el rol en la respuesta

        this.router.navigateByUrl('home');
      },
      error: (error) => {
        alert('Credenciales incorrectas');
        localStorage.removeItem('token');
        localStorage.removeItem('role'); // Eliminar el rol en caso de error
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }

  submit() {
    if (this.loginForm.valid) {
      console.log('Form login: ', this.loginForm.value);
      this.login(this.loginForm.value);
    } else {
      alert('Formulario inválido');
    }
  }
}
