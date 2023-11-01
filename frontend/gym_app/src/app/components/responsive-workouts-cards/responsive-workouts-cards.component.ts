import { Component, Input, OnInit } from '@angular/core';
import { ClasesService } from '../../services/clases.service';
import { JWTService } from '../../services/jwt.service';

@Component({
  selector: 'app-responsive-workouts-cards',
  templateUrl: './responsive-workouts-cards.component.html',
  styleUrls: ['./responsive-workouts-cards.component.css']
})
export class ResponsiveWorkoutsCardsComponent {
  @Input()
  title!: string;
  @Input() 
  // items!: {title: string | number, description: string, buttonText: string }[];
  items!: { image: string, title: string | number, description: string, buttonText: string, id_clase: number }[];

}

