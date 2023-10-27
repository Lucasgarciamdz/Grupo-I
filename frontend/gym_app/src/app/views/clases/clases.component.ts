import { Component } from '@angular/core';
import { ClassCardComponent } from '../../components/class-card/class-card.component';


@Component({
  selector: 'app-clases',
  templateUrl: './clases.component.html',
  styleUrls: ['./clases.component.css']
})
export class ClasesComponent {
  get isToken() {
    return localStorage.getItem('token');
  }

  classItems = [
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
