import {Component, NgModule, OnInit, ViewChild} from '@angular/core';
import {UsuariosService} from 'src/app/services/usuarios.service';
import {FormsModule, NgForm} from "@angular/forms";

@Component({
  selector: 'app-clases-list',
  templateUrl: './clases-list.component.html',
  styleUrls: ['./clases-list.component.css']
})
export class ClasesListComponent {


  @ViewChild('userForm')
  userForm!: NgForm;

  editingUserId: number = 0;

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
    this.editingUserId = id;
    alert('Editar usuario con id ' + id)
  }

  deleteUser(id: number): void {
    this.userSvc.deleteUser(id).subscribe({
      next: (user: any) => {
        alert('Usuario eliminado');
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
        this.editingUserId = 0

      }
    });
  }


  cancelEdit(): void {
    alert('Cancelar edición');
  }
  @NgModule({
    declarations: [ClasesListComponent],
    imports: [CommonModule, FormsModule],
    exports: [ClasesListComponent]
  })
}
