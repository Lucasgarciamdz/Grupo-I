import { HttpParams } from '@angular/common/http';
import { Component, ViewChild, OnInit, ElementRef } from '@angular/core';
import {NgForm} from "@angular/forms";
import { BaseService } from 'src/app/services/base.service';
@Component({
  selector: 'app-clases-list',
  templateUrl: './clases-list.component.html',
  styleUrls: ['./clases-list.component.css']
})
export class ClasesListComponent implements OnInit{
  
  @ViewChild('tableWrapper') tableWrapper!: ElementRef;

  @ViewChild('clasesForm')
  clasesForm!: NgForm;

  editingClaseId: number = 0;

  clases: any[] | undefined;

  noMoreclases: boolean = false;

  pageNumber: number = 1;

  perPage: number = 10;

  constructor(private backSvc: BaseService) {
  }


  ngOnInit() {
    this.backSvc.get("clases", { page: this.pageNumber, perpage: this.perPage }).subscribe({
      next: (clases: any) => {
        this.clases = clases.clase;
      },
      error: (err: any) => {
        console.error(err);
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


  // ...

  loadMore(): void {
    this.pageNumber++;
    const params = new HttpParams()
      .set('page', this.pageNumber.toString())
      .set('perpage', this.perPage.toString());
    this.backSvc.get("clases", params.toString()).subscribe({
      next: (clases: any) => {
        if (clases.clase?.length < this.perPage) {
          this.noMoreclases = true;
        }
        this.clases = this.clases?.concat(clases.clase);
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


  saveclases(form: NgForm): void {
    alert('Guardar clase')
    const {tipo} = form.value;

    const clases = {tipo};

    const clasesJson = JSON.stringify(clases);

    const strId = (this.editingClaseId).toString(10)

    console.log(clasesJson);
    console.log(strId);
    
    this.backSvc.put("clase/" + strId, clasesJson).subscribe({
      next: (clases: any) => {
        alert('Clase actualizada');
      },
      error: (error) => {
        alert('Error al actualizar clase');
      },
      complete: () => {
        console.log('Finalizó');
        this.editingClaseId = 0

      }
    });
  }

  cancelEdit(): void {
    alert('Cancelar edición');
    this.editingClaseId = 0
  }

}
