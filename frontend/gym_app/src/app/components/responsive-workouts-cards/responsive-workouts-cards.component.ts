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
  items!: { image: string, title: string, description: string, buttonText: string }[];
}

