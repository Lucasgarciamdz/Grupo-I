import { Component, OnInit } from '@angular/core';
import { ClasesService } from 'src/app/services/clases.service';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  get isToken() {
    return localStorage.getItem('token');
  }

  pageNumber: number = 1;
  perPage: number = 10;

  searchText = '';
  filterApplied = false;

  clasesMasPopulares: any[] = [];
  clasesMasIntensas: any[] = [];
  responseClases: any[] = [];
  clases: any[] = [];
  filteredClases: any[] = [];

  workoutItemsPopulares: any[] = [];
  workoutItemsIntensas: any[] = [];
  workoutItems: any[] = [];


  constructor(private clasesService: ClasesService) { }

  ngOnInit() {
    const params = new HttpParams()
    .set('page', this.pageNumber.toString())
    .set('perpage', this.perPage.toString());

    this.clasesService.getClases().subscribe({
      next: (response: any) => {
        console.log('response: ', response.clase);
        this.clases = response.clase.map((clase: any) => ({
          image: clase.imagen,
          title: 'Clase ' + clase.id,
          description: clase.descripcion,
          buttonText: 'Ver Clase',
          id_clase: clase.id,
          link: '/views/class/' + clase.id,
          tipo: clase.tipo
        }));
      },
      error: (error) => {
        console.error(error);
      },
      complete: () => {
        console.log('Finalizó');
      }
    });

    console.log('clases: ', this.clases);

    this.clasesService.getClasesMasPopulares().subscribe({
      next: (response: any[]) => {
        console.log('response 2: ', response);
        this.clasesMasPopulares = response;
        this.workoutItemsPopulares = this.clasesMasPopulares.map(clase => ({
          image: clase.imagen,
          title: 'Clase ' + clase.id,
          description: clase.descripcion,
          buttonText: 'Ver Clase',
          id_clase: clase.id,
          link: '/views/class/' + clase.id,
          tipo: clase.tipo
        }));
      },
      error: (error) => {
        console.error(error);
      },
    });

    this.clasesService.getClasesMasIntensas().subscribe({
      next: (response: any[]) => {
        this.clasesMasIntensas = response;
        this.workoutItemsIntensas = this.clasesMasIntensas.map(clase => ({
          image: clase.imagen,
          title: 'Clase ' + clase.id,
          description: clase.descripcion,
          buttonText: 'Ver Clase',
          id_clase: clase.id,
          link: '/views/class/' + clase.id,
          tipo: clase.tipo
        }));
      },
      error: (error) => {
        console.error(error);
      },
    });
  }

  applyFilter() {
    this.filterApplied = true;
    this.filterClasses();
  }

  filterClasses() {
    this.filteredClases = this.clases.filter(clase => clase.tipo.includes(this.searchText));
  }

  clearFilter() {
    this.searchText = '';
    this.filterApplied = false;
    this.filterClasses();
  }

  getAllClasses() {
    this.filterApplied = true;
  }
}