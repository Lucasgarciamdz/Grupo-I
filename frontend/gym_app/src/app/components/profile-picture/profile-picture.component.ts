import { Component, Input, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { JWTService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-profile-picture',
  template: `
    <img [src]="image" class="img img-thumbnail rounded-circle mx-auto d-block" alt="Profile Picture">
    <h2 class="text-center">{{ name || "alumno x"}}</h2>
  `,
  styles: [
    `
    img {
      max-width: 25%;
      max-height: 25%;
    }
    `
  ]
})
export class ProfilePictureComponent implements OnInit {
  @Input() image: string | undefined;
  @Input() name: string | undefined;

  // constructor(private usuariosService: UsuariosService, private jwtService: JWTService) {}

  // ngOnInit() {
  //   const userId = parseInt(this.jwtService.getId() || '', 10);
  //   if (userId) {
  //     this.usuariosService.getUserById<any>(userId).subscribe({
  //       next: (data) => {
  //         // this.image = data.imagen;
  //         this.name = `${data.nombre} ${data.apellido}`;
  //       },
  //       error: (error) => {
  //         console.error(error);
  //       }
  //     });
  //   }
  // }

  ngOnInit() {
    const userData = JSON.parse(localStorage.getItem('usuario') || '{}');
    // console.log(userData);
    this.name = `${userData.nombre} ${userData.apellido}`;
    // this.image = userData.imagen;
  }
}