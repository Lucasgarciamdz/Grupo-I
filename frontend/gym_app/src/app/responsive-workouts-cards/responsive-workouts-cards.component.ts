import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-responsive-workouts-cards',
  templateUrl: './responsive-workouts-cards.component.html',
  styleUrls: ['./responsive-workouts-cards.component.css']

})
export class ResponsiveWorkoutsCardsComponent {
  @Input()
  title!: string;
  @Input() 
  items!: { image: string, title: string, description: string, buttonText: string }[];
}
