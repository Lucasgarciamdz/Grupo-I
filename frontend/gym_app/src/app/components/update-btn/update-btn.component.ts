import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';
import { UserDataService } from 'src/app/services/user-data.service';

// // Importa la interfaz UserData
// import { UserData } from 'src/app/services/user-data.service';

@Component({
  selector: 'app-update-btn',
  templateUrl: './update-btn.component.html',
  styleUrls: ['./update-btn.component.css'],
})

export class UpdateBtnComponent implements OnInit {
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

  previousUrl: string = '';

  constructor(
    private router: Router,
    private usuariosService: UsuariosService,
    private jwtService: JWTService,
    private userDataService: UserDataService
  ) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.previousUrl = this.router.url;
      }
    });
  }

  ngOnInit() {
    // Obtén los datos del servicio UserDataService
    this.userData = this.userDataService.getUserData();
    console.log(this.userData);
  }

  onSubmit() {
    const userId = parseInt(this.jwtService.getId() || '', 10);
    if (userId) {
      this.usuariosService.putUser(userId, this.userData).subscribe({
        next: (data: any) => {
          this.router.navigate(['/profile']);
        },
        error: (error) => {
          console.error(error);
        },
      });
    }
  }
}
