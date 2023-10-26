import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-update-btn',
  templateUrl: './update-btn.component.html',
  styleUrls: ['./update-btn.component.css']
})
export class UpdateBtnComponent implements OnInit {
  previousUrl: string = '';
  form: FormGroup;

  constructor(private router: Router, private usuariosService: UsuariosService, private jwtService: JWTService) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.previousUrl = this.router.url;
      }
    });

    this.form = new FormGroup({
      name: new FormControl(''),
      lastname: new FormControl(''),
      email: new FormControl(''),
      phone: new FormControl(''),
      gender: new FormControl(''),
      address: new FormControl(''),
      age: new FormControl(''),
      idn: new FormControl(''),
      rol: new FormControl('')
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
            age: data.edad,
            idn: data.dni,
            rol: data.rol
          });
        },
        error: (error) => {
          console.error(error);
        }
      });
    }
  }

  onSubmit() {
  const userId = parseInt(this.jwtService.getId() || '', 10);
  if (userId) {
    const userData = {
      nombre: this.form.get('name')?.value,
      apellido: this.form.get('lastname')?.value,
      email: this.form.get('email')?.value,
      telefono: this.form.get('phone')?.value,
      sexo: this.form.get('gender')?.value,
      direccion: this.form.get('address')?.value,
      edad: this.form.get('age')?.value,
      dni: this.form.get('idn')?.value,
      rol: this.form.get('rol')?.value,
      id_login: userId
    };
    this.usuariosService.putUser(userId, userData).subscribe({
      next: (data: any) => {
        console.log(data);
        this.router.navigate(['/profile']);
      },
      error: (error) => {
        console.error(error);
      }
    });
  }
}
}