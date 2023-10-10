import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  get isToken() {
    return localStorage.getItem('token');
  }

  workoutItems = [
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

