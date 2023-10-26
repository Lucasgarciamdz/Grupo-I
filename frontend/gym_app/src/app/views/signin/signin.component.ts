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
      email: ["f.bertoldi@alumno.um.edu.ar", Validators.required],
      contrasena: ['123', Validators.required]
    })
  }

  //f.bertoldi@alumno.um.edu.ar
  //123
  //l.garcia@alumno.um.edu.ar
  //456
  ///frg.lopez@alumno.um.edu.ar
  ///789
  login(dataLogin:any = {}) {
    //dataLogin = {email: this.loginForm.value.email, password: this.loginForm.value.password}
    console.log('Comprobando credenciales');
    this.authService.login(dataLogin).subscribe({
      next: (rta:any) => {
        alert('Login exitoso');
        console.log('Respuesta login: ',rta.access_token);
        localStorage.setItem('token', rta.access_token);
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

  submit() {
    if (this.loginForm.valid) {
      console.log('Form login: ', this.loginForm.value);
      this.login(this.loginForm.value);
    } else {
      alert('Formulario inválido');
    }
  }
}
