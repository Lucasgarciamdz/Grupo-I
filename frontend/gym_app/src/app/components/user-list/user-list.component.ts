import { CommonModule, Location } from '@angular/common';
import { Component, NgModule, OnInit, ViewChild } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { FormsModule, NgForm } from "@angular/forms";
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  @ViewChild('userForm')
  userForm!: NgForm;

  editingUserId: number = -1;

  users: any[] | undefined;

  showFilterForm: number = 0;

  minAge: number | undefined;
  maxAge: number | undefined;
  rol: string | undefined;

  constructor(private userSvc: UsuariosService, private router: Router, private location: Location) {
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

  reloadPage() {
    window.location.reload();
  }  

  editUser(id: number): void {
    this.editingUserId = id;
    alert('Editar usuario con id ' + id)
  }

  deleteUser(id: number): void {
    this.userSvc.deleteUser(id).subscribe({
      next: (user: any) => {
        alert('Usuario eliminado');
        this.reloadPage();
      },
      error: (error) => {
        alert('Error al eliminar usuario');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }

  saveUser(form: NgForm): void {
    alert('Guardar usuario')
    const {nombre, rol, edad} = form.value;

    const user = {nombre, rol, edad};

    const userJson = JSON.stringify(user);
    this.userSvc.putUser(this.editingUserId, userJson).subscribe({
      next: (user: any) => {
        alert('Usuario actualizado');
      },
      error: (error) => {
        alert('Error al actualizar usuario');
      },
      complete: () => {
        console.log('Finalizó');
        this.editingUserId = -1

      }
    });
  }

  cancelEdit(): void {
    this.editingUserId = -1
    alert('Cancelar edición');
  }

  toggleFilterForm(): void {
    this.showFilterForm = 1;
  }

  applyFilters() {
    
  }
}

@NgModule({
  declarations: [UserListComponent],
  imports: [CommonModule, FormsModule],
  exports: [UserListComponent]
})

export class UserListModule {
}
