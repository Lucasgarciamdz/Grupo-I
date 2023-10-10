import {Component, NgModule, OnInit, ViewChild} from '@angular/core';
import {FormsModule, NgForm} from "@angular/forms";
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-clases-list',
  templateUrl: './clases-list.component.html',
  styleUrls: ['./clases-list.component.css']
})
export class ClasesListComponent {


  @ViewChild('clasesForm')
  clasesForm!: NgForm;

  editingClaseId: number = 0;

  clases: any[] | undefined;

  constructor(private backSvc: BaseService) {
  }

  ngOnInit() {
    this.backSvc.get("clases").subscribe({
      next: (clases: any) => {
        this.clases = clases.clase;
      },
      error: (error) => {
        alert('Error al obtener usuarios');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }


  editclases(id: number): void {
    this.editingClaseId = id;
    alert('Editar clase con id ' + id)
  }

  deleteclases(id: number): void {
    this.backSvc.delete("clases" + id).subscribe({
      next: (clases: any) => {
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


  saveclases(form: NgForm): void {
    alert('Guardar clase')
    const {tipo} = form.value;

    const clases = {tipo};

    const clasesJson = JSON.stringify(clases);

    const strId = (this.editingClaseId).toString(10)
    this.backSvc.put(strId, clasesJson).subscribe({
      next: (clases: any) => {
        alert('Usuario actualizado');
      },
      error: (error) => {
        alert('Error al actualizar usuario');
      },
      complete: () => {
        console.log('Finalizó');
        this.editingClaseId = 0

      }
    });
  }

  cancelEdit(): void {
    alert('Cancelar edición');
  }

}
