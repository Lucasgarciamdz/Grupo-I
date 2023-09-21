import { Component } from '@angular/core';

@Component({
  selector: 'app-stud-work',
  templateUrl: './stud-work.component.html',
  styleUrls: ['./stud-work.component.css']
})
export class StudWorkComponent {

  
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
