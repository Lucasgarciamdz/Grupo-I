import { Component } from '@angular/core';
import { Location } from '@angular/common';
import { ProfesoresService } from 'src/app/services/profesores.service';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-profesor-check',
  templateUrl: './profesor-check.component.html',
  styleUrls: ['./profesor-check.component.css']
})
export class ProfesorCheckComponent {

  users: any[] | undefined;

  pageNumber: number = 1;
  perPage: number = 10;
  noMoreUsers: boolean = false;

  constructor(private profSvc: ProfesoresService, private location: Location) {
  }

  ngOnInit() {
    const params = new HttpParams()
      .set('page', this.pageNumber.toString())
      .set('perpage', this.perPage.toString());
    this.profSvc.getProfesores().subscribe({
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
    console.log("Re piola se recargó la página");
  }

  rejectProf(id: number): void {
    this.profSvc.rejectProf(id).subscribe({
      next: (user: any) => {
        alert('Profesor rechazado');
        this.reloadPage();
      },
      error: (error) => {
        alert('Error al rechazar usuario');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }

  acceptProf(id: number, claseId: number): void {
    this.profSvc.acceptProf(id, claseId).subscribe({
      next: (user: any) => {
        alert('Profesor aceptado y asociado a la clase');
        this.reloadPage();
      },
      error: (error) => {
        alert('Error al aceptar y asociar profesor a la clase');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }
}
