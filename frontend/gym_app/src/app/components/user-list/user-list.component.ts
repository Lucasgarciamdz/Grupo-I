import { CommonModule } from '@angular/common';
import { Component, NgModule, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  editingUser: number = 0;

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


  editUser(id: number): void { 
    this.editingUser = id;
  }

  deleteUser(id: number): void {
    alert('Eliminar usuario con id ' + id);
  }

  saveUser(): void {
    alert('Guardar usuario');
  }

  cancelEdit(): void {
    alert('Cancelar edición');
  }
}


@NgModule({  declarations: [UserListComponent],
  imports: [CommonModule],
  exports: [UserListComponent]})

export class UserListModule { }