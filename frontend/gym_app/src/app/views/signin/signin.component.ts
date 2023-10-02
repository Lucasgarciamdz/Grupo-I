import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent {
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

  login(dataLogin:any = {}) {
    console.log('Comprobando credenciales');
    this.authService.login(dataLogin).subscribe({
      next: (rta:any) => {
        // alert('Login exitoso');
        console.log('Token: ',rta.access_token);
        localStorage.setItem('token', rta.access_token);
        this.router.navigateByUrl('home');
      }, error:(error) => {
        alert('Credenciales incorectas');
        localStorage.removeItem('token');
      }, complete: () => {
        console.log('Finalizo')
      }
    })
  }

  submit() {
    if(this.loginForm.valid) {
      console.log('Form login: ',this.loginForm.value);
      this.login(this.loginForm.value)
    } else {
      alert('Formulario invalido');
    }
  }
}