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
      email: ["alumno@gmail.com.ar", Validators.required],
      contrasena: ['123', Validators.required]
    })
  }

  login(dataLogin:any = {}) {
    //dataLogin = {email: this.loginForm.value.email, password: this.loginForm.value.password}
    console.log('Comprobando credenciales');
    this.authService.login(dataLogin).subscribe({
      next: (rta:any) => {
        // alert('Login exitoso');
        console.log('Respuesta login: ',rta.access_token);
        console.log('Respuesta login: ',rta);
        localStorage.setItem('token', rta.access_token);
        localStorage.setItem('id_usuario', rta.id_usuario);
        localStorage.setItem('id_alumno', rta.id_alumno);
        localStorage.setItem('id_profesor', rta.id_profesor);
        localStorage.setItem('usuario', JSON.stringify(rta.usuario));
        this.router.navigateByUrl('home');
      },
      error: (error) => {
        alert('Credenciales incorrectas');
        localStorage.removeItem('token');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }

  togglePasswordVisibility(): void {
    const passwordInput = document.getElementById('password') as HTMLInputElement;
    passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password';
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
