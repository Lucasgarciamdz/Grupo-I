import {Component, ViewChild} from '@angular/core';
import {NgForm} from "@angular/forms";
import {ProfesoresService} from "../../services/profesores.service";

@Component({
  selector: 'app-profesores-list',
  templateUrl: './profesores-list.component.html',
  styleUrls: ['./profesores-list.component.css']
})
export class ProfesoresListComponent {
  @ViewChild('userForm')
  userForm!: NgForm;

  editingUserId: number = 0;

  users: any[] | undefined;

  constructor(private profSvc: ProfesoresService) {
  }

  ngOnInit() {
    this.profSvc.getProfesores().subscribe({
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


  editProfesor(id: number): void {
    this.editingUserId = id;
    alert('Editar usuario con id ' + id)
  }

  deleteProfesor(id: number): void {
    this.profSvc.deleteProfesor(this.editingUserId).subscribe({
      next: (profesor: any) => {
        alert('Profesor eliminado');
      },
      error: (error) => {
        alert('Error al eliminar profesor');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }


  saveProfesor(form: NgForm): void {
    alert('Guardar usuario')
    const {nombre, rol, edad} = form.value;

    const prof = {nombre, rol, edad};

    const profJson = JSON.stringify(prof);
    this.profSvc.putProfesor(this.editingUserId, profJson).subscribe({
      next: (user: any) => {
        alert('Profesor actualizado');
      },
      error: (error) => {
        alert('Error al actualizar profesor');
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
}
