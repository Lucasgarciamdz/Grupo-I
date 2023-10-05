import { CommonModule } from '@angular/common';
import { Component, NgModule, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  users: any[] | undefined;

  constructor(private userSvc: UsuariosService) { 
  }

  ngOnInit() {
    this.userSvc.getUsers().subscribe({
      next: (users: any) => {
        this.users = users.usuario;
      },
      error: (error) => {
        alert('Error al obtener usuarios');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }
}

@NgModule({  declarations: [UserListComponent],
  imports: [CommonModule],
  exports: [UserListComponent]})

export class UserListModule { }