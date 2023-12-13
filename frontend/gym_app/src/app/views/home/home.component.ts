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
  getAll = false;

  clasesMasPopulares: any[] = [];
  clasesMasIntensas: any[] = [];
  responseClases: any[] = [];
  clases: any[] = [];
  filteredClases: any[] = [];

  workoutItemsPopulares: any[] = [];
  workoutItemsIntensas: any[] = [];
  workoutItems: any[] = [];
  workoutItemsFiltered: any[] = [];

  constructor(private clasesService: ClasesService) { }

  ngOnInit() {
    const params = new HttpParams()
    .set('page', this.pageNumber.toString())
    .set('perpage', this.perPage.toString());

    this.clasesService.getClasesAll().subscribe({
      next: (response: any[]) => {;
        // console.log('response 1: ', response);
        this.clases = response;
        this.workoutItems = this.clases.map(clase => ({
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
      }
    });

    this.clasesService.getClasesMasPopulares().subscribe({
      next: (response: any[]) => {
        // console.log('response 2: ', response);
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
    console.log('filteredClases: ', this.filteredClases);
    this.workoutItemsFiltered = this.filteredClases.map(clase => ({
      image: clase.imagen,
      title: 'Clase ' + clase.id,
      description: clase.descripcion,
      buttonText: 'Ver Clase',
      id_clase: clase.id,
      link: '/views/class/' + clase.id,
      tipo: clase.tipo
    }));
  }

  clearFilter() {
    this.searchText = '';
    this.filterApplied = false;
    this.getAll = false
    this.filterClasses();
  }

  getAllClasses() {
    this.getAll = true;
  }
}