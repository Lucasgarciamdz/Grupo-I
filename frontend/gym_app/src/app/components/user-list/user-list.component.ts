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

  // editUser(user: any) {
  //   this.userSvc.editUser(user).subscribe({
  //     next: (updatedUser: any) => {
  //       // update the user in the users array
  //       const index = this.users.findIndex(u => u.id === updatedUser.id);
  //       this.users[index] = updatedUser;
  //     },
  //     error: (error) => {
  //       alert('Error al editar usuario');
  //     },
  //     complete: () => {
  //       console.log('Usuario editado');
  //     }
  //   });
  // }

  // deleteUser(user: any) {
  //   this.userSvc.deleteUser(user.id).subscribe({
  //     next: () => {
  //       // remove the user from the users array
  //       const index = this.users.findIndex(u => u.id === user.id);
  //       this.users.splice(index, 1);
  //     },
  //     error: (error) => {
  //       alert('Error al eliminar usuario');
  //     },
  //     complete: () => {
  //       console.log('Usuario eliminado');
  //     }
  //   });
  // }
}

@NgModule({  declarations: [UserListComponent],
  imports: [CommonModule],
  exports: [UserListComponent]})

export class UserListModule { }