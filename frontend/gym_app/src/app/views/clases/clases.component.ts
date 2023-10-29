import { Component } from '@angular/core';

@Component({
  selector: 'app-clases',
  templateUrl: './clases.component.html',
  styleUrls: ['./clases.component.css']
})
export class ClasesComponent {
  get isToken() {
    return localStorage.getItem('token');
  }

  planificaciones: any[] = [

  ];
  
  title: string = 'My Classes';
  
  items: { image: string, title: string, description: string, buttonText: string }[] = [
    {
      image: 'assets/clases/clase1.jpg',
      title: 'Clase 1',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    },
    {
      image: 'assets/clases/clase2.jpg',
      title: 'Clase 2',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    },
    {
      image: 'assets/clases/clase3.jpg',
      title: 'Clase 3',
      description: 'Fuerza',
      buttonText: 'Ver Clase'
    },
  ];
}
