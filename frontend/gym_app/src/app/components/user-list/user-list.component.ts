import { CommonModule, Location } from '@angular/common';
import { Component, NgModule, OnInit, ViewChild } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { FormsModule, NgForm } from "@angular/forms";
import { Router } from '@angular/router';
import { HttpParams } from '@angular/common/http';

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
  showNoFilter: number = 0;

  minAge: number = 0;
  maxAge: number = 0;
  rol: string = '';

  filterOption: string = '';

  pageNumber: number = 1;
  perPage: number = 10;
  noMoreUsers: boolean = false;

  @ViewChild('tableWrapper')
  tableWrapper: any;

  constructor(private userSvc: UsuariosService, private router: Router, private location: Location) {
  }

  ngOnInit() {
    const params = new HttpParams()
    .set('page', this.pageNumber.toString())
    .set('perpage', this.perPage.toString());
    this.userSvc.getUsers().subscribe({
      next: (users: any) => {
        if (users.usuario?.length < this.perPage) {
          this.noMoreUsers = true;
        }
          this.users = users.usuario;
          console.log(this.users);
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
    this.location;
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
    this.filterOption = ''

    if (this.showFilterForm === 1) {
      this.showFilterForm = 0;
    }
    else {
      this.showFilterForm = 1;
    }
  }

  applyFilters() : void {
    this.showFilterForm = 0
    this.showNoFilter = 1
    if (this.filterOption === 'rol') {
      console.log(this.rol);
      this.userSvc.getUsersByRol(this.rol).subscribe({
        next: (data: any) => {
          this.users = data.usuario
          console.log('Filtered users by Rol:', data);
        },
        error: (error) => {
          console.error('Error filtering by Rol:', error);
        }
      });
    } else if (this.filterOption === 'age') {

      console.log(this.minAge)
      console.log(this.maxAge)

      this.userSvc.getUsersByAge(this.minAge, this.maxAge).subscribe({
        next: (data: any) => {
          this.users = data.usuario
          console.log('Filtered users by Age:', data);
        },
        error: (error) => {
          console.error('Error filtering by Age:', error);
        }
      });
    } else {
      this.showNoFilter = 0
    }
  }

  resetFilters(): void {

    if (this.filterOption === 'rol') {
      this.rol = ''; // Reset Rol filter
    } else if (this.filterOption === 'age') {
      this.minAge = 0; // Reset Min Age filter
      this.maxAge = 0; // Reset Max Age filter
    }

    this.pageNumber = 1;
    this.showNoFilter = 0

    const params = new HttpParams()
    .set('page', this.pageNumber.toString())
    .set('perpage', this.perPage.toString());
    this.userSvc.get("/usuarios", params.toString()).subscribe({
      next: (users: any) => {
        if (users.usuario?.length < this.perPage) {
          this.noMoreUsers = true;
        }
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

  loadMore(): void {
    this.pageNumber++;
    let params = new HttpParams()
      .set('page', this.pageNumber.toString())
      .set('perpage', this.perPage.toString());

    if (this.filterOption === 'rol') {
      params = params.set('rol', this.rol);
    } else if (this.filterOption === 'age') {
      params = params.set('minAge', this.minAge.toString());
      params = params.set('maxAge', this.maxAge.toString());
    }

    this.userSvc.get("/usuarios", params.toString()).subscribe({
      next: (users: any) => {
        if (users.usuario?.length < this.perPage) {
          this.noMoreUsers = true;
        }
        this.users = this.users?.concat(users.usuario);
        setTimeout(() => {
          if (this.tableWrapper) {
            this.tableWrapper.nativeElement.style.maxHeight = '600px';
            this.tableWrapper.nativeElement.style.overflowY = 'auto';
          }
        });
      },
      error: (err: any) => {
        console.error(err);
      }
    });
  }
}

@NgModule({
  declarations: [UserListComponent],
  imports: [CommonModule, FormsModule],
  exports: [UserListComponent]
})

export class UserListModule {
}